""" 1. En una escuela se quiere tener un sistema para guardar la información de sus estudiantes para tener mejor organizado sus datos.
a. Crear un diccionario que sirve para representar a una persona en este contexto, pensar en las
características que se consideren más relevantes para identificar a una persona (su nombre,
DNI, edad, etc).
b. Agregar al diccionario creado, un campo que sea otro diccionario y sirva para guardar el curso
del estudiante y sus características (año, división, orientación, etc).
c. Teniendo una lista de diccionarios de estudiantes, buscar en la lista la persona con mayor edad
e imprimirla por pantalla. """
estudiante1={
    "id": 1,
    "nombre": "Esteban Alonzo",
    "dni": "31.444.890",
    "edad": 33
}
estudiante2={
    "id": 2,
    "nombre": "María López",
    "dni": "28.555.678",
    "edad": 25
}
estudiante3={
    "id": 3,
    "nombre": "Juan Pérez",
    "dni": "30.666.789",
    "edad": 28
}
estudiante4={
    "id": 4,
    "nombre": "Carmela Urriza",
    "dni": "35.656.789",
    "edad": 50
}
estudiante5={
    "id": 5,
    "nombre":"Cosme Fulanito",
     "dni": "35.656.789", 
     "edad":70
}

print("\n----creando lista:----")
estudiantes = [estudiante1,estudiante2,estudiante3,estudiante4]
print(estudiantes)

# agregando estudiante con append - Extra
print("\n----agregando estudiante con append - Extra----")
estudiantes.append(estudiante5)
print(estudiantes)
# b) agregando diccionario a diccionarios:
print("\n----agregando diccionario a diccionarios:----")
def agregar_diccionarios(estudiante):
    estudiante["curso"]={
        "id": 90,
            "año": 2024,
            "día_cursada": "viernes",
            "profesor": "Ernesto Flores"
    }
agregar_datos_curso =list(map(agregar_diccionarios,estudiantes))    
print(estudiantes)

# c) buscar estudiante mayor
print("\n----buscar estudiante mayor----")

def obtener_edad(estudiante):
    return estudiante["edad"]
estudiante_mayor_edad = max(estudiantes, key=obtener_edad)
print(estudiante_mayor_edad)

""" 2. En un vivero se guardan las plantas en una lista de diccionario con la siguiente información: especie, si necesita luz solar o no, y el precio. (OBSERVACIÓN: ¿Qué tipo de dato nos permitía guardar si algo es verdad o no?). 
Ahora se necesita un sistema que guarde las plantas a medida que van llegando. Se pide hacer una función que reciba la lista de diccionarios de plantas, y los datos de la planta nueva y agregue esa planta a la lista de diccionarios. """

planta1 = {
    "especie": "Cactus",
    "necesita_luz_solar": True,
    "precio": 10.99
}
planta2 = {
    "especie": "Rosa",
    "necesita_luz_solar": True,
    "precio": 15.50
}

planta3 = {
    "especie": "Helecho",
    "necesita_luz_solar": False,
    "precio": 8.75
}

plantas=[planta1,planta2,planta3]
print("---lista de plantas---")
print(plantas)
print("---función Agregar Planta---")
def agregar_planta(planta):
    plantas.append(planta)
    print(plantas)
agregar_planta({"especie": "Suculenta","necesita_luz_solar": True,"precio": 12.25})  

""" 3. Se representa un ticket de supermercado como una lista de diccionarios, donde cada diccionario tiene la siguiente información:
● Nombre del producto
● Precio por unidad
● Cantidad
Se pide hacer una función que reciba el ticket y devuelva el monto total a pagar.
 """
ticket_supermercado = [
    {"Nombre del producto": "Leche", "Precio por unidad": 2.5, "Cantidad": 1},
    {"Nombre del producto": "Pan", "Precio por unidad": 1.0, "Cantidad": 2},
    {"Nombre del producto": "Huevos", "Precio por unidad": 3.75, "Cantidad": 1},
    {"Nombre del producto": "Manzanas", "Precio por unidad": 2.0, "Cantidad": 3},
    {"Nombre del producto": "Arroz", "Precio por unidad": 1.5, "Cantidad": 2}
]

def monto_total(ticket):
    monto=0.0
    for producto in ticket:
        valor = producto["Precio por unidad"] * producto["Cantidad"]
        monto+= valor  
    print(monto)
print("-------monto total a pagar---------")    
monto_total(ticket_supermercado)

""" 4. Sol tiene una lista de diccionarios donde guarda todas las películas que vió. 
La información que tiene para cada una es: el nombre de la serie, año en que salió, y la puntuación que le puso del 1 al 10. 
Hace mucho que quiere que Tomás empiece a ver las películas que ella considera que son las mejores que vio.
Hacer una función que reciba el diccionario de las películas que vió Sol, y que devuelva una nueva lista de diccionarios donde sólo estén las películas que tienen puntaje mayor a 7.
 """
# Lista de diccionarios de películas
peliculas_de_sol = [
    {"nombre": "Titanic", "año": 1997, "puntuación": 6},
    {"nombre": "El Padrino", "año": 1972, "puntuación": 9},
    {"nombre": "La Lista de Schindler", "año": 1993, "puntuación": 10},
    {"nombre": "Forrest Gump", "año": 1994, "puntuación": 7},
    {"nombre": "El Señor de los Anillos: El Retorno del Rey", "año": 2003, "puntuación": 9},
    {"nombre": "Pulp Fiction", "año": 1994, "puntuación": 8},
    {"nombre": "El Caballero de la Noche", "año": 2008, "puntuación": 6},
    {"nombre": "Matrix", "año": 1999, "puntuación": 8},
    {"nombre": "Cadena Perpetua", "año": 1994, "puntuación": 5},
    {"nombre": "Gladiador", "año": 2000, "puntuación": 8}
]
def peliculas_de_tomas(peliculas):
    lista_peliculas=[]
    for pelicula in peliculas:
        if pelicula["puntuación"] >7:
             lista_peliculas.append(pelicula)
    # otra forma: 
    #lista_peliculas = [pelicula for pelicula in peliculas if pelicula["puntuación"] > 7]         
    print(lista_peliculas)         
peliculas_de_tomas(peliculas_de_sol)
""" 5. Un profesor guarda las notas del primer parcial de sus alumnos en una lista de diccionarios que guarda la siguiente información:
● Nombre
● Apellido
● Intento
● Nota
Donde ”intento” es la instancia que está rindiendo, 1 si es la primera vez que rinde el parcial, 2 si es el primer recuperatorio y 3 si es el segundo recuperatorio.
Se pide hacer una función que, dado esta lista de diccionarios, devuelva el promedio de las notas en la primera oportunidad que rindieron los alumnos.
¿Cómo harían para generalizar la función y que el intento sea parametrizable? Es decir, que no
solamente sirve para el intento 1, sino que también pueda servir para los demás.
2
"""       
alumnos_primer_parcial = [
    {"Nombre": "Juan", "Apellido": "Gómez", "Intento": 1, "Nota": 8.5},
    {"Nombre": "María", "Apellido": "López", "Intento": 2, "Nota": 10.0},
    {"Nombre": "Pedro", "Apellido": "Martínez", "Intento": 1, "Nota": 9.2},
    {"Nombre": "Ana", "Apellido": "Rodríguez", "Intento": 3, "Nota": 6.9},
    {"Nombre": "Luis", "Apellido": "González", "Intento": 2, "Nota": 8.0}
]
print("-----promedio para intento 1)")
def promedio(alumnos):
    sumar_notas=0.0
    contador=0
    for alumno in alumnos:
        if alumno["Intento"]==1:
            contador += 1
            sumar_notas+=alumno["Nota"]
    print(sumar_notas/contador) 
promedio(alumnos_primer_parcial) 

print("-----promedio para cualquier intento)")
def promedio_parametrizable(alumnos, intento):
    sumar_notas=0.0
    contador=0
    for alumno in alumnos:
        if alumno["Intento"]==intento:
            contador += 1
            sumar_notas+=alumno["Nota"]
    print(sumar_notas/contador) 
promedio_parametrizable(alumnos_primer_parcial, 3)  

""" 6. En una fábrica, se hace un chequeo de calidad a los productos antes de cada entrega. El resultado del chequeo de la entrega se guarda en una lista de diccionarios, donde cada diccionario tiene la siguiente información de cada producto:
● Código del producto
● Fecha de vencimiento
● Si pasó el chequeo de calidad o no.

 Se pide hacer una función que reciba esta lista de diccionarios y elimine todos los productos que no pasaron el chequeo de calidad. 
 Devolver en una tupla el diccionario con los elementos eliminados y la cantidad de elementos que quedaron en el diccionario.
Dado que la tupla es inmutable y nosotros no podemos ir agregando elementos a una tupla, ¿En qué
momento deberíamos crear la tupla?
 """
productos_fabrica = [
    {"Código del producto": "001", "Fecha de vencimiento": "2024-06-30", "Chequeo de calidad": True},
    {"Código del producto": "002", "Fecha de vencimiento": "2024-07-15", "Chequeo de calidad": False},
    {"Código del producto": "003", "Fecha de vencimiento": "2024-08-20", "Chequeo de calidad": True},
    {"Código del producto": "004", "Fecha de vencimiento": "2024-09-10", "Chequeo de calidad": True},
    {"Código del producto": "005", "Fecha de vencimiento": "2024-10-05", "Chequeo de calidad": False}
]
def pasa_chequeo(listado):
    elementos_eliminados=()
    contador=0
    for elemento in listado:
        if elemento["Chequeo de calidad"] == False:
            contador+=1
            elementos_eliminados+=(elemento,)
    print("Los elementos que no pasaron la prueba de calidad son en total",contador," . | Detalle de elementos eliminados: ",elementos_eliminados)
pasa_chequeo(productos_fabrica)    

""" 7. Se quiere guardar la información de un grupo de maratonistas. 
Se necesita guardar su nombre, DNI, y todas las maratones que corrió, de la cual a su vez se quiere tener el nombre de cada una, el año, el puesto en que salió el maratonista, y el tiempo que tardó en terminarla.
a. Crear el diccionario que represente esta situación.
AYUDA: Queremos guardar muchos maratonistas, y a su vez, muchas maratones para cada maratonista, entonces ¿Qué tipo de dato debería ser el campo que guarda todas las maratones? ¿Y qué tipo de dato es la maratón en sí?
b. Teniendo una lista de diccionarios de maratonistas, ordenarlos alfabéticamente.
c. Ordenar las maratones de cada maratonista según el tiempo que tardó en completar cada una
de forma ascendente.
 """
listado_maratonistas = [
    {
        "nombre": "María",
        "dni": "87654321",
        "maratones": [
            {"nombre_maraton": "Maratón de Berlín", "año": 2020, "puesto": 3, "tiempo_minutos": 195},
            {"nombre_maraton": "Maratón de Chicago", "año": 2019, "puesto": 7, "tiempo_minutos": 205}
        ]
    },
    {
    "nombre": "Zenon",
    "dni": "98765432",
    "maratones": [
        {"nombre_maraton": "Maratón de Berlín", "año": 2023, "puesto": 3, "tiempo_minutos": 195},
        {"nombre_maraton": "Maratón de Chicago", "año": 2022, "puesto": 7, "tiempo_minutos": 205}
        ]
    },
    {
        "nombre": "Pedro",
        "dni": "45678912",
        "maratones": [
            {"nombre_maraton": "Maratón de Londres", "año": 2023, "puesto": 8, "tiempo_minutos": 220},
            {"nombre_maraton": "Maratón de Boston", "año": 2022, "puesto": 12, "tiempo_minutos": 230}
        ]
    },
    {
        "nombre": "Juan",
        "dni": "12345678",
        "maratones": [
            {"nombre_maraton": "Maratón de Buenos Aires", "año": 2022, "puesto": 5, "tiempo_minutos": 180},
            {"nombre_maraton": "Maratón de Nueva York", "año": 2021, "puesto": 10, "tiempo_minutos": 210}
        ]
    },
]
# necesito que entre al listado, recorra los diccionarios y tome los nombres, y una vez que hizo eso los ordene por orden de a a z
#luego necesito poder ir llamando esa lista ordenada para imprimirla

print("---------nombres ordenados----------")
#version de codigo acotada: nombres = [maratonista["nombre"] for maratonista in listado_maratonistas] nombres.sort() 

nombres=[]
for maratonista in listado_maratonistas:
    nombres.append(maratonista["nombre"])
nombres.sort() 

def imprimir_en_orden():
    for nombre in nombres:
        for maratonista in listado_maratonistas:
            if nombre == maratonista["nombre"]:
                print(maratonista)                
imprimir_en_orden()

