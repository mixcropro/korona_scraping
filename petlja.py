from hr_corona import *
from texttable import Texttable

t = Texttable(max_width=170)
t.set_cols_dtype(['t','t','t','t','t','t','t'])
t.add_rows([['1 Grad Zagreb', '2 Zagrebačka županija', "3 Dubrovačko-neretvanska županija", "4 Splitsko-dalmatinska županija",
             "5 Šibensko-kninska županija", "6 Zadarska županija", "7 Ličko-senjska županija"],

            ['8 Karlovačka županija', "9 Primorsko-goranska županija", "10 Istarska županija",
             "11 Sisačko-moslavačka županija", "12 Krapinsko-zagorska županija", "13 Varaždinska županija", "14 Međimurska županija"],

            ['15 Koprivničko-križevačka županija', "16 Bjelovarsko-bilogorska županija", "17 Virovitičko-podravska županija",
             "18 Požeško-slavonska županija", "19 Brodsko-posavska županija", "20 Osječko-baranjska županija", "21 Vukovarska županija"]])
print(t.draw())

i = 1
while i > 0:
    br = input('Ukoliko želite znati potpune informacije za Hrvatsku i Svijet unesite 0, inače odaberite željenu županiju unošenjem broja: ')
    if br == "0":
        hr_info()
    elif br == "1":
        zg_info()
    elif br == "2":
        zag_info()
    elif br == "3":
        dub_info ()
    elif br == "4":
        st_info()
    elif br == "5":
        si_info()
    elif br == "6":
        zd_info()
    elif br == "7":
        ls_info()
    elif br == "8":
        kc_info()
    elif br == "9":
        pr_info()
    elif br == "10":
        ist_info()
    elif br == "11":
        sm_info()
    elif br == "12":
        kr_info()
    elif br == "13":
        vz_info()
    elif br == "14":
        md_info()
    elif br == "15":
        kk_info()
    elif br == "16":
        bj_info()
    elif br == "17":
        vp_info()
    elif br == "18":
        pz_info()
    elif br == "19":
        bp_info()
    elif br == "20":
        os_info()
    elif br == "21":
        vu_info()
    else:
        print("Krivi unos!\n")
    br2 = input("Ako želite završiti program unesite p i stisnite enter, inače stisni enter za nastavak. \n")
    if br2 == "p":
        i -= 1
    else:
        continue




