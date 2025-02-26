# Tanpa class Method
# class Hewan:
#     jumlah = 0  # Atribut class

#     def tambah():
#         Hewan.jumlah += 1  # Menyebut langsung class `Hewan`

# class Kucing(Hewan):
#     pass

# # Memanggil metode dari subclass
# Kucing.tambah()

# print(Hewan.jumlah)  # Output: 1
# print(Kucing.jumlah)  # Output: 1


# Menggunakan class Method

class Hewan:
    jumlah = 0

    @classmethod
    def tambah(cls):
        cls.jumlah += 1
        
class Kucing(Hewan):
    pass

class Anjing(Hewan):
    pass

k1 = Kucing.tambah()
k2 = Kucing.tambah()
a1 = Anjing.tambah()

print(Hewan.jumlah) # Output 0
print(Kucing.jumlah) # Output 2
print(Anjing.jumlah) # Output 1