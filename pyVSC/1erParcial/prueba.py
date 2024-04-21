def transformar(persona):
    return persona[0][0] + str(persona[1])

lista_personas=[("tomas", 75),("Gisela",18),("Carmela",67)]
filtrada= list(map(transformar, lista_personas))
print(filtrada)


""" Este código en Python realiza lo siguiente:

Define una función llamada transformar que toma un argumento llamado persona.
Dentro de la función transformar, accede al primer elemento de la tupla persona (que es el nombre) y toma su primer carácter (índice 0).
Luego, convierte el segundo elemento de la tupla persona (que es la edad) en una cadena usando str().
Concatena el primer carácter del nombre con la edad convertida en cadena.
Define una lista llamada lista_personas que contiene tuplas donde el primer elemento es el nombre y el segundo elemento es la edad de diferentes personas.
Utiliza la función map() para aplicar la función transformar a cada elemento de lista_personas.
Convierte el resultado de map() en una lista llamada filtrada.
Finalmente, imprime la lista filtrada. """


def todos_pares(lista):
    todos_pares=True   # si aca pongo false y en el if hago == 0 True, lo que pasa es que siempre me va a dar true xq mientras haya mas elementos true me va a tomar eso y no el negtivo
    for elemento in lista:
        if elemento % 2 !=0:
            todos_pares=False
    return todos_pares

resultado= todos_pares([1,4,6,8,10]) 
print(resultado)       
lista=[2,4,6,8]
lista=lista[0:3]
print(lista)

i = 1

while i < 7:
    print("hola")
    i=i+1