print("")
print("Alfaro_Ibarra_Sheccid_1171_3w_Practicando clases.")
print("")
#Definir una clase con el nombre cuenta
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


# Solicitar el nombre del titular y la cantidad inicial
nombre_titular = input("Ingresar nombre del titular: ")
cantidad_inicial = float(input("Ingresar cantidad inicial: "))

# Crear la cuenta
cuenta1 = Cuenta(nombre_titular, cantidad_inicial)

# Mostrar la cuenta
cuenta1.mostrar()

# Solicitar la cantidad a ingresar
cantidad_a_ingresar = float(input("Ingresar cantidad a ingresar: "))
cuenta1.ingresar(cantidad_a_ingresar)

# Puedes agregar más interacciones, como retirar dinero
cantidad_a_retirar = float(input("Ingresar cantidad a retirar: "))
cuenta1.retirar(cantidad_a_retirar)
