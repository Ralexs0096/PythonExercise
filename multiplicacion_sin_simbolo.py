#realizar multiplicacion sin operador de Multiplicacion
def multi_sin(a,b):
    resultado = 0
    for x in range(a):
        resultado = resultado + b
    print(resultado)

multi_sin(3,2)