# komparasi (true false)
# > < >= <= == != is is-not

x = 25   # 2 digit nim awal
y = 82   # 2 digit nim akhir

print("===== lebih dari (>) =====")
hasil = y > x
print(y, ">", x, "=", hasil)
hasil = x > y
print(x, ">", y, "=", hasil)

print("\n===== kurang dari (<) =====")
hasil = x < y
print(x, "<", y, "=", hasil)
hasil = y < x
print(y, "<", x, "=", hasil)

print("\n===== lebih dari sama dengan (>=) =====")
hasil = x >= 25
print(x, ">=", 25, "=", hasil)
hasil = y >= 85
print(y, ">=", 85, "=", hasil)

print("\n===== kurang dari sama dengan (<=) =====")
hasil = y <= 82
print(y, "<=", 82, "=", hasil)
hasil = x <= 20
print(x, "<=", 20, "=", hasil)

print("\n===== sama dengan (==) =====")
hasil = x == 25
print(x, "==", 25, "=", hasil)
hasil = x == y
print(x, "==", y, "=", hasil)

print("\n===== tidak sama dengan (!=) =====")
hasil = x != y
print(x, "!=", y, "=", hasil)
hasil = y != 82
print(y, "!=", 82, "=", hasil)

print("\n===== is =====")
a = x
b = y
c = a
hasil = a is c
print("a is c =", hasil)
hasil = a is b
print("a is b =", hasil)

print("\n===== is not =====")
hasil = a is not b
print("a is not b =", hasil)
hasil = a is not c
print("a is not c =", hasil)
