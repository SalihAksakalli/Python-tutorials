#    Çalışan (isim,soyisim,email,maas) ---> Yazılımcı 
#                                             ---> Backend
#                                             ---> Frontend


# Çalışan (isim,soyisim,email,maas) ---> müdür
#                                             ---> Ar - Ge müdürü
#                                             ---> Ürün Müdürü
#                                             ---> Genel Müdür



class Calisan:
    zam_orani = 1.3
    def __init__(self,isim ,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@sirket.com"
    
    def bilgilerini_göster(self):
        return f" isim : {self.isim} soyisim : {self.soyisim} Maas : {self.maas}"


Calisan1 = Calisan("salih","Aksakalli",10000)
Calisan2 = Calisan("mustafa","Aksakalli",15000)


# print(Calisan1.email)


class Yazılımcı(Calisan):
    def __init__(self, isim, soyisim, maas,bildigidil):
        super().__init__(isim,soyisim,maas)
        self.bildigidil = bildigidil

    zam_orani = 1.8
    def bilgilerini_göster(self):
        return f" isim : {self.isim} soyisim : {self.soyisim} Maas : {self.maas}  Bildigi Dil : {self.bildigidil}"

    def dilini_söyle(self):
        return f" Bildigim Dil : {self.bildigidil}"


class Yonetici(Calisan):
    def __init__(self, isim, soyisim, maas,calisanlar = None):
        super().__init__(isim, soyisim, maas)

        if calisanlar == None:
            self.calisanlar = []
        else :
            self.calisanlar = calisanlar

    def calisan_ekle(self,Calisan):
        if Calisan not in self.calisanlar:
            self.calisanlar.append(Calisan)



    def calisan_sil(self,Calisan):
        if Calisan  in self.calisanlar:
            self.calisanlar.remove(Calisan)


    def calisanlari_göster(self):
        for calisan in self.calisanlar:
            print(calisan.bilgilerini_göster())




Yazılımcı1 = Yazılımcı("ikra","Aksakalli",10000,"python")
Yazılımcı2 = Yazılımcı("zeynep","Aksakalli",14000,"C")



# print(Yazılımcı1.email)
# print(Yazılımcı1.dilini_söyle())
# print(Yazılımcı2.dilini_söyle())
# print(Yazılımcı1.zam_orani)
# print(Calisan1.zam_orani)



yonetici1 = Yonetici("Şakir","Aksakalli",24000)

yonetici1.calisan_ekle(Yazılımcı1)
yonetici1.calisan_ekle(Calisan1)

yonetici1.calisanlari_göster()
print("************************************")



yonetici1.calisan_sil(Yazılımcı1)
yonetici1.calisanlari_göster()


yonetici2 = Yonetici("Muhammed","Yılmaz",17000,[Yazılımcı1,Yazılımcı2,Calisan1])
yonetici2.calisanlari_göster()



