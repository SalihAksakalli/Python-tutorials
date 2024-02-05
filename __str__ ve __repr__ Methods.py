# a  = "python"

# print(str(a))
# print(repr(a))


# from  datetime import date,datetime


# bugun =  date.today()
# print(bugun)
# print(str(bugun))
# print(repr(bugun))

class Futboller:
    def __init__(self,isim,soyisim,yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas

    def __str__(self):
        return f"Ad : {self.isim} Soyad : {self.soyisim} Yas : {self.yas}"
    
    def __repr__(self):
        return f'Furbolcu( "{self.isim}","{self.soyisim}",{self.yas})'


Futboller1 = Futboller("Ronaldo","cristiano",35)
print(Futboller1)
print(Futboller1.__repr__())