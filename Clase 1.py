#Primero creamos la clase
class Persona:
    #2. Definición de atributos
    def __init__(self,nombre,edad,altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
    #4. Definir métodos
    def Hablar(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad}, soy tan alta que mido {self.altura}") 

#3. Creación de objeto
p1= Persona("Luisa",21,1.62)
print(p1.nombre)
print(p1.edad)
print(p1.Hablar())


  