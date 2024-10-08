'''
    50 soruluk, 4 yanlışın 1 doğruyu götürdüğü sınavda öğrencinin inputlarla girilen
    doğru yanlış sayısına göre aldığı puanı hesaplayan programı yazınız.
    Ogrenci isimli bir sınıf tanımlayınız.
    Bu sınıfın içinde ogrenci_adi, ogrenci_soyadi, ogrenci_sinif’ı değişkenleri bulunacaktır.
    Bu sınıftan nesne oluşturulurken bu bilgiler parametre olarak verilecektir.
    Soru diye bir sınıfınız olacaktır. Bu sınıfın net_sayisi ve hesapla isimli iki fonksiyon olacaktır.
    net_sayisi fonksiyonu doğru ve yanlış sayısını parametre olarak alıp öğrencinin kaç neti olduğunu bulacaktır.
    hesapla fonksiyonu net sayısını parametre olarak alıp öğrencinin puanını hesaplayacaktır.
    Her net 2 puan olacak şekilde öğrenci bilgileri ve puanı console ekranında gösterilecektir.
'''


class Ogrenci:
    def __init__(self, ogrenci_adi, ogrenci_soyadi, ogrenci_sinif):
        self.ogrenci_adi = ogrenci_adi
        self.ogrenci_soyadi = ogrenci_soyadi
        self.ogrenci_sinif = ogrenci_sinif

    def ogrenci_bilgileri(self):
        return f"Adı: {self.ogrenci_adi}, Soyadı: {self.ogrenci_soyadi}, Sınıf: {self.ogrenci_sinif}"


class Soru:
    def net_sayisi(self, dogru, yanlis):
        net = dogru - (yanlis // 4)
        return net

    def hesapla(self, net):
        puan = net * 2
        return puan


ogrenci_adi = input("Öğrencinin adı: ")
ogrenci_soyadi = input("Öğrencinin soyadı: ")
ogrenci_sinif = input("Öğrencinin sınıfı: ")

ogrenci = Ogrenci(ogrenci_adi, ogrenci_soyadi, ogrenci_sinif)

dogru = int(input("Doğru sayısı: "))
yanlis = int(input("Yanlış sayısı: "))

soru = Soru()

net = soru.net_sayisi(dogru, yanlis)

puan = soru.hesapla(net)

print("\nÖğrenci Bilgileri:")
print(ogrenci.ogrenci_bilgileri())
print(f"Net Sayısı: {net}")
print(f"Sınav Puanı: {puan}")
