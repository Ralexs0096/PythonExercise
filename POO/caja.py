"""Ejercicio calcular el volumen de una caja"""
class Caja:
    
    def __init__(self, alto, ancho, largo):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo

    def calcular_volumen(self):
        return self.alto * self. ancho * self.largo

alto = int(input('Introduce el valor del alto de la caja: \n'))
ancho = int(input('Introduce el valor del ancho de la caja: \n'))
largo = int(input('Introduce el valor del largo de la caja: \n'))

#Asignamos los valores del usuario al objeto caja
caja = Caja(alto, largo, ancho)

#retornamos el area de la caja desde el objeto caja y su metodo
print('el area de la caja es: {}'.format(caja.calcular_volumen()))