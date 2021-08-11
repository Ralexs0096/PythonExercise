numero = int(input('Escribe un numero\n'))

numero_string = str(numero)

vacio = []

for x in numero_string:
    vacio.append(int(x))


print(sorted(vacio))