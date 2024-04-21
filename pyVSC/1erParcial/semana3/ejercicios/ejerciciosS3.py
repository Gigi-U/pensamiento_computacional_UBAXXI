
#&  Expresiones
#############################################################
print("-------EJERCICIO 1 👇")
# 1. Escribir la expresión para saber si un número es más grande que otro. Guardarla en una variable de tipo bool e imprimirla por pantalla para ver su valor.
a=19
b=13
esMayor= a>b  
print(esMayor)

#############################################################
print("-------EJERCICIO 2 👇")
# 2. Repetir el punto anterior pero con la expresión que determina que una letra NO es vocal.
letra="z"
esVocal=True
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(esVocal)
else:
    print(not esVocal) 
#############################################################
print("-------EJERCICIO 3 👇")
# 3. Repetir pero para la expresión que permite saber si un número es par y menor a 10.
evenNumber=2
if evenNumber%2==0 and evenNumber <10:
    print("es par y menor a 10")
else:
    print("una de las dos condiciones no se está cumpliendo")       

#& Estructuras de control condicionales 
#############################################################
print("-------EJERCICIO 4 👇")
""" 4. Crear una función que dado un número, devuelva su valor absoluto. El valor absoluto de un número es
el mismo número sin considerar el signo.
Por ejemplo, el absoluto de 2 es 2 (|2| = 2) y el absoluto de -4 es 4 (|-4|=4). """

def valorAbsoluto(nr):
    if nr < 0:
        return nr * -1
    else:
        return nr

absoluto = valorAbsoluto(-5)
print(absoluto)

#############################################################
print("-------EJERCICIO 5 👇")
""" 5. Crear el programa al que sea imposible ganarle en el juego de “Piedra, papel o tijera”. Cada elemento va a ser representado con una letra: R para piedra, P para papel y T para tijera.
a. Hacer una función que le haga al usuario ingresar alguna de esas letras, e imprima por pantalla la jugada para ganarle. Por ejemplo:
> ¡Juguemos! Ingresá piedra ( R), papel (P) o tijera (T)
> P
> Tijera. ¡Te gané!
ATENCIÓN: Observar cómo se usa una frase inicial para darle a entender al usuario lo que tiene que hacer (en este caso ingresar alguna de las tres letras).
b. Mostrar por pantalla el mensaje “NO vale” cuando el usuario ingresa una letra no válida
(distinta de R, P o T). """

def piedraPapelTijeraTramposo():
      palabraIngresada = input("¡Juguemos! Ingresá piedra (R), papel (P) o tijera (T): ")
      if palabraIngresada == "R":
          return "Papel. ¡Te Gané!"
      elif palabraIngresada == "P":
          return "Tijera. ¡Te Gané!"
      elif palabraIngresada == "T":
          return "Piedra. ¡Te Gané!"
      else:
          return "No vale"
print(piedraPapelTijeraTramposo())

#############################################################
print("-------EJERCICIO 6 👇")
""" 6. Escribir código que dado dos enteros, determine si la suma de ambos da menos que 100. Si la suma de ambos es menor a 100, calcular cuánto falta para llegar a 100 y mostrar por pantalla un mensaje con ese valor. 
Si la suma es mayor a 100, mostrar un mensaje diciendo “Llega a 100”. 
Extra: ¿Cómo harían para que el programa quede generalizado para cualquier límite, a elección del usuario, y no solo para 100?. """

def llegACien(entero1, entero2):
    suma = entero1 + entero2
    if suma > 100:
        return"Llega a 100"
    elif suma < 100:
        return"Faltan " + str(100 - suma) + " para que la suma llegue a 100"
    else:
        return"Es justo 100"

respuesta = llegACien(99, 1)
print(respuesta)

#Extra 
print("-------EJERCICIO 6 - extra 👇")

def limiteCustom(entero3, entero4, limite):
    suma = entero3 + entero4
    if suma > limite:
        return "Llega al límite"
    elif suma < limite:
        return "Faltan " + str(limite-suma) + " para que la suma llegue al límite"
    else:
        return "Es justo el limite"

respuesta2 = limiteCustom(99, 1, 150)
print(respuesta2)

#############################################################
print("-------EJERCICIO 7 👇")
""" 7. Se tienen letras para representar las estaciones del año:
● V para verano
● O para otoño
● I para invierno
● P para primavera
Crear una función que dada una letra, imprima por pantalla la estación del año que representa (es
decir, si se ingresa V se mostrará por pantalla el mensaje “Verano”). En caso de no representar a
ninguna estación mostrar un mensaje que diga “error”. Probar la función creada llamándola con A, P, O,B, V e I."""

def estaciones(letra):
    respuesta=""
    if letra == "V":
        respuesta= "Verano"
        return respuesta
    elif letra =="O":
        respuesta= "Otoño"
        return respuesta
    elif letra =="I":
        respuesta= "Invierno"
        return respuesta
    elif letra =="P":
        respuesta= "Primavera"
        return respuesta
    else: return "error"

estacion= estaciones("O")
print(estacion)    

#&  Estructuras de control iterativas 
#############################################################
print("-------EJERCICIO 8 👇 ---  FOR" )
""" 8. Se quiere hacer un programa para enseñar a unos niños a contar. Crear una función que reciba un número entero e imprima por pantalla los números del 1 hasta ese número con la estructura de control iterativa for. """
def contemos(nr):
    for i in range(1, nr + 2):
        print(i)
contemos(9)

#############################################################
print("-------EJERCICIO 9 👇")
""" 9. Se quiere mejorar el programa para enseñar matemáticas pensado en el ejercicio anterior. Ahora se necesita una funcionalidad que permita a los niños aprender las tablas. Crear una función que reciba un número entero e imprima por pantalla la tabla de ese número del 1 al 10. """
def multipliquemos(nr):
    for i in range(1, 11):
        print(nr, "x", i, "=", nr * i)
multipliquemos(2)

print("-------EJERCICIO 9 👇 ---- extra todas las tablas del 1 al 10 por  numero limite ")

def multipliquemos2(limite):
    for numero in range(1, limite + 1):
        print("Tabla del", numero)
        for i in range(1, 11):
            print(numero, "x", i, "=", numero * i)
        print()
limite = int(input("Ingrese un numero y se imprimirán todas las tablas hasta la de ese número: "))
multipliquemos2(limite)

#############################################################
print("-------EJERCICIO 10 👇 -- Con While" )
""" 10. Crear una función que simule un cumpleaños: que dado un entero imprima “Que los cumplas feliz” esa cantidad de veces. """
def felizCumpleaños(edad):
    saludos = 1
    while saludos <= edad:
        print("Que los cumplas feliz")
        saludos += 1

edad = int(input("Ingresa tu edad: "))
felizCumpleaños(edad)

#############################################################
print("-------EJERCICIO 11 👇")
""" 11. En un almacén están buscando la forma de hacer los cobros más automáticamente. Para esto, se nos pide crear una función que reciba un número entero que representa lo que hay que cobrar, le pida al usuario ingresar un monto, y se vaya mostrando por pantalla cuánto falta para completar el pago.
Repetir este proceso hasta que la deuda sea 0 o menor. Por ejemplo, si se recibe el monto 30:
> El importe a pagar es de 30 pesos. Por favor, ingrese un monto.
> 10
> El importe a pagar es de 20 pesos. Por favor, ingrese un monto.
> 15
> El importe a pagar es de 5 pesos. Por favor, ingrese un monto.
> 5"""

def cuantoFalta(entero):
    pagado = 0
    while pagado < entero:
        monto = float(input("El importe a pagar es de " + str(entero - pagado) + " pesos. Por favor, ingrese un monto: "))
        pagado += monto
cuantoFalta(10000)

#& Estructuras de control condicionales e iterativas 
#############################################################
print("-------EJERCICIO 12 👇")
""" 12. Escribir código que recorra los números del 1 al 20 y determine para cada uno si es par o impar, imprimiendo un mensaje por pantalla en cada caso. Es decir, el output esperado sería:
> El número 1 es impar.
> El número 2 es par.
…
> El número 20 es par. """

def parOInpar():
    numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    for i in numbers:
        if i%2==0:
            print("el número "+ str(i) +" es par")
        else:  print("el número "+ str(i) +" es impar")  
parOInpar()

#sin el array:
def parOInpar2():
    for i in range(1, 21):
        if i % 2 == 0:
            print("el número " + str(i) + " es par")
        else:
            print("el número " + str(i) + " es impar")

parOInpar2()

#############################################################
print("-------EJERCICIO 13 👇")
""" 13. Se tiene una máquina de sacar juguetes que funciona cuando se ingresa una determinada cantidad de fichas, y se quiere hacer una función que imite ese comportamiento.

a. Hacer una función que reciba un número que represente el precio de la máquina, e imprima por pantalla “Ingresá x fichas para comenzar” hasta que se hayan ingresado esa cantidad de letras F (que representan una ficha), y luego “¡A jugar!” cuando se hayan ingresado todas las fichas necesarias. 
Por ejemplo, si la función recibe 3, debería tener el siguiente
comportamiento:
> Ingresá 3 fichas para comenzar
> F
> Ingresá 3 fichas para comenzar
> F
> Ingresá 3 fichas para comenzar
> B
> Ingresá 3 fichas para comenzar
> F
> ¡A jugar!
ATENCIÓN: notar cómo cuando se ingresa una letra distinta de F, esta se ignora a la hora de contar la cantidad de fichas que fueron ingresadas.

b. Ahora se quiere que se vaya mostrando por pantalla, cuántas fichas FALTAN ingresar para empezar a jugar Es decir:
> Ingresá 3 fichas (F) para comenzar
> F
> Ingresá 2 fichas (F) para comenzar
> F
> Ingresá 1 fichas (F) para comenzar
> B
> Ingresá 1 fichas (F) para comenzar
> F
> ¡A jugar!

c. Agregar a la función el mensaje de error “Por favor solamente ingrese fichas reales (F)” cuando se recibe una letra distinta de F. """

def sacarJuguetes(cantidadFichas):
    fichasIngresadas=0
    while fichasIngresadas < cantidadFichas:
        fichasRestantes= cantidadFichas - fichasIngresadas  
        fichas=input("Ingresá "+str(fichasRestantes)+" fichas para comenzar(cada ficha es una F): ")
        if fichas=="F":
            fichasIngresadas
            fichasIngresadas+= 1
        else: 
            fichasIngresadas = fichasIngresadas  
            print("Por favor solamente ingrese fichas reales (F)")  
    print("¡A Jugar!")
sacarJuguetes(3)    

#############################################################
print("-------EJERCICIO 14 👇")
#! pendienteeeeeeeeeeeeeeeeeeeeeeeeeeeeee
""" 14. Crear una función que reciba un número entero e imprima los números primos entre 0 y el número ingresado.
AYUDA: un número es primo cuando solamente es divisible por sí mismo y por 1, es decir que para ver si es primo hay que ver que el módulo (%) de ese número con los anteriores hasta el 1 (sin incluirlo) sea distinto de 0, o sea que no sea divisible. """

def primos(nroEntero):
    for i in range(2, nroEntero + 1):
        es_primo = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                es_primo = False
                break
        if es_primo:
            print(i)
primos(10)    
#! pendiente


