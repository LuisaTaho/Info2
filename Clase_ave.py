#Creación de clase
class Animal:
    def __init__(self,especie,edad,sonido):
        self.especie=especie
        self.edad=edad
        self.sonido=sonido
    #Definir métodos
    def hablar(self):
        print(f"Soy un {self.especie} y yo hago{self.sonido}")
    def moverse(self):
        pass
    #Perro hereda de animal
class Perro(Animal): 
    def __init__(self,especie,edad,sonido,raza,tamaño):
        #Invocar clase padre
        Animal.__init__(self,especie,edad,sonido)
        self.raza=raza
        self.tamaño=tamaño
    def describe(self):
        print(f"Hola, soy un {self.especie}, tengo {self.edad} y hago {self.sonido}, soy de la raza {self.raza} y soy {self.tamaño}")

#Definir objetos
mi_perro =Perro('Perro',4,'Guau!','labrador', 'grande')

print(mi_perro.describe())
