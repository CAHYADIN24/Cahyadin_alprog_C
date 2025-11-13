# Mengambil input dari user

nama = input("Masukan Nama Anda : ")
print("Selamat datang ", nama)
print("nilai dari nama =", nama)
print(type(nama))

bil_int = int(input("Masukan bilangan bulat : "))
print("bilangan bulat adalah ", bil_int)
print("nilai dari bil_int =", bil_int)
print(type(bil_int))

bil_float = float(input("Masukan bilangan pecahan : "))
print("bilangan pecahan adalah ", bil_float)
print("nilai dari bil_float =", bil_float)
print(type(bil_float))

bil_bool = bool(input("Masukan bilangan true or false : "))
print("bilangan yang andala masukan adalah ", bil_bool)
print("nilai dari true or false =", bil_bool)
print(type(bil_bool))

# buatlah program dengan output sebagai berikut
# masukan nama anda :
# masukan umur anda :
# nama anda adalah (nama)
# tipe data dari nama anda adalah (tipe data dari nama)
# umur anda adalah (umur)
# tipe data dari umur anda adalah (tipe data dari umur)

nama = input("Masukan Nama Anda : ")
umur = int(input("Masukan Umur Anda : "))

print("Nama Anda Adalah", nama)
print("Tipe Data dari Nama Anda Adalah", type(nama))
print("Umur Anda Adalah", umur)
print("Tipe Data dari Umur Anda Adalah", type(umur))