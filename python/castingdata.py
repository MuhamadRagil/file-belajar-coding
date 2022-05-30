#mengkonversi dari satu tipe data ke tipe data yang lain
#tipe data : int, str, float, bool

#tipe data integer
from sqlalchemy import true


print("====Integer====")
data_integer = 14
print("data =", data_integer, ", type =", type(data_integer))

data_string = str(data_integer)
data_float = float(data_integer)
data_bool = bool(data_integer)
print("data =", data_string, ", type =", type(data_string))
print("data =", data_float, ", type =", type(data_float))
print("data =", data_bool, ", type =", type(data_bool))

##tipe data string
print("====String====")
data_float = "ading"
print("data =", data_string, ", type =", type(data_string))

data_integer = int(data_string)
data_string = str(data_string)
data_bool = bool(data_string)
print("data =", data_string, ", type =", type(data_string))
print("data =", data_float, ", type =", type(data_float))
print("data =", data_bool, ", type =", type(data_bool))


##tipe data float
print("====Float====")
data_float = 18.5
print("data =", data_float, ", type =", type(data_float))

data_string = str(data_float)
data_integer = int(data_float)
data_bool = bool(data_float)
print("data =", data_string, ", type =", type(data_string))
print("data =", data_integer, ", type =", type(data_integer))
print("data =", data_bool, ", type =", type(data_bool))

