from datetime import datetime 
import pymongo

def HesaplamaIzinYil(PTKIseGiristarihi):
    yeary = datetime.today().year
    monthy = datetime.today().month
    dayy = datetime.today().day
    girisyeary = PTKIseGiristarihi.year
    girismonthy = PTKIseGiristarihi.month
    girisdayy = PTKIseGiristarihi.day
    sonucyeary = yeary - girisyeary
    sonucmonthy = monthy - girismonthy
    sonucdayy = dayy - girisdayy
    #print("gün : ",dayy, "Ay : ", monthy,"yıl : ",yeary )
    #print("gün : ",girisdayy, "Ay : ", girismonthy,"yıl : ",girisyeary )
    #print("gün : ",sonucdayy, "Ay : ", sonucmonthy,"yıl : ",sonucyeary )
    HakedilenIzinYil = sonucyeary
    if sonucyeary == 0:
        HakedilenIzinYil = sonucyeary
    elif sonucmonthy == 0:
        if dayy < girisdayy:
            HakedilenIzinYil = sonucyeary - 1.0
    elif sonucmonthy < 0:
        HakedilenIzinYil = sonucyeary - 1.0
    print(HakedilenIzinYil)
    return HakedilenIzinYil

def HesaplamaIzinYilAyrilan(PTKIseGiristarihi, PTKIseCikistarihi):
    yeary = PTKIseCikistarihi.year
    monthy = PTKIseCikistarihi.month
    dayy = PTKIseCikistarihi.day
    girisyeary = PTKIseGiristarihi.year
    girismonthy = PTKIseGiristarihi.month
    girisdayy = PTKIseGiristarihi.day
    sonucyeary = yeary - girisyeary
    sonucmonthy = monthy - girismonthy
    sonucdayy = dayy - girisdayy
    #print("gün : ",dayy, "Ay : ", monthy,"yıl : ",yeary )
    #print("gün : ",girisdayy, "Ay : ", girismonthy,"yıl : ",girisyeary )
    #print("gün : ",sonucdayy, "Ay : ", sonucmonthy,"yıl : ",sonucyeary )
    HakedilenIzinYil = sonucyeary
    if sonucmonthy == 0:
        if dayy < girisdayy:
            HakedilenIzinYil = sonucyeary - 1.0
    elif sonucmonthy < 0:
        HakedilenIzinYil = sonucyeary - 1.0
    print(HakedilenIzinYil)
    return HakedilenIzinYil



def HesaplamaIzinGun(PTKIseGiristarihi):
    yeary = datetime.today().year
    monthy = datetime.today().month
    dayy = datetime.today().day
    girisyeary = PTKIseGiristarihi.year
    girismonthy = PTKIseGiristarihi.month
    girisdayy = PTKIseGiristarihi.day
    sonucyeary = yeary - girisyeary
    sonucmonthy = monthy - girismonthy
    sonucdayy = dayy - girisdayy
    print("gün : ",dayy, "Ay : ", monthy,"yıl : ",yeary )
    print("gün : ",girisdayy, "Ay : ", girismonthy,"yıl : ",girisyeary )
    print("gün : ",sonucdayy, "Ay : ", sonucmonthy,"yıl : ",sonucyeary )
    HakedilenIzinYil = sonucyeary
    if sonucmonthy == 0:
        if dayy < girisdayy:
            HakedilenIzinYil = sonucyeary - 1.0
    elif sonucmonthy < 0:
        HakedilenIzinYil = sonucyeary - 1.0
    print(HakedilenIzinYil)
    islem = 0
    islemgun = 0
    HakedilenIzinGun = 0
    if HakedilenIzinYil >=15:
        islem = HakedilenIzinYil - 14
        islemgun = islem * 26
        HakedilenIzinGun = 70 + 220 + islemgun
    elif HakedilenIzinYil < 15 and HakedilenIzinYil > 5:
        islem = HakedilenIzinYil - 5
        islemgun = islem * 20
        HakedilenIzinGun = 70 + islemgun
    elif HakedilenIzinYil <= 5 and HakedilenIzinYil >0:
        islemgun = HakedilenIzinYil * 14
        HakedilenIzinGun = islemgun
    
    return HakedilenIzinGun

def HesaplamaIzinGunAyrılan(PTKIseGiristarihi, PTKIseCikistarihi):
    yeary = PTKIseCikistarihi.year
    monthy = PTKIseCikistarihi.month
    dayy = PTKIseCikistarihi.day
    girisyeary = PTKIseGiristarihi.year
    girismonthy = PTKIseGiristarihi.month
    girisdayy = PTKIseGiristarihi.day
    sonucyeary = yeary - girisyeary
    sonucmonthy = monthy - girismonthy
    sonucdayy = dayy - girisdayy
    #print("gün : ",dayy, "Ay : ", monthy,"yıl : ",yeary )
    #print("gün : ",girisdayy, "Ay : ", girismonthy,"yıl : ",girisyeary )
    #print("gün : ",sonucdayy, "Ay : ", sonucmonthy,"yıl : ",sonucyeary )
    HakedilenIzinYil = sonucyeary
    if sonucmonthy == 0:
        if dayy < girisdayy:
            HakedilenIzinYil = sonucyeary - 1.0
    elif sonucmonthy < 0:
        HakedilenIzinYil = sonucyeary - 1.0
    print(HakedilenIzinYil)
    islem = 0
    islemgun = 0
    HakedilenIzinGun = 0
    if HakedilenIzinYil >=15:
        islem = HakedilenIzinYil - 14
        islemgun = islem * 26
        HakedilenIzinGun = 70 + 220 + islemgun
    elif HakedilenIzinYil < 15 and HakedilenIzinYil > 5:
        islem = HakedilenIzinYil - 5
        islemgun = islem * 20
        HakedilenIzinGun = 70 + islemgun
    elif HakedilenIzinYil <= 5 and HakedilenIzinYil >0:
        islemgun = HakedilenIzinYil * 14
        HakedilenIzinGun = islemgun
    
    return HakedilenIzinGun



    