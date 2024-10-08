'''
Kullanıcının girdiği vize1, vize2, final notlarına göre harf notunu hesaplayınız.
-vize1 toplam notun %30'una etki edecektir.
-vize2 toplam notun %30'una etki edecektir.
-final toplam notun %40'ına etki edecektir.

Bu değerler 0-100 arası kabul edilmelidir!
    Toplam Not >=  90 -----> AA
    Toplam Not >=  85 -----> BA
    Toplam Not >=  80 -----> BB
    Toplam Not >=  75 -----> CB
    Toplam Not >=  70 -----> CC
    Toplam Not >=  65 -----> DC
    Toplam Not >=  60 -----> DD
    Toplam Not >=  55 -----> FD
    Toplam Not <  55 -----> FF
'''


def harf_notu_hesapla(vize1, vize2, final):

    ortalama_not = (vize1 * 0.30) + (vize2 * 0.30) + (final * 0.40)
    print('Ortalama not: ', ortalama_not)

    if ortalama_not >= 90:
        return "AA"
    elif ortalama_not >= 85:
        return "BA"
    elif ortalama_not >= 80:
        return "BB"
    elif ortalama_not >= 75:
        return "CB"
    elif ortalama_not >= 70:
        return "CC"
    elif ortalama_not >= 65:
        return "DC"
    elif ortalama_not >= 60:
        return "DD"
    elif ortalama_not >= 55:
        return "FD"
    else:
        return "FF"


vize1 = int(input('vize 1 notunu giriniz: '))
vize2 = int(input('vize 2 notunu giriniz: '))
final = int(input('final notunu giriniz: '))

print(harf_notu_hesapla(vize1, vize2, final))
