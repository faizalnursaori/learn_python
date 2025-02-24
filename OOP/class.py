#Struktur dasar Class
class NamaClass:
    # Konstruktor (__init__) untuk inisialisasi atribut
    def __init__(self, atribut1, atribut2):
        self.atribut1 = atribut1
        self.atribut2 = atribut2

    #Metode untuk melakukan aksi
    def metode(self):
        print(f"Atribut 1: {self.atribut1} Atribut2 : {self.atribut2}")

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def drive(self):
        print(f"You are driving {self.color} {self.model}")

car1 = Car("BMW", "Black")