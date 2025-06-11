from dataclasses import dataclass, fields
import re

# DATAMINE_PATH = "/data/WarThunder-dev"
DATAMINE_PATH = "/home/thisconnect/War-Thunder-Datamine"
FILE_EXTENSION = "blkx"
# FILE_EXTENSION = "blk"


@dataclass
class Missile:
    CxK: float
    caliber: float
    wingAreaMult: float
    mass: float
    massEnd: float
    massEnd1: float
    timeFire: float
    timeFire1: float
    force: float
    force1: float
    startSpeed: float
    finsAoaHor: float

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
        string = None
        folder = "rocketguns"
        try:
            with open(f"{DATAMINE_PATH}/aces.vromfs.bin_u/gamedata/weapons/{folder}/{filename}.{FILE_EXTENSION}", "r") as f:
                string = f.read()
        except Exception:
            print(f"could not find {filename} in {folder}")
        if not string:
            folder = "bombguns"
            try:
                with open(f"{DATAMINE_PATH}/aces.vromfs.bin_u/gamedata/weapons/{folder}/{filename}.{FILE_EXTENSION}", "r") as f:
                    string = f.read()
            except Exception:
                print(f"could not find {filename} in {folder}")
        if not string:
            folder = "groundmodels_weapons"
            try:
                with open(f"{DATAMINE_PATH}/aces.vromfs.bin_u/gamedata/weapons/{folder}/{filename}.{FILE_EXTENSION}", "r") as f:
                    string = f.read()
            except Exception:
                print(f"could not find {filename} in {folder}")
        if not string:
            folder = "fakeguns"
            try:
                with open(f"{DATAMINE_PATH}/aces.vromfs.bin_u/gamedata/weapons/{folder}/{filename}.{FILE_EXTENSION}", "r") as f:
                    string = f.read()
            except Exception:
                print(f"could not find {filename} in {folder}")
                print(f"{filename} doesnt exist")
                return None

        return string

    def __init__(self, filename):
        self.name = filename
        self.source = self._open_file(filename)
        if self.source is None:
            return
        self._load_all()

    def missile_calculate(self) -> list:
        if self.caliber:
            self.caliber = 10 * self.caliber

        impulse1, impulse2, speed_after_boost1, speed_after_boost2, deltav1, deltav2, deltav_total = 0, 0, 0, 0, 0, 0, 0
        # impulse = time * force
        impulse1 = self.timeFire * self.force
        # speed_after_boost
        speed_after_boost1 = (impulse1/((self.mass + self.massEnd)/2)) + self.startSpeed
        deltav1 = speed_after_boost1 - self.startSpeed

        if self.massEnd1:
            impulse2 = self.timeFire1 * self.force1
            speed_after_boost2 = impulse2/((self.massEnd + self.massEnd1)/2) + speed_after_boost1
            deltav2 = speed_after_boost2 - speed_after_boost1
        else:
            speed_after_boost2 = speed_after_boost1

        deltav_total = deltav1 + deltav2

        try:
            if self.massEnd1:
                wet_mass_ratio = (self.mass-self.massEnd1)/self.mass
            else:
                wet_mass_ratio = (self.mass-self.massEnd)/self.mass
        except ZeroDivisionError:
            print(f"mass={self.mass}, end1={self.massEnd1}, end={self.massEnd}")
            wet_mass_ratio = 0
        wet_mass_ratio = wet_mass_ratio * 100
        return [
            self.name,
            self.startSpeed,
            self.mass,
            self.force,
            self.timeFire,
            self.massEnd,
            impulse1,
            round(speed_after_boost1, 2),
            self.force1,
            self.timeFire1,
            self.massEnd1,
            impulse2,
            round(speed_after_boost2, 2),
            round(deltav1, 2),
            round(deltav2, 2),
            round(deltav_total, 2),
            self.CxK,
            self.caliber,
            self.wingAreaMult,
            self.finsAoaHor,
            round(wet_mass_ratio, 2),
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
            "CxK",
            "Caliber",
            "WingAreaMult",
            "Fin area",
            "Wet Mass Ratio"
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
            "N/A",
            "mm",
            "N/A",
            "N/A",
            "%"
        ]
