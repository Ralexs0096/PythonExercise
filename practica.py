#Calculo del Inidce de Masa - IMC
# Formula: Peso KG / (altura * altura)
print('Calculemos el IMC de tu persona\n')

nombre = input('Como te llamas?\n')
peso_libras = int(input('Dame tu peso en libras\n'))
altura_metros = float(input('Dame tu altura en metros\n'))

peso_kg = peso_libras / 2.2

resulta_imc = peso_kg / (altura_metros * altura_metros)

print('Hola {}\nTu indice de masa corporal es: {}'.format(nombre,resulta_imc))
