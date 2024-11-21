print("")
print("Alfaro_Ibarra_Sheccid_1171_3w_Practicando clases.")
print("")
#Definir una clase que se llame Persona
class Persona:
    #Definir un método constructor que reciba el nombre, la edad y el dNi de la persona
    def __init__(self, nombre, edad, DNi):
        self.nombre = nombre
        self.edad = edad
        self.DNi = DNi
    #Definir un método que muestre la información de la persona
    def Imprimir(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.DNi}")
    #Definir un método que muestre si la persona es mayor de edad o no
    def resultados(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad")
        else:
            print(f"{self.nombre} es menor de edad")

#Crear un objeto de la clase Persona
persona= Persona(input("Pon tu nombre: "), int(input("Pon tu edad: ")), int(input("Pon tu DNI: ")))
persona.Imprimir()
persona.resultados()
