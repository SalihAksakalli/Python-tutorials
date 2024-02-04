class calisan:
    def __init__(self,name,surname,age):
        self.name = name 
        self.surname = surname
        self.age =  age
        
        # Class'a bağlı olan fonksiyonlara method  denir
    def show_info(self):
        print(f"Ad: {self.name} Soyad : {self.surname}  Yaş : {self.age}")



calisan1 = calisan("Mustafa","Aksakalli",12)
#print(calisan1.name,calisan1.surname,calisan1.age)

calisan1.show_info()

calisan2 = calisan("Salih","Aksakalli",21)
# print(calisan2.name,calisan2.surname,calisan2.age)

calisan2.show_info()