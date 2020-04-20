import requests
from bs4 import BeautifulSoup as bs

def hr_info():
    url = "https://www.koronavirus.hr/"
    r = requests.get(url)
    s = bs (r.text, "html.parser")
    hrv = s.find_all("strong")
    hrvv = s.find_all("li", class_="counter-updated")
    print("Zarazeni u Hrvatskoj: ", hrv[1].text.strip())
    print("Zarazeni u Svijetu: ", hrv[2].text.strip())
    print("Izliječeni u Hrvatskoj: ", hrv[3].text.strip())
    print("Izliječeni u Svijetu: ", hrv[4].text.strip())
    print("Preminuli u Hrvatskoj: ", hrv[5].text.strip())
    print("Preminuli u Svijetu: ", hrv[6].text.strip())
    print("Ažurirano: ", hrvv[0].text.strip()[9:-41])
def zg_info():
    url_zg = "https://www.koronavirus.hr/grad-zagreb/140"
    rzg = requests.get(url_zg)
    szg = bs(rzg.text, "html.parser")
    zg = szg.find_all("strong")
    print("Zaraženi u Gradu Zagrebu: ", zg[7].text.strip())
    print("Preminuli u Gradu Zagrebu: ", zg[8].text.strip())
    print("Ažurirano: ", zg[9].text.strip()[18:])
def dub_info():
    url_dub = "https://www.koronavirus.hr/dubrovacko-neretvanska/166"
    rdub = requests.get(url_dub)
    sdub = bs(rdub.text, "html.parser")
    dub = sdub.find_all("strong")
    print("Zaraženi u Dubrovačko-neretvanskoj županiji: ", dub[7].text.strip())
    print("Preminuli u Dubrovačko-neretvanskoj županiji: ", dub[8].text.strip())
    print("Ažurirano: ", dub[9].text.strip()[9:-12])

def st_info():
    url_st = "https://www.koronavirus.hr/splitsko-dalmatinska/164"
    rst = requests.get (url_st)
    ssd = bs (rst.text, "html.parser")
    st = ssd.find_all ("strong")
    print("Zaraženi u Splitsko-dalmatinskoj županiji: ", st[7].text.strip())
    print("Preminuli u Splitsko-dalmatinskoj županiji: ", st[8].text.strip())
    print("Ažurirano: ", st[9].text.strip()[9:])

def si_info():
    url_si = "https://www.koronavirus.hr/sibensko-kninska/162"
    rsi = requests.get(url_si)
    ssi = bs(rsi.text, "html.parser")
    si = ssi.find_all("strong")
    print("Zaraženi u Šibensko-kninskoj županiji: ", si[7].text.strip ())
    print("Preminuli u Šibensko-kninskoj županiji: ", si[8].text.strip ())
    print("Ažurirano: ", si[9].text.strip()[9:])

def zd_info():
    url_zd = "https://www.koronavirus.hr/zadarska/160"
    rzd = requests.get(url_zd)
    szd = bs(rzd.text, "html.parser")
    zd = szd.find_all("strong")
    print("Zaraženi u Zadarskoj županiji: ", zd[7].text.strip ())
    print("Preminuli u Zadarskoj županiji: ", zd[8].text.strip ())
    print("Ažurirano: ", zd[9].text.strip()[9:])
def ls_info():
    url_ls = "https://www.koronavirus.hr/licko-senjska/156"
    rls = requests.get(url_ls)
    sls = bs(rls.text, "html.parser")
    ls = sls.find_all("strong")
    print ("Zaraženi u Ličko-senjskoj županiji: ", ls[7].text.strip ())
    print ("Preminuli u Ličko-senjskoj županiji: ", ls[8].text.strip ())
    print ("Ažurirano: ", ls[10].text.strip ()[9:])

def kc_info():
    url_kc = "https://www.koronavirus.hr/karlovacka/146"
    rkc = requests.get (url_kc)
    skc = bs (rkc.text, "html.parser")
    kc = skc.find_all ("strong")
    print ("Zaraženi u Karlovačkoj županiji: ", kc[7].text.strip ())
    print ("Preminuli u Karlovačkoj županiji: ", kc[8].text.strip ())
    print ("Ažurirano: ", kc[9].text.strip ()[32:-1])

def pr_info():
    url_pr = "https://www.koronavirus.hr/primorsko-goranska/155"
    rpr = requests.get (url_pr)
    spr = bs (rpr.text, "html.parser")
    pr = spr.find_all ("strong")
    print ("Zaraženi u Primorsko-goranskoj županiji: ", pr[7].text.strip ())
    print ("Preminuli u Primorsko-goranskoj županiji: ", pr[8].text.strip ())
    print ("Ažurirano: ", pr[9].text.strip ()[9:-330])

def ist_info():
    url_is = "https://www.koronavirus.hr/istarska/165"
    ris = requests.get (url_is)
    sis = bs (ris.text, "html.parser")
    ist = sis.find_all ("strong")
    print ("Zaraženi u Istarskoj županiji: ", ist[7].text.strip ())
    print ("Preminuli u Istarskoj županiji: ", ist[8].text.strip ())
    print ("Ažurirano: ", ist[9].text.strip ()[9:])

def sm_info():
    url_sm = "https://www.koronavirus.hr/sisacko-moslavacka/144"
    rsm = requests.get (url_sm)
    ssm = bs (rsm.text, "html.parser")
    sm = ssm.find_all ("strong")
    print ("Zaraženi u Sisačko-moslavačkoj županiji: ", sm[7].text.strip ())
    print ("Preminuli u Sisačko-moslavačkoj županiji: ", sm[8].text.strip ())
    print ("Ažurirano: ", sm[9].text.strip ()[9:])

def zag_info():
    url_zag = "https://www.koronavirus.hr/zagrebacka/143"
    rzag = requests.get (url_zag)
    szag = bs (rzag.text, "html.parser")
    zag = szag.find_all ("strong")
    print ("Zaraženi u Zagrebačkoj županiji: ", zag[7].text.strip ())
    print ("Preminuli u Zagrebačkoj županiji: ", zag[8].text.strip ())
    print ("Ažurirano: ", zag[9].text.strip ()[9:])

def kr_info():
    url_kr = "https://www.koronavirus.hr/krapinsko-zagorska-zupanija/174"
    rkr = requests.get (url_kr)
    skr = bs (rkr.text, "html.parser")
    kr = skr.find_all ("strong")
    print ("Zaraženi u Krapinsko-zagorskoj županiji: ", kr[7].text.strip ())
    print ("Preminuli u Krapinsko-zagorskoj županiji: ", kr[8].text.strip ())
    print ("Ažurirano: ", kr[9].text.strip ()[9:])

def vz_info():
    url_vz = "https://www.koronavirus.hr/varazdinska/148"
    rvz = requests.get (url_vz)
    svz = bs (rvz.text, "html.parser")
    vz = svz.find_all ("strong")
    print ("Zaraženi u Varaždinskoj županiji: ", vz[7].text.strip ())
    print ("Preminuli u Varaždinskoj županiji: ", vz[8].text.strip ())
    print ("Ažurirano: ", vz[9].text.strip ()[9:-10])
def md_info():
    url_md = "https://www.koronavirus.hr/medjimurska/167"
    rmd = requests.get (url_md)
    smd = bs (rmd.text, "html.parser")
    md = smd.find_all ("strong")
    print ("Zaraženi u Međimurskoj županiji: ", md[7].text.strip ())
    print ("Preminuli u Međimurskoj županiji: ", md[8].text.strip ())
    print ("Ažurirano: ", md[9].text.strip ()[9:])

def kk_info():
    url_kk = "https://www.koronavirus.hr/koprivnicko-krizevacka/153"
    rkk = requests.get (url_kk)
    skk = bs (rkk.text, "html.parser")
    kk = skk.find_all ("strong")
    print ("Zaraženi u Koprivničko-križevačkoj županiji: ", kk[7].text.strip ())
    print ("Preminuli u Koprivničko-križevačkoj županiji: ", kk[8].text.strip ())
    print ("Ažurirano: ", kk[9].text.strip ()[9:])

def bj_info():
    url_bj = "https://www.koronavirus.hr/bjelovarsko-bilogorska/154"
    rbj = requests.get (url_bj)
    sbj = bs (rbj.text, "html.parser")
    bj = sbj.find_all ("strong")
    print ("Zaraženi u Bjelovarsko-bilogorskoj županiji: ", bj[7].text.strip ())
    print ("Preminuli u Bjelovarsko-bilogorsoj županiji: ", bj[8].text.strip ())
    print ("Ažurirano: ", bj[9].text.strip ()[9:-11])

def vp_info():
    url_vp = "https://www.koronavirus.hr/viroviticko-podravska/157"
    rvp = requests.get (url_vp)
    svp = bs (rvp.text, "html.parser")
    vp = svp.find_all ("strong")
    print ("Zaraženi u Virovitičko-podravskoj županiji: ", vp[7].text.strip ())
    print ("Preminuli u Virovitičko-podravskoj županiji: ", vp[8].text.strip ())
    print ("Ažurirano: ", vp[9].text.strip ()[9:])


def pz_info():
    url_pz = "https://www.koronavirus.hr/pozesko-slavonska/158"
    rpz = requests.get (url_pz)
    spz = bs (rpz.text, "html.parser")
    pz = spz.find_all ("strong")
    print ("Zaraženi u Požeško-slavonskoj županiji: ", pz[7].text.strip ())
    print ("Preminuli u Požeško-slavonskoj županiji: ", pz[8].text.strip ())
    print ("Ažurirano: ", pz[9].text.strip ()[9:-9])

def bp_info():
    url_bp = "https://www.koronavirus.hr/brodsko-posavska/159"
    rbp = requests.get (url_bp)
    sbp = bs (rbp.text, "html.parser")
    bp = sbp.find_all ("strong")
    print ("Zaraženi u Brodsko-posavskoj županiji: ", bp[7].text.strip ())
    print ("Preminuli u Brodsko-posavskoj županiji: ", bp[8].text.strip ())
    print ("Ažurirano: ", bp[9].text.strip ()[9:])

def os_info():
    url_os = "https://www.koronavirus.hr/osjecko-baranjska/161"
    ros = requests.get (url_os)
    sos = bs (ros.text, "html.parser")
    os = sos.find_all ("strong")
    print ("Zaraženi u Osječko-baranjskoj županiji: ", os[7].text.strip ())
    print ("Preminuli u Osječko-baranjksoj županiji: ", os[8].text.strip ())
    print ("Ažurirano: ", os[9].text.strip ()[9:])

def vu_info():
    url_vu = "https://www.koronavirus.hr/vukovarsko-srijemska/163"
    rvu = requests.get (url_vu)
    svu = bs (rvu.text, "html.parser")
    vu = svu.find_all ("strong")
    print ("Zaraženi u Vukovarskoj županiji: ", vu[7].text.strip ())
    print ("Preminuli u Vukovarskoj županiji: ", vu[8].text.strip ())
    print ("Ažurirano: ", vu[9].text.strip ()[9:-34])

hr_info()