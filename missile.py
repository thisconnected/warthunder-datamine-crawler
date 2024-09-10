from dataclasses import dataclass, fields
import re

DATAMINE_PATH = "/home/thisconnect/War-Thunder-Datamine"


@dataclass
class Missile:
    mass: float
    massEnd: float
    massEnd1: float
    timeFire: float
    timeFire1: float
    force: float
    force1: float
    startSpeed: float

    def _extract(self, string) -> float:
        return float(string.split(':')[1])

    def _load_param(self, fieldname) -> bool:
        temp = re.search(rf"{fieldname}\"[0-9\:\.\ ]*", self.source)
        if not temp:
            return False
        temp = self._extract(temp.group())
        setattr(self, fieldname, temp)

    def _load_all(self):
        for field in fields(self):
            setattr(self, field.name, None)
            self._load_param(field.name)

    def _open_file(self, filename) -> str:
        path = f"{DATAMINE_PATH}/aces.vromfs.bin_u/gamedata/weapons/rocketguns/{filename}.blkx"
        with open(path, "r") as f:
            string = f.read()
        return string

    def __init__(self, filename):
        self.name = filename
        self.source = self._open_file(filename)
        self._load_all()

    def missile_calculate(self) -> list:
        impulse1, impulse2, speed_after_boost1, speed_after_boost2, deltav1, deltav2, deltav_total = 0, 0, 0, 0, 0, 0, 0
        impulse1 = self.timeFire * self.force
        speed_after_boost1 = impulse1/((self.mass + self.massEnd)/2) + self.startSpeed
        deltav1 = speed_after_boost1 - self.startSpeed

        if self.massEnd1:
            impulse2 = self.timeFire1 * self.force1
            speed_after_boost2 = impulse2/((self.massEnd + self.massEnd1)/2) + speed_after_boost1
            deltav2 = speed_after_boost2 - speed_after_boost1
        else:
            speed_after_boost2 = speed_after_boost1

        deltav_total = deltav1 + deltav2

        return [
            self.name,
            self.startSpeed,
            self.mass,
            self.force,
            self.timeFire,
            self.massEnd,
            impulse1,
            speed_after_boost1,
            self.force1,
            self.timeFire1,
            self.massEnd1,
            impulse2,
            speed_after_boost2,
            deltav1,
            deltav2,
            deltav_total,
        ]

    @staticmethod
    def missile_description() -> list:
        return [
            "Name",
            "Start Speed",
            "Mass",
            "Force motor stage 1",
            "Time fire stage 1",
            "Mass end stage 1",
            "Impulse stage 1",
            "Speed after stage 1",
            "Force motor stage 2",
            "Time fire stage 2",
            "Mass end stage 2",
            "Impulse stage 2",
            "Speed after stage 2",
            "ΔV stage 1",
            "ΔV stage 2",
            "ΔV total",
        ]

    @staticmethod
    def missile_units() -> list:
        return [
            "N/A",
            "m/s",
            "kg",
            "N",
            "s",
            "kg",
            "Ns",
            "m/s",
            "N",
            "s",
            "kg",
            "Ns",
            "m/s",
            "m/s",
            "m/s",
            "m/s",
        ]
