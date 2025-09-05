#!/usr/bin/env python3

from missile import Missile
import csv

missile_preset = [
    # spaa
    # "152mm_mim146",
    # "239mm_hq_17_user_cannon",
    # "152mm_9m311_rocket_launcher",
    # "163mm_roland_vt_1_launcher_user_cannon",
    # "160mm_sam_1c_launcher_user_cannon",
    # "80mm_type_91_launcher_user_cannon",
    # "120mm_9m37m_rocket_launcher",
    # "atam_mistral",
    # "us_aim92_stinger",
    # "su_9m39",
    # "su_9m336",
    # "72mm_hn_6_launcher_user_cannon",
    # newspa
    "170mm_57e6_rocket_launcher",
    "380mm_aster_30_user_cannon",
    "166mm_camm_user_cannon",
    "360mm_9m317m_user_cannon",
    "130mm_fb_10_rocket_launcher",
    "fb10a",
    "fb10",
    "127mm_iris_t_user_cannon",
    "127mm_aim_9x_user_cannon",
    "180mm_iris_t_sl_user_cannon",
    "178mm_sl_amraam_user_cannon",
    "160mm_spyder_launcher_user_cannon",
    # basic sraam
    # "su_pl5b",
    # "us_aim9d_sidewinder",
    # "il_shafrir_2",
    # "su_r_13m1",
    # "su_r_60",
    # "us_aim9e_sidewinder",
    # "us_aim9d_sidewinder",
    # "us_aim9j_sidewinder",
    # "us_aim9l_sidewinder",
    # "br_maa_1",
    # "fr_r_550_magic",
    # # advanced sraaam
    # "cn_pl8b",
    # "su_pl8",
    # "su_pl5e2",
    # "su_pl5c",
    # "su_pl5b",
    # "fr_r_550_magic_2",
    # "su_r_73",
    # "us_aim9m_sidewinder",
    # "cn_ty_90",
    # "il_pyton_4",
    # atgm
    # "180mm_2k4_rocket_launcher",
    # "125mm_9m113_rocket_launcher",
    # "9m112",
    # "9m119",
    # "9m117",
    # "9m117m1",
    # "su_9m120",
    # "su_9m133fm3_kornet",
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
    # "152mm_hj_9_launcher_user_cannon",
    # "110mm_spike_freccia_rocket_launchr_user_cannon",
    # "151mm_qn502cdd_rocket_launcher",
    "cn_akd_10",
    "cn_cm_502kg_he",
    "su_9m120m_laser_guided",
    "su_9m127",
    "su_9m123",
    "su_lmur",
    "euro_trigat_lr",
    "spike_er",
    "us_hellfire_agm_114_k",
    "us_agm_179_mr_ir",
    # arh
    # "cn_pl12",
    # "us_aim_120a",
    # "us_aim_120c_5",
    # "fr_mica_em",
    # "il_derby",
    # "jp_aam4",
    # "su_r_77",
    # "su_r_77_1",
    # "us_aim_54a",
    # "us_aim_54c",
    # "cn_pl12",
    # "cn_sd10a",
    # "ir_fakour_90",
    # "su_r_27er",
    # # sahr
    # "fr_matra_super_530d",
    # "fr_matra_super_530f",
    # "us_aim7f_sparrow",
    # "uk_skyflash_temp",
    # "cn_pf10",
    # "su_r_27r",
    # "us_aim7e2_dogfight_sparrow",
    # "uk_skyflash_aim_7_dogfight",
    # "su_r_24r",
    # "su_r_23r",
    # "fr_r_530_matra_radar",
    # "fr_aa20",
    # # plane agm
    # "uk_brimstone_dm",
    # "su_9m127",
    # "su_grom_1",
    # "su_kh_38ml",
    # "su_kh_29td",
    # "su_s_25l_rocket",
    # "us_agm_65d",
    # "us_agm_65g",
    # "fr_as30l",
    # "uk_pgm_500_iir",
    # "uk_pgm_500",
    # "fr_250kg_aasm_250_hammer_laser",
    # "fr_500kg_aasm_500_hammer_laser",
    # # asm
    # "us_agm_119a_penguin",
    # "gr_as34_kormoran",
    # "jp_asm1",
    # "jp_asm2",
    ]

missile_list = []
missile_list.append(Missile.missile_description())
missile_list.append(Missile.missile_units())

for missile in missile_preset:
    new_missile = Missile(missile)
    if new_missile.source is None:
        continue
    missile_list.append(new_missile.missile_calculate())


transposed = list(map(list, zip(*missile_list)))


# with open("test.csv", "w") as csvfile:
#     writer = csv.writer(csvfile, delimiter=";")
#     writer.writerow(Missile.missile_description())
#     for missile in missile_list:
#         print(missile)
#         writer.writerow(missile)


version_string = "temp"
try:
    with open("/home/thisconnect/War-Thunder-Datamine/aces.vromfs.bin_u/version", "r") as f:
        version_string = f.read()
except:  # noqa: E722
    pass

with open(f"{version_string}.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    for row in transposed:
        writer.writerow(row)
