palabra = str(input("escribe una palabra: "))
voc = "aeiou"
cont = 0

for letra in palabra:
    if letra in voc:
        cont = cont + 1


print(f"numero de vocales {cont}")


# numero = int(input("INTRODUCE UN NUMERO: "))

# for i in range (10):
#      print(f"{numero} x {i} = {numero  * i}")

