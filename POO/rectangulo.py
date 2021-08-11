"""Calcular el area de un rectangulo - ejercicio"""
class Rectangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        #retorna el area
        return self.base * self.altura

print('Vamos a calcular el area de un Rectangulo.')
base = int(input('Introduce el valor de la base del rectangulo: \n'))
altura = int(input('Introduce el valor de la altura del rectangulo: \n'))

rectangulo = Rectangulo(base, altura)

print('El area del rectangulo es: {}'.format(rectangulo.calcular_area()))