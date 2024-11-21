print("")
print("Alfaro_Ibarra_Sheccid_1171_3w_Practicando funciones.")
print("")
#Definir una función con su argumento
def pal(palabra):
    #si la palabra es igual a la palabra al reves, es palindromo
    return palabra == palabra[::-1]
#Preguntar al usuario si quiere ingresar una palabra
pl=input("Pon una palabra: ")
#utilizar if para saber si la palabra es palindromo o no
if pal (pl):
    print("La palabra es palindromo")
else:
    print("La palabra no es palindromo")