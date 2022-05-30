# Operasi perbandingan
# setiap hasilnya adalah nilai boolean
# <,>,<=,>=,==,!=,is,is not

import yaml


a = 4
b = 2

# lebih dari >
print("====LEBIH DARI====")
hasil = a > b
print(a, '>', b, '=' ,hasil)
hasil = b > 3
print(b, '>', 3, '=' ,hasil)
hasil = b > 2
print(b, '>',2, '=' ,hasil)

# kurang dari <
print("====KURANG DARI====")
hasil = a < b
print(a, '<', b, '=' ,hasil)
hasil = b < 3
print(b, '<', 3, '=' ,hasil)
hasil = b < 2
print(b, '<',2, '=' ,hasil)

# kurang dari sama dengan <=
print("====KURANG DARI SAMA DENGAN====")
hasil = a <= b
print(a, '<=', b, '=' ,hasil)
hasil = b <= 3
print(b, '<=', 3, '=' ,hasil)
hasil = b <= 2
print(b, '<=',2, '=' ,hasil)

# lebih dari sama dengan >=
print("====LEBIH DARI SAMA DENGAN====")
hasil = a >= b
print(a, '>=', b, '=' ,hasil)
hasil = b >= 3
print(b, '>=', 3, '=' ,hasil)
hasil = b >= 2
print(b, '>=',2, '=' ,hasil)

# sama dengan ==
print("====SAMA DENGAN====")
hasil = a == b
print(a, '==', b, '=' ,hasil)
hasil = b == 3
print(b, '==', 3, '=' ,hasil)
hasil = b == 2
print(b, '==',2, '=' ,hasil)

# tidak sama dengan !=
print("====SAMA DENGAN====")
hasil = a != b
print(a, '!=', b, '=' ,hasil)
hasil = b != 3
print(b, '!=', 3, '=' ,hasil)
hasil = b != 2
print(b, '!=',2, '=' ,hasil)

# is sebagai komperasi object identity
print("===OBJECT IDENTITY IS====")
x = 5 # x is 5 (nilai 5 adalah literal)
y = 5
print("nilai x  =",x, "id =", hex(id(x)))
print("nilai y  =",y, "id =", hex(id(y)))
hasil = x is y
print("x is y =", hasil)

x = 5
y = 6
print("nilai x  =",x, "id =", hex(id(x)))
print("nilai y  =",y, "id =", hex(id(y)))
hasil = x is y
print("x is y =", hasil)

# is not sebagai komperasi object identity
print("===OBJECT IDENTITY IS NOT====")
x = 5 # x is 5 (nilai 5 adalah literal)
y = 5
print("nilai x  =",x, "id =", hex(id(x)))
print("nilai y  =",y, "id =", hex(id(y)))
hasil = x is not y
print("x is not y =", hasil)

x = 5
y = 6
print("nilai x  =",x, "id =", hex(id(x)))
print("nilai y  =",y, "id =", hex(id(y)))
hasil = x is not y
print("x is not y =", hasil)


