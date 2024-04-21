
#& Secuencias
#Las secuencias son un conjunto de datos. 
#? los strings. (secuencias de caracteres)
# los strings son un conjunto contiguo de memoria. no pueden modificar su longitud.
#las secuencias de sirting son inmutables.
# al concatenar 2 variables de string yo creo una 3ra variable.

#? Las tuplas
#sin inmuables como los strings pero pueden contener elementos de distinto tipo de datos. ej puedo tener letras, int, una tupla, una lista, etc.

#? Listas
# parecidas a las tuplas pero son mutables (le puedo agregar quitar o modificar sus elementos)

#* EJEMPLOS DE TUPLAS
tupla_0=() #vacía
tupla_1=("flor",10,("Gisela",11,True)) # si tiene  1 elemento solo debo agregar una coma al final para que el programa se de cuenta que es una tupla
print(tupla_1)
#* EJEMPLOS DE LISTAS
lista_0=[]
lista_1=["Gisela",False,["Carmela","Indi"]]
print(lista_1)
#^ ACCESO A TUPLAS Y LISTAS

elemento_3_tupla=tupla_1[2]
elemento_1_lista=lista_1[0]
print(elemento_3_tupla)
print(elemento_1_lista)

# seleccionar un valor sin tener que hacer lo anterior
fecha = (26,"febrero",1980)
dia,mes,año=fecha
print(mes)

#? EJEMPLO
print("--------Lista original: ")
puntos = [
    (4,6),
    (8,2),
    (10,5),
    (1,1),
    (0,7),
    (0,0),
    (2,3),
    (2,2)
]
contador=0
for punto in puntos:
    x,y=punto
    contador+=1
    print(contador,") x: ",x,"- y: ",y)

print("--------agregando un elemento: ")
puntos.append((50,50))
contador=0
for punto in puntos:
    x,y=punto
    contador+=1
    print(contador,") x: ",x,"- y: ",y)

print("--------agregando un elemento en una posición específica: ")
puntos.insert(4,(80,80))

contador=0
for punto in puntos:
    x,y=punto
    contador+=1
    print(contador,") x: ",x,"- y: ",y)

print("--------borrando un elemento: ")
puntos.remove((0,7))
contador=0
for punto in puntos:
    x,y=punto
    contador+=1
    print(contador,") x: ",x,"- y: ",y)

print("--------modificando un elemento: ")
for i, punto in enumerate(puntos):
    if punto == (80, 80):
        puntos[i] = (80,81)

contador = 0
for punto in puntos:
    x, y = punto
    contador += 1
    print(contador, ") x: ", x, "- y: ", y)