a = 14
b = 18

#operator prtambahan +
hasil = a + b
print(a, '+' ,b, '=', hasil)

#operator pengurangan -
hasil = a - b
print(a, '-' ,b, '=', hasil)

#operator perkalian *
hasil = a * b
print(a, '*' ,b, '=', hasil)

#operator pemagian /
hasil = a / b
print(a, '/' ,b, '=', hasil)

#operator eksponen (pangkat) **
hasil = a ** b
print(a, '**' ,b, '=', hasil)

#operator modulus (sisa bagi) %
hasil = a % b
print(a, '%' ,b, '=', hasil)

#operator floor division (dibulatkan) //
hasil = a // b
print(a, '//' ,b, '=', hasil)


##Prioritas Operasi
'''
    1.()
    2.eksponen **
    3.perkalian dkk *  / ** % //
    4.pertambahan dan pengurangan
'''
x = 4
y = 6
z = 7

hasil = x * y + z ** x // y / z - x
print (x, '*', y ,'+', z ,'**', x ,'//', y , '/', z , '-', x, '=',hasil)




