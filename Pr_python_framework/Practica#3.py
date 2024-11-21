print("")
print("Alfaro_Ibarra_Sheccid_1171_3w_Practicando clases.")
print("")
class Persona:
    #Definir un método constructor que reciba el nombre, la edad y el dNi de la persona
    def __init__(self, nombre, edad, DNi):
        self.nombre = nombre
        self.edad = edad
        self.DNi = DNi
    
    def es_mayor_edad(self):
        return self.edad >= 18
    
    def es_menor_edad(self):
        return self.edad < 18

class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad
#Definir una funcion para mostrar la cuenta
    def mostrar(self):
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad}")
#Definir un método para depositar dinero
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
            print(f"Se han ingresado {cantidad}. Nuevo saldo: {self.cantidad}")
        else:
            print("La cantidad a ingresar debe ser mayor que cero.")
#Definr un método para retirar dinero
    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.cantidad:
                self.cantidad -= cantidad
                print(f"Se han retirado {cantidad}. Nuevo saldo: {self.cantidad}")
            else:
                print("No hay suficiente saldo para retirar esa cantidad.")
        else:
            print("La cantidad a retirar debe ser mayor que cero.")

class Cuenta_joven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0.05):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
    
    def titular_valido(self):
        return self.titular.es_mayor_edad() and self.titular.es_menor_edad()

    def mostrar(self):
        print(f"Cuenta joven de: {self.titular.nombre}")
        print(f"Bonificacion:{self.bonificacion*100:.2f}%")
        super().mostrar()
    
    #Datos

nombre= input("Pon tu nombre:")
edad = int(input("Pon tu edad:"))
dni= input("Pon tu DNI:")

persona= Persona(nombre, edad, dni)

#Es valido para ser una cuenta joven
if persona.es_mayor_edad() and persona.es_menor_edad():
    bonificacion=float(input("Introducir cantidad de bonificación:"))
    cuenta_joven = Cuenta_joven(persona, 0, bonificacion)
    cuenta_joven.mostrar()
    
    retiro=float(input("Cantidad deseada a retirar:"))
    cuenta_joven.retirar(retiro)
else:
    print("No puedes tener una cuenta joven")