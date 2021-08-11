class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

Persona.nombre = 'Alexs'
Persona.edad = 24

print(Persona.nombre)