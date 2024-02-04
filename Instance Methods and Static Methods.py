from datetime import date

class kisi:
    kisi_sayisi = 0
    def __init__(self,isim,yas):
        self.isim = isim
        self.yas = yas
        kisi.kisi_sayisi += 1
    
    def bilgilerini_soyle(self): #instance method 
        return f" isim : {self.isim} yas :  {self.yas}"
    
    @classmethod
    def kisiSayisiniSöyle(classmethod):
        return classmethod.kisi_sayisi
    
    @classmethod
    def string_ile_olustur(classmethod,str):
        isim,yas = str.split("-")
        return classmethod(isim,yas)
    @classmethod
    def dogum_yili_ile_olustur(classmethod,isim,dogum_yili):
        return classmethod(isim,date.today().year - dogum_yili)
    @staticmethod
    def dogum_yili_hesapla(kisi):
        return date.today().year - kisi.yas
        

kisi1 =  kisi("Salih",21)
kisi2 = kisi("mustafa",12)
kisi3 = kisi.string_ile_olustur("Ayşe-25")
kisi4 = kisi.dogum_yili_ile_olustur("hatcik",2000)
# print(kisi1.bilgilerini_soyle())
# print(kisi3.isim)
# print(kisi3.yas)

print(kisi4.isim,kisi4.yas)
print(kisi.kisiSayisiniSöyle())

print(kisi.dogum_yili_hesapla(kisi1))