#calcular el peso del usuario en la luna.

#el peso se calcula en base a la gravedad del planeta
#la gravedad de la luna es de 6
#formula: peso en KG / 6
print('vamos a calcular su peso en la luna')
nombre =input('como te llamas?\n')
peso_kg=float(input('dame tu peso en kg\n'))

#calculo
resultado = peso_kg/6
print('mira {} tu peso en la luna es: {} '.format(nombre,resultado))