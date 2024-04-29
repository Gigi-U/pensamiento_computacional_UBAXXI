
#& Recursos con Strings
# 1. Hacer una función que reciba un string y que imprima solamente los caracteres que sean vocales.
def solo_vocales(palabra):
    vocales_de_palabra=[]
    for vocal in palabra:
        if vocal=="a" or vocal =="e" or vocal=="i" or vocal=="o" or vocal=="u":
        # otra forma
        # if vocal in "aeiouAEIOU":
            vocales_de_palabra.append(vocal)
    frase="".join(vocales_de_palabra)
    print(frase)
solo_vocales("hombre")    
# 2. Hacer una función que reciba un string y que lo invierta.
def invertir_string(string):
    string=string[::-1]
    return string
mi_string=invertir_string("gisela")    
print(mi_string)

""" 3. Hacer una función que reciba dos strings, un string y un substring, es decir, que el primero contiene al segundo, se pide devolver el string habiendo eliminado el substring del mismo.
Ejemplo: 
string: “Campeones del Mundo - 2022”  substring: “2022”
Una vez llamada a la función el string nos debería quedar “Campeones del Mundo - ”, notar que solo
borra el año, el espacio no. """
def borrar_parte_de_string(string,substring):
    return string.replace(substring, "")

string ="Campeones del Mundo - 2022"
substring=string[21:]
nuevo_string=borrar_parte_de_string(string, substring)
print(nuevo_string)


#* otra forma creando una funcion substring que lea de atras para adelante y tome la ultima palabra solamente
def borrar_parte_de_string(string,substring):
    return string.replace(substring, "")
string ="Campeones del Mundo (opcion2) - 2022"
# acá creamos el substring de forma diferente, ya que en vez de contar de 0 en adelante lo que hace es ir al final de la fila y va a guardarse todos los caracteres o numeros que vayan juntos, hasta llegar al primer espacio.
frase_invertida = string[::-1]
indice_espacio = frase_invertida.find(" ")
substring = frase_invertida[:indice_espacio][::-1]

nuevo_string=borrar_parte_de_string(string, substring)
print(nuevo_string)

#& Recursos con listas
#Para todos estos ejercicios se recomienda fuertemente tener a mano la documentación de los métodos de listas.

""" 4. Un chef está armando una lista de supermercado con todos los ingredientes que hay que comprar. Sólo quiere agregar un ingrediente a la lista si no lo escribió antes, así no tiene repetidos.
Hacer un programa que inserte un nuevo elemento en una lista de strings, solamente si el elemento que se desea insertar no se encuentra en la lista. La lista de ingredientes la podemos pensar como una
lista de strings.
Ejemplo:
ingredientes: [“tomate”, “queso”, “cebolla”, “huevo”]
ingrediente a agregar: “orégano”
La lista de ingredientes debería quedar [“tomate”, “queso”, “cebolla”, “huevo”, “orégano”]
En cambio, si el ingrediente a agregar es “queso” la lista debería quedar igual. """

ingredientes= ["tomate", "queso", "cebolla", "huevo"]
def lista_ingredientes(ingrediente):
    if ingrediente not in ingredientes:
        ingredientes.append(ingrediente)
    print(ingredientes)
lista_ingredientes("oregano")    
# 5. Agustina está jugando a las cartas con sus amigos. A ella le gusta tener las cartas de su mano bien ordenadas. Esto significa que cada vez que tiene que agarrar una nueva carta, la quiere agregar a su mano en el lugar indicado para no romper el orden. Si se tiene una lista de enteros ordenadas de mayor a menor. Hacer una función que según esta lista inserte un nuevo entero, manteniendo el orden.

#& Recursos con listas GUIA DE EJERCICIOS Nº 4 PARTE 2
""" Podemos pensar la lista de cartas como números enteros.
Ejemplo:
cartas: [1, 4, 6, 8]
carta nueva: 5
La lista de cartas debería quedar: [1, 4, 5, 6, 8]
Tratar de pensar una solución sin usar el método sort. (no es obligatorio). """
cartas= [1, 4, 6, 8]
def ordenar_sin_sort(carta):
    cartas.insert(2,carta)
    print(cartas)
ordenar_sin_sort(5)
# 6. Santiago armó una lista con el pedido de empanadas de su familia pero ahora quiere saber la cantidad de gustos diferentes que tiene que pedir. Podemos pensar la lista de empanadas como una lista de strings, entonces deberíamos devolver la cantidad de strings diferentes que hay en una lista.
empanadas=["carne","carne","jamón y queso","humita","humita","humita","verdura","verdura","pollo","carne","carne","pollo","pollo"]

def pedido_empanadas():
    listado_empanadas={}
    for empanada in empanadas:
        if empanada not in listado_empanadas:
            listado_empanadas[empanada]=1
        else:
            listado_empanadas[empanada]+=1
    for empanada, cantidad in listado_empanadas.items():
        print("Empanadas de ",empanada, ":",cantidad)

pedido_empanadas()

# 7. Manuel y su pareja armaron una lista numerada con las actividades de mantenimiento de la casa.Decidieron dividirse las tareas, a Manuel le tocó hacer todas las actividades con número par, por eso necesitamos hacer una función que reciba una lista de enteros, y devuelva otra lista que solamente contenga números pares, que vienen a ser las tareas de Manuel.

lista_numerada=[1,2,3,4,5,6,7,8,9,10]
def guardar_pares():
    lista_manuel=[]
    for tarea in lista_numerada:
        if tarea%2==0:
            lista_manuel.append(tarea)
    print("tareas de manuel: ",str(lista_manuel))
guardar_pares()

#* otra forma de hacer lo mismo: 
print("---------VERSION SIMPLIFICADA-----------")

def guardar_pares(lista):
    return [tarea for tarea in lista if tarea % 2 == 0]

print("Tareas de Manuel:", guardar_pares(lista_numerada))

#* otra forma con map: 
print("---------CON MAP-----------")

def es_par(numero):
    return numero % 2 == 0

def guardar_pares(lista):
    return list(filter(es_par, lista))

print("Tareas de Manuel:", guardar_pares(lista_numerada))
#&Recursos con Tuplas
""" 8. Un matrimonio está organizando una fiesta y tiene que armar una lista de invitados. Cada uno tiene su propia tupla y guarda en ella a todos los que quiere invitar.

Si alguien cancela tienen que sacarlo de la tupla.
Hacer una función que reciba la tupla y un nombre, y devuelva una nueva tupla sin el nombre pasado por parámetro.
Las tuplas son inmutables, entonces ¿Cómo podemos hacer para “eliminar” un elemento de una tupla? Recordemos que las tuplas tienen definido el operador +, pero no el operador -. """


invitados_novio = ("Juan Perez", "María López", "Pedro González", "Ana Martínez", "Luisa García", "Carlos Fernandez", "Laura Ramirez", "Miguel Diaz", "Sofía Alvarez", "Pablo Rodriguez")
invitados_novia = ("Luis Fernandez", "Elena Gomez", "Andrea Torres", "Javier Sanchez", "Isabel Navarro", "Diego Romero", "Carmen Serrano", "Roberto Ruiz", "Paula Jimenez", "José Martin")

def quitar_invitado(tupla, nombre):
    nueva_tupla = ()
    for invitado in tupla: # invitado es el elemento que ya estaba en la lista
        if invitado != nombre: # nombre es el nombre del invitado que quiero quitar
            nueva_tupla += (invitado,)
    return nueva_tupla

invitados_novia=quitar_invitado(invitados_novia, "Elena Gomez")
invitados_novio=quitar_invitado(invitados_novio, "Juan Perez")
# 9. Cuando ya tienen a todos los invitados tienen que juntar sus tuplas, para eso se necesita una función que a partir de dos tuplas cree una sola que sea la combinación de ambas tuplas.
print("--------tupla general: ")
def tupla_general(tupla1,tupla2):
    nueva_tupla=()
    nueva_tupla+=(tupla1)
    nueva_tupla+=(tupla2)
    print(nueva_tupla)
tupla_general(invitados_novio, invitados_novia)
