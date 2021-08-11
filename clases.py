class Persona:
    
    def __init__(self, nombre, apellido, edad, sexo):
        self.name = nombre
        self.last = apellido
        self.age = edad
        self.sex = sexo
        
    def datos(self):
        return "Eres "+ self.name, self.last, self.age, self.sex
    
mi_persona1 = Persona('Alexs','Ruiz',24,'masculino')
print(mi_persona1.datos())