#def = define
# los () incluiran los parámetros 
# los : estan avisando que terminó la "firma" de la función
# las funciones por si mismas no tienen ningun efecto en el programa. Siempre deben ser llamadas o invocadas.

# se carga el dato del nombre por parámetro 
def saludarParametro(nombre):

    saludo= "¡Hola"+ " "+ nombre+", ¿cómo estas?!"
    print(saludo)
    
saludarParametro("Carmela")
saludarParametro("Indi")
saludarParametro("Pepa")

# con input:
def saludarInput():

    tu_nombre=input("Ingresa tu nombre: ")

    saludo= "¡Hola"+ " "+ tu_nombre+"!"
    print(saludo)
    
saludarInput()


# Devolviendo valor para que se use después:
def sumarNumeros(numero1, numero2):
    suma=numero1+numero2
    return suma    

resultadoSuma= sumarNumeros(20,55)

# Usando la función anterior:
def multiplicarYLlamarOtraFuncion(numero3):
    multiplicacion= resultadoSuma * numero3
    return multiplicacion

resultadoMultiplicacion= multiplicarYLlamarOtraFuncion(5)
print(resultadoMultiplicacion)

# obtener 2 valores por separado:
def obtenerDosValores(numero1, numero2):
    suma = numero1+numero2
    resta = suma-5
    return suma, resta    

suma, resta= obtenerDosValores(20,55)  # estas variables son diferentes a las de la funcion
print(suma)
print(resta)