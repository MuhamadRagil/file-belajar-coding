#data yang di ambil pasti str
data = input("masukan data :")

print("data =", data, "Type =", type(data))

#jika ingin mengambil data int dan float,maka bisa dengan casting
angka = int(input("masukan angka :"))
angka = float(input("masukan angka :"))

print("data =", angka, "Type =", type(angka))

#mengambil data boolean
biner = bool(int(input("masukan nilai :")))

print("data =", biner, "Type :", type(biner))