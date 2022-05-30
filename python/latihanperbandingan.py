# membuat gabungan area dari rentang angka

#++++3--------10+++++
inputUser = float(input("Masukan nilai yang kurang dari 3 dan lebih dari 10 ="))

# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print( "Kurang dari 3 =", isKurangDari)

# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print ("Lebih dari 10 =", isLebihDari)

# membandingan dengan operator logika
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukan =", isCorrect)

#----3+++++++10------
print("============")
inputUser = float(input("Masukan nilai yang lebih dari 3 dan kurang dari 10 ="))

# Memeriksa angka lebih dasri 3
isLebihDari = (inputUser > 3)
print ("Lebih dari 3 =", isLebihDari)

isKurangDari = (inputUser < 10)
print ("Kurang dari 10 =", isKurangDari)

# membandingkan dengan operator logika
isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukan =", isCorrect)

#---0+++++5-----8++++11----
print("=============")
inputUser = float(input("Masukan Angka :"))

b = (inputUser > 0)
print("nilai b ;", b)
c = (inputUser < 5)
print("nilai c ;", c)
d = (inputUser > 8)
print("nilai d ;", d)
e = (inputUser < 11)
print("nilai e ;", e)

bc = b and c
print(bc)
de = d and e
print(de)

x = bc or de
print(x)


#+++0-----5+++++8----11+++++
print("===========")
inputUser = float(input("Masukan Angka :"))

b = (inputUser < 0)
print("nilai b ;", b)
c = (inputUser > 5)
print("nilai c ;", c)
d = (inputUser < 8)
print("nilai d ;", d)
e = (inputUser > 11)
print("nilai e ;", e)

bc = b and c
print(bc)
de = d and e
print(de)

x = bc or de
print(x)
