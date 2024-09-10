#!/usr/bin/env python3

from missile import Missile
import csv

missile_preset = [
    "su_pl8",
    "su_pl5e2",
    "fr_r_550_magic_2",
    "su_r_73",
    "us_aim9m_sidewinder",
    ]

missile_list = []

for missile in missile_preset:
    new_missile = Missile(missile)
    missile_list.append(new_missile.missile_calculate())

with open("test.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(Missile.missile_description())
    for missile in missile_list:
        writer.writerow(missile)
