# operasi aritmatika (x : + -)
print(">>> Operasa Aritmatika <<<\n") 

# penjumlahan
a = 17
b = 3
hasil = a + b
print(a, "+", b, "=", hasil)

# pengurangan -
# perkalian *
# pembagian /
# perpangkatan **
# modulus %
# floor divison //

# pengurangan -
hasil = a - b
print(a, "-", b, "=", hasil)

# perkalian *
hasil = a * b
print(a, "*", b, "=", hasil)

# pembagian /
hasil = a / b
print(a, "/", b, "=", hasil)

# perpangkatan **
hasil = a ** b
print(a, "**", b, "=", hasil)

# modulus (sisa bagi)
hasil = a % b
print(a, "modulus", b, "=", hasil)

# floor divison // (pembulatan)
hasil = a // b
print(a, "floor div", b, "=", hasil)

# operasi prioritas
# 1. ()
# 2. pangkat akar
# 3. x :
# 4. + -

print("\n>>> Operasi Prioritas <<<\n")

# 1. ()
hasil1 = (5 + 3) * 2
print("(5 + 3) * 2 =", hasil1)

# 2. pangkat akar
hasil2 = 2 ** 3 * 2
print("2 ** 3 * 2 =", hasil2)

# 3. * :
hasil3 = 10 + 6 / 2
print("10 + 6 / 2 =", hasil3)

# 4. + -
hasil4 = 10 - 3 + 2
print("10 - 3 + 2 =", hasil4)

# contoh gabungan 
print("\n>>> Contoh gabungan <<<\n") 
hasil5 = 10 + 2 * 3 ** 2 - (5 + 1)
print("10 + 2 * 3 ** 2 - (5 + 1) =", hasil5)
