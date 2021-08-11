class Aritmetica:
    
    def __init__(self, operando1, operando2):
        self.op1 = operando1
        self.op2 = operando2
        
    def sumar(self):
        return self.op1 + self.op2

#Creamos un nuevo objeto
aritmetica = Aritmetica(2,2)

#Una Forma de acceder
print(Aritmetica.sumar(aritmetica))
#otra forma mas practica de acceder
print(aritmetica.sumar())