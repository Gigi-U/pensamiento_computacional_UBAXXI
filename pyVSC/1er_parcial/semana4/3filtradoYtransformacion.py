
#& MAP Y FILTER
def cortar_palabra(palabra):
    return palabra[:4]

palabras = [
    "Variable", 
    "Función", 
    "Clase", 
    "Método", 
    "Bucle", 
    "Lista", 
    "Tupla", 
    "Diccionario", 
    "Conjunto", 
    "Cadena", 
    "Índice", 
    "Módulo", 
    "Biblioteca",
    "Importar", 
    "Exportar", 
    "Argumento", 
    "Operador", 
    "Condición", 
    "Iteración", 
    "Anidado"
]

palabras_cortas=map(cortar_palabra, palabras)
print(list(palabras_cortas))

print("sumar uno-------------------")
def sumar_uno(numero):
    return numero+1

numeros=[3,7,5,6,8,4,3]
nuevos_numeros = list(map(sumar_uno, numeros))
print(numeros)
print(nuevos_numeros)

print("filter-------------------")
#retorna true o false y filtra
#& FILTER

print("filtra palabras cortas-------------------")

def es_palabra_corta(flores):
    longitud=len(flores)
    if(longitud < 5):
        return True
    else:
        False
flores = [
    "Rosa", 
    "Lirio", 
    "Margarita", 
    "Tulipán", 
    "Girasol", 
    "Orquídea", 
    "Jazmín", 
    "Clavel", 
    "Amapola", 
    "Jacinto"
]
flores_cortas=list(filter(es_palabra_corta,flores))
print(flores_cortas)
