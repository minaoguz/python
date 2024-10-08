'''
3 tane parametre alan bolunen_sayi_bulma isimli bir fonksiyon tanımlayınız.
Bu fonsiyon; min_sayi, max_sayi, bolen_sayi isimli parametreleri alsın.
Fonksiyon dışardan aldığı bu parametre değerlerini kullanarak, min_sayi ve max_sayi 
aralığındaki bolen_sayi değerine bölünen sayıları tam_bolunenler adlı bir diziye atayıp, listelesin.
tam_bolunenler dizisi ile min_sayi ve max_sayi arasındaki değerlerin sayısını return ile döndürsün.
'''

min_sayi = int(input('min sayi --> '))
max_sayi = int(input('max sayi --> '))
bolen_sayi = int(input('bolen sayi --> '))

def bolunen_sayi_bulma(min_sayi, max_sayi, bolen_sayi):

   tam_bolunenler = []

   for sayi in range(min_sayi, max_sayi + 1):
       if sayi % bolen_sayi == 0:
           tam_bolunenler.append(sayi)

   print(tam_bolunenler)

   return len(tam_bolunenler)

print(bolunen_sayi_bulma(min_sayi, max_sayi, bolen_sayi))