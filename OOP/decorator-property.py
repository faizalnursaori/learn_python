class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age # Atribut "private"
    
    @property
    def age(self): # Getter
        print("Mengambil umur...")
        return self._age
    
    @age.setter
    def age(self, value): # Setter
    # Memvalidasi dan mengatur nilai aribut age agar tidak negatif
        if value < 0:
            raise ValueError("Umur tidak boleh negatif")
        print(f"Menetapkan umur ke {value}")
        self._age = value

    @age.deleter
    def age(self):
        print("Menghapus umur...")
        del self._age

p1 = Person("Faizal", 25)
print(p1.age) # Memanggil getter

p1.age = -30 # Memanggil setter => Error kalau negatif
p1.age = 30 # Memanggil setter

print(p1.age)

del p1.age
print(p1.age) #Error karena valuenya 0
