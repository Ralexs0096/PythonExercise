class Persona:
    def __init__ (self, name, lastname):
        self.nombre = name
        self.apellido = lastname

jefe = Persona('Alexs','Ruiz')
print('Mi nombre es {} {}'.format(jefe.nombre, jefe.apellido))