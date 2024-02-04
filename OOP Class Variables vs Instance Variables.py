# Class Variables vs Instance Variables

class calisan:
    # zamorani = 1.1
    personelSayisi = 0
    def __init__(self,isim,maas):
        self.isim = isim
        self.maas = maas
        calisan.personelSayisi += 1

# calisan1 = calisan("Ali",100000)
# calisan2 = calisan("Salih",15000)


# print(calisan.zamorani)
# print(calisan1.zamorani)
# print(calisan2.zamorani)





# calisan.zamorani = 1.4

# print(calisan.zamorani)
# print(calisan1.zamorani)
# print(calisan2.zamorani)




# calisan1.zamorani = 1.4

# print(calisan.zamorani)
# print(calisan1.zamorani)
# print(calisan2.zamorani)

# print(calisan1.__dict__)
# print(calisan2.__dict__)

print(calisan.personelSayisi)
calisan1 = calisan("Ali",100000)
print(calisan.personelSayisi)
calisan2 = calisan("Salih",15000)
print(calisan.personelSayisi)
