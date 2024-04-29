
#& Familiarización con secuencias
# 1. Crear una lista con los números del 1 al 10. Acceder con el índice a la posición que contiene el número 5, e imprimirlo por pantalla. Recordar que el índice de las listas empiezan con 0.

numeros=[
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10
]
numero_elegido=numeros.index(5)
print(numero_elegido)
# 2. Con la lista del punto anterior, usar la función len() para averiguar su longitud, e imprimirla.
longitud_lista=len(numeros)
print(longitud_lista)
# 3. Crear una secuencia con números distintos, y luego devolver el elemento máximo y el mínimo.
def minimoYmaximo():
    minimo=min(secuencia)
    maximo=max(secuencia)
    print("el valor mínimo es: ",minimo," y el valor máximo es: ",maximo)
secuencia = [75, 18, 12, 20, 2, 30]
minimoYmaximo()

#* sin usar min y max
# def ordenado():
#     secuencia.sort()
#     print(secuencia)

# def minimoYmaximo():
#     secuencia.sort()
#     minimo=secuencia[0]
#     secuencia.sort(reverse=True)
#     maximo=secuencia[0]
#     print("el valor mínimo es: ",minimo," y el valor máximo es: ",maximo)

# 4. Ordenar la secuencia del ejercicio anterior, e imprimirla por pantalla. (ver funciones de listas)
def ordenado():
     secuencia.sort()
     print(secuencia)

ordenado()

# 5. Crear una tupla que guarde tu nombre y tu edad. Luego, imprimir por pantalla tu edad, accediendo al elemento de la tupla que corresponda.

nombre_y_edad=(("Gisela",44))
nombre,edad=nombre_y_edad
print(edad)

""" 6. Hacer una lista con 5 nombres, y realizar las siguientes actividades con la misma: 
a. Cambiar el último elemento de la lista y cambiar el último nombre por “Juan”. Olvidándonos de
que sabemos que tiene 5 elementos, ¿Cómo podría saber cuál es el último elemento si no sé la
longitud?
b. Devolver el nombre que esté a dos posiciones del final. ¿Cómo hacemos para que nos funcione
para cualquier lista y no solo para la que tenga 5 elementos?
c. Recorrer la lista e imprimir cada nombre por pantalla.
d. Imprimir por pantalla la lista con 3 repeticiones, usar el operador repetición (*).
 """

nombres=["Pedro","Inés","Tomás","Helena","Agnes"]
def cambiar_nombre():
    for i, _ in enumerate(nombres):
        #debido a la función enumerate(). Cuando uso enumerate(), estoy iterando sobre una secuencia y necesito capturar tanto el índice como el valor en cada iteración
        if i == len(nombres) - 1:
            nombres[i] = "Juan"
            break

    print(nombres)

cambiar_nombre()     

# 7. Se pide ahora crear 3 tuplas como las del ejercicio 5, con un nombre y una edad. A continuación, guardarlas en una lista. Pensar, ¿De que nos servirá guardar las tuplas en una lista en vez de tenerlas por separado?

#&Ejercicios con listas y tuplas

""" 8. Se quiere guardar información de los siguientes países: Francia, Argentina, Japón, Alemania, Perú.
a. Crear una tupla para cada país que contenga su nombre, su capital y el continente donde se
encuentra.
b. Guardar las tuplas en una lista.

c. Hacer una función que reciba por parámetros la lista, e imprima la información de cada país
con el siguiente formato:

Por ejemplo:
País: Japón
Capital: Tokio
Continente: Asia
 """
francia=("Francia","París","Europa")
argentina=("Argentina","Capital Federal","America")
japon=("Japón","Tokio","Asia")
alemania=("Alemania","Berlín","Europa")
paises= [francia,argentina,japon,alemania]

def lista_paises(paises):
    for pais in paises:
        pa,cap,cont=pais

        print("\n","País: ",pa,"\n","Capital: ",cap,"\n","Continente: ",cont)
lista_paises(paises)
#& Secuencias, tuplas y listas GUIA DE EJERCICIOS Nº 4 PARTE 1
# 9. Una librería tiene un sistema que guarda los nombres de todos los libros que tienen en una lista de la siguiente forma: [“El principito”, “It”, “Sherlock Holmes”...]. 
#Se quiere saber cuántos libros repetidos tienen. Hacer código que imprima para cada título, cuántos ejemplares hay. Aclaración: No se sabe la cantidad de elementos que tiene la lista, la lista nombrada es solo un ejemplo.

nombres_libros = [
    "Cien años de soledad",
    "El alquimista",
    "El código Da Vinci",
    "Orgullo y prejuicio",
    "Harry Potter y la piedra filosofal",
    "Don Quijote de la Mancha",
    "1984",
    "Harry Potter y la piedra filosofal",
    "Matar a un ruiseñor",
    "El señor de los anillos: La comunidad del anillo",
    "El gran Gatsby",
    "Harry Potter y la piedra filosofal",
    "Harry Potter y el cáliz de fuego",
    "El nombre del viento",
    "El señor de los anillos: La comunidad del anillo",
    "Los juegos del hambre",
    "Crimen y castigo",
    "Harry Potter y el cáliz de fuego",
    "Las aventuras de Sherlock Holmes",
    "El señor de los anillos: La comunidad del anillo"
]
def libro_repetido():
    listado_libros={}
    for  libro in nombres_libros:
        if libro not in listado_libros:
            listado_libros[libro]=1
        else:
            listado_libros[libro] +=1
    for libro, ejemplares in listado_libros.items():
            print("Libro:",libro," - Ejemplares:", ejemplares)     
      
libro_repetido()     

# 10. Crear una lista que contenga los números del 1 al 10, luego recorrerla y guardar en otra lista esos números elevados al cuadrado.
def cuadrado(numero):
    return numero*numero

uno_al_diez=[1,2,3,4,5,6,7,8,9,10]
def cuadrado_del_numero():
    al_cuadrado = list(map(cuadrado, uno_al_diez))
    print(al_cuadrado)
cuadrado_del_numero()    

# 11. Se tiene la siguiente lista de palabras: [“entender”, “pueden”, “humanos”, “los”, “que”, “código”, “escriben”, ”programadores”, “buenos”, “Los”, “entiende.”, “computadora”, “una”, “que”, “código”, “escribe”, “tonto”, “Cualquier”]. 
#Hacer una función que reciba una lista, y devuelva un string uniendo las palabras desde el final de la lista hasta el principio con un “ ” (espacio) entre cada una, para formar la frase. (ver funciones de listas y strings).
palabras = ["entender", "pueden", "humanos", "los", "que", "código", "escriben", "programadores", "buenos", "Los", "entiende.", "computadora", "una", "que", "código", "escribe", "tonto", "Cualquier"]
palabras.reverse()
def concatenador(palabras):
    frase=" ".join(palabras)
    print(frase)
concatenador(palabras)

# 12. Se quiere hacer un sistema en la facultad para que un alumno pueda ir guardando las materias que va haciendo. Para eso, crear una función que le pregunte al usuario la materia que quiere almacenar, e ir guardando la información en una lista hasta que ingrese una ‘X’. ¿Qué funciones de listas no permiten insertar en una lista? (insert y append)

def guardar_materia():
    lista_materias=[]
    pregunta=input("Qué materia aprobaste?: ")
    while pregunta != "X" and pregunta !="x":
        lista_materias.append(pregunta)
        pregunta=input("Qué materia aprobaste?: ")
    print(lista_materias)
guardar_materia()
""" 13. Se tiene un ticket de supermercado que se puede representar como una lista de tuplas (producto, precio).
a. Hacer una función que reciba la lista, calcule y devuelva el total que hay que pagar.
b. Ahora se tienen dos tickets. Juntar ambos y volver a calcular el total.
Un ejemplo de lista puede ser: [(“Detergente”, 123), (“Jabón Líquido”, 456)] y nos tendría que devolver 579.(No copien y peguen la lista de la guía, porque hay caracteres que no los va a reconocer el editor
de texto)

 """

def ticket(lista_productos,lista_productos2):
    total=0
    for producto, precio in lista_productos2:
            lista_productos.append((producto,precio))

    for _,precio in lista_productos:
        total+=precio
    print("Monto total:", total) 

lista_productos = [
    ("Manzanas", 2000.50),
    ("Leche", 1000.20),
    ("Pan", 800.80),
    ("Huevos", 3000.50),
    ("Arroz", 1000.00)
]
lista_productos2 = [
    ("Papel higiénico", 1500.75),
    ("Queso", 2500.30),
    ("Galletas", 1200.50),
    ("Jabón", 800.20),
    ("Aceite de oliva", 1800.00)
]
ticket(lista_productos, lista_productos2)
