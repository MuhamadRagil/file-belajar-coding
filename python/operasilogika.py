# Operasi logika atau boolean
# NOT OR AND XOR

#NOT
print("====NOT====")
a = False
c = not a
print("data a =", a)
print("data c =", c)

#OR(Jika salah satu true maka akan true)
print("====OR====")
a = False
b = True
c = a or b
print(a, "OR", b, "=", c)

a = True
b = False
c = a or b
print(a, "OR", b, "=", c)

a = False
b = False
c = a or b
print(a, "OR", b, "=", c)

a = True
b = True
c = a or b
print(a, "OR", b, "=", c)

#AND(Jika keduanya true maka akan true)
print("====AND====")
a = False
b = True
c = a and b
print(a, "AND", b, "=", c)

a = True
b = False
c = a and b
print(a, "AND", b, "=", c)

a = False
b = False
c = a and b
print(a, "AND", b, "=", c)

a = True
b = True
c = a and b
print(a, "AND", b, "=", c)

#XOR(Jika keduanya true maka akan true)
print("====XOR====")
a = False
b = True
c = a ^ b
print(a, "XOR", b, "=", c)

a = True
b = False
c = a ^ b
print(a, "XOR", b, "=", c)

a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c)

a = True
b = True
c = a ^ b
print(a, "XOR", b, "=", c)
