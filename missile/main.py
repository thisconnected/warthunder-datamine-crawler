#!/usr/bin/env python3

from missile import Missile
import csv

missile_preset = [
    # "su_pl8",
    # "su_pl5e2",
    # "fr_r_550_magic_2",
    # "su_r_73",
    # "us_aim9m_sidewinder",
    # "cn_pl12",
    # "us_aim_120a",
    # "us_aim_120b",
    # "fr_mica_em",
    # "il_derby",
    # "jp_aam4",
    # "su_r_77",
    # "su_r_77_1",
    # "us_aim_54a",
    # "us_aim_54c",
    # "cn_pl12",
    # "cn_sd10a",
    # "ir_fakour_90"
    # "su_9m123",
    # "su_9m127",
    # "su_9m120m_laser_guided",
    # "su_9m120",
    # "su_9m133fm3_kornet"
    # "euro_hot3",
    # "euro_hot2",
    # "euro_hot",
    # "us_bgm_71_tow_heli",
    # "us_bgm_71_tow2_heli",
    # "cn_hj_8a",
    # "cn_hj_8c",
    # "cn_hj_8e",
    # "cn_hj_8h",
    # "su_9m114",
    # "su_9m17m",
    # "fr_ss_11",
    # "fr_ss_12",
    # "swd_rb53",
    # "us_aim7f_sparrow",
    # "us_aim7e2_dogfight_sparrow",
    # "uk_skyflash_aim_7_dogfight",
    # "su_r_23r",
    # "su_r_24r",
    # "su_r_27r",
    # "fr_matra_super_530f",
    # "fr_matra_super_530d",
    # "fr_r_530_matra_radar",
    # "fr_aa20",
    # "cn_pf10"
    # "uk_brimstone_dm",
    # "su_9m127",
    "su_grom_1",
    "su_kh_38ml",
    "us_agm_65d",
    "us_agm_65g",
    "su_kh_29td",
    "fr_as30l",
    "uk_pgm_500_iir",
    "uk_pgm_500",
    "fr_250kg_aasm_250_hammer_laser",
    "fr_500kg_aasm_500_hammer_laser",

    ]

missile_list = []
missile_list.append(Missile.missile_description())
missile_list.append(Missile.missile_units())

for missile in missile_preset:
    new_missile = Missile(missile)
    missile_list.append(new_missile.missile_calculate())


transposed = list(map(list, zip(*missile_list)))


# with open("test.csv", "w") as csvfile:
#     writer = csv.writer(csvfile, delimiter=";")
#     writer.writerow(Missile.missile_description())
#     for missile in missile_list:
#         print(missile)
#         writer.writerow(missile)

with open("missiles.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    for row in transposed:
        writer.writerow(row)
