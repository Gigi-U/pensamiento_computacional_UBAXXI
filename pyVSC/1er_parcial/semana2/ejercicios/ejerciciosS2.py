
#& INGRESO DE DATOS----------------------------------------
print("-------EJERCICIO 1 👇")
""" Crear un programa que le solicite al usuario un entero y lo imprima por pantalla.
Recordá que podés usar las funciones input (para solicitar información) y print para mostrar
información. """

def entero():
  dime_numero_entero = int(input("Ingrese un número entero: "))
  return dime_numero_entero

numero_ingresado = entero()
print("El número es:", numero_ingresado)

#############################################################
print("-------EJERCICIO 2 👇")
""" Crear un programa que le solicite al usuario dos números enteros y luego imprima por pantalla:
● la suma de ambos números
● la resta de ambos números
● la multiplicación de ambos números
● la división entera de ambos números
● el resto """
def calculador():

  num1 = int(input("Ingrese un número entero: "))  
  num2 = int(input("Ingrese otro número entero: "))  
  suma = num1 + num2
  resta = num1 - num2
  multiplicacion = num1 * num2
  division = num1 / num2

  resto= num1%num2 
  
  print("La suma es:", suma)
  print("La resta es:", resta)
  print("La multiplicación es:", multiplicacion)
  print("La división es:", division)
  print("El resto es:", resto)

calculador()

#############################################################
print("-------EJERCICIO 3 👇")
#Crear un programa que le solicite al usuario un entero y determine si es par, mostrando por pantalla un mensaje que indique el resultado.

def parOImpar():
    numero=int(input("Ingresa un número entero: "))
    if numero%2==0:
        mensaje="es par"
        print(mensaje)
    else:
        mensaje="es inpar"
        print(mensaje)
parOImpar()

#############################################################
print("-------EJERCICIO 4 👇")
#Escribir un programa que le pida a un usuario su año de nacimiento y otro año, y le diga qué edad tenía el usuario en el año ingresado.
def tuEdad():
    año_de_nacimiento=int(input("ingresa tu año de nacimiento: "))  
    año_x=int(input("ingresa un año cualquiera - posterior al de tu nacimiento: "))  
    tu_edad_en_año_x= año_x-año_de_nacimiento
    print(tu_edad_en_año_x)
tuEdad()

#############################################################
print("-------EJERCICIO 5 👇")
#Crear un programa que le solicite al usuario 5 enteros y muestre por pantalla el promedio de ellos. Es muy común usar variables para acumular valores.
def promedio():
    nro1=int(input("ingresa un número : "))  
    nro2=int(input("ingresa 2do número : ")) 
    nro3=int(input("ingresa 3er número : "))  
    nro4=int(input("ingresa 4to número : "))  
    nro5=int(input("ingresa 5too número : "))  
    promedio= float((nro1+nro2+nro3+nro4+nro5)/5)
    print(promedio)
promedio()

#############################################################
print("-------EJERCICIO 6 👇")
#Crear una función que reciba un número y muestre el anterior y el siguiente.
def anteriorYSiguiente():
    numero =int(input("Ingresa un número : "))
    numero_anterior= numero-1
    numero_siguiente= numero+1
    return  numero, numero_anterior, numero_siguiente
numero, numero_anterior, numero_siguiente= anteriorYSiguiente()    
print("el numero anterior a "+ str(numero)+ " es: "+ str(numero_anterior) +" y el siguiente es: "+ str( numero_siguiente))

#############################################################
print("-------EJERCICIO 7 👇")
#Crear una función que una un string y un entero, ambos dentro de un string.
def stringCompuesto():
  palabra=input("ingresa una palabra : ")  
  entero=int(input("ingresa un número entero: "))
  stringCompuesto=palabra+" "+str(entero)
  print(stringCompuesto)
  print(type(stringCompuesto))
stringCompuesto()

#############################################################
print("-------EJERCICIO 8 👇")
#Crear una función que reciba un entero y que retorne (devuelva) el resto y el cociente.
def obtener_resto_y_cociente(dividendo, divisor):
    cociente = dividendo // divisor
    resto = dividendo % divisor
    return resto, cociente

dividendo = 10
divisor = 3
resto, cociente = obtener_resto_y_cociente(dividendo, divisor)
print("Resto: ", resto) 
print("Cociente: ", cociente)  

#CADENAS-----------------------------------------------------
#############################################################
print("-------EJERCICIO 9 👇")
#Pedirle nombre y apellido por separado e imprimir “Apellido, Nombre”. 
def nombreYApellido():
    apellido= input("ingresa tu apellido: ")
    nombre=input("Ingresa tu nombre: ")
    print(f"{apellido}, {nombre}")
nombreYApellido()

#############################################################
print("-------EJERCICIO 10 👇")
# Obtener una palabra e imprimir la cantidad de letras.
def contadorDeCaracteres():
  palabra=input("ingresa una palabra : ")  
  print(len(palabra))
contadorDeCaracteres()

#############################################################
print("-------EJERCICIO 11 👇")
# Obtener una palabra e imprimir los primeros 5 caracteres (pista: slicear la palabra).
def obtenerCincoPrimerosCaracteres():
  palabra=input("ingresa una palabra de más de 5 caracteres: ")
  palabra_cortada = palabra[:5:]
  print(palabra_cortada)
obtenerCincoPrimerosCaracteres()

#############################################################
print("-------EJERCICIO 12 👇")
# Obtener una palabra, borrarle todas las ‘a’ e imprimirla por pantalla (pista: usar una función predefinida de Python).

def borrarLasA():
  palabra=input("ingresa una palabra: ")
  palabra_sin_a = palabra.replace("a", "")
  print(palabra_sin_a)
borrarLasA()
