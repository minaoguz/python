'''
sayi_atama ve sayi_okunusu isimli 2 tane fonksiyon tanımlayınız.
Bu fonksiyonlardan sayi_atama fonksiyonu 2 basamaklı bir sayıyı parametre olarak alsın
ve fonksiyon içinde bu değer bir değişkene atansın.
Daha sonra sayi_atama fonksiyonu içinde sayi_okunusu isimli fonksiyon çağırılarak
değişkene atanan sayının okunuşu string olarak verilsin.
sayi_atama fonksiyonu 2 basamaktan daha az yada daha fazla sayıyı kabul etmeyecektir.
'''

def sayi_atama(num):
    if (10 <= num <= 99) or (-99 <= num <= -10):
        return num
    else:
        print("Lütfen iki basamaklı bir sayı giriniz.")
        return None

def sayi_okunusu(num):
    valid_num = sayi_atama(num)

    if valid_num is not None:
        onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]
        birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]

        negatif = False
        if valid_num < 0:
            negatif = True
            valid_num = abs(valid_num)

        onlar_basamagi = valid_num // 10
        birler_basamagi = valid_num % 10

        okunus = onlar[onlar_basamagi] + " " + birler[birler_basamagi]

        if negatif:
            okunus = "Eksi " + okunus

        print("Sayının okunuşu:", okunus)

sayi_okunusu(59)
