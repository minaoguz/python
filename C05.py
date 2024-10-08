'''
Insan isimli bir sınıf tanımlayınız.
Bütün constructor parametreleri default değerlere sahip olacak, default contructor (__init__) içinde belirlenecektir.
Bu değerler; ad, soyad, yas, ulke, sehir olacaktır.Ek olarak yetenekler isimli bir boş dizi init fonksiyonu içinde tanımlanacaktır.
kisi_bilgileri isimli fonksiyon ile init fonksiyonu içinde belirlenen kisi bilgileri return’le döndürülecektir.
yetenek_ekle isimli fonksiyon ile init fonksiyonu içinde belirlenen yetenekler dizisine yetenekler eklenecektir.
- Bu classtan belirtilen bilgileri içeren bir nesne tanımlayınız.
- Tanımlanan nesneye yetenek ekleyiniz. (Bisiklete binmek, Python vs.)
- kisi_bilgileri fonksiyonu ile bu bilgileri console ekranında gösteriniz.
'''

class Insan:
    def __init__(self, ad="none", soyad="none", yas=0, ulke="none", sehir="none"):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []

    def kisi_bilgileri(self):
        return f"Ad: {self.ad}, Soyad: {self.soyad}, Yas: {self.yas}, Ulke: {self.ulke}, Sehir: {self.sehir}, Yetenekler: {', '.join(self.yetenekler) if self.yetenekler else 'Yetenek yok'}"

    def yetenek_ekle(self, yetenek):
        self.yetenekler.append(yetenek)

kisi = Insan(ad="Ali", soyad="Yılmaz", yas=25, ulke="Turkiye", sehir="Istanbul")

kisi.yetenek_ekle("Bisiklete binmek")
kisi.yetenek_ekle("Yemek yapmak")

print(kisi.kisi_bilgileri())