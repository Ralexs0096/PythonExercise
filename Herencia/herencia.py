class Persona:
    def __init__(self, nombre, edad, apellido):
        self.name = nombre
        self.age = edad
        self.last_name = apellido
        
    def __str__(self):
        return "Nombre: " + self.name + ", edad: " + str(self.age)
        
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre,edad)
        self.salary = sueldo
        
    def __str__(self):
        return super().__str__() + ", Sueldo: "+ str(self.salary)
persona = Persona('Alexs',24)
print(persona)