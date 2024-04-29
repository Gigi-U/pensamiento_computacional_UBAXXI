# por imput
def nombreYApellido():

    nombre=input("Ingresa tu nombre: ")
    apellido= input("ingresa tu apellido: ")
    return apellido, nombre
    
apellido, nombre = nombreYApellido()
print(apellido+", "+nombre)


# por parámetro
def nombreYApellido2(nombre, apellido):

    print(apellido+", "+nombre)
    
nombreYApellido2("Carmela", "Urriza")

#~ Usando MÉTODO FORMAT
def nombreYApellido3():
    apellido= input("ingresa tu apellido: ")
    nombre=input("Ingresa tu nombre: ")
    print("{}, {}".format(apellido, nombre))

nombreYApellido3()

#~ Usando Nueva notación
def nombreYApellido3():
    apellido= input("ingresa tu apellido: ")
    nombre=input("Ingresa tu nombre: ")
    print(f"{apellido}, {nombre}")

nombreYApellido3()

""" En Python 3.6 se añadió (PEP 498) una nueva notación para cadenas llamada cadenas "f", que simplifica la inserción de variables y expresiones en las cadenas. Una cadena "f" contiene variables y expresiones entre llaves ({}) que se sustituyen directamente por su valor. Las cadenas "f" se reconocen porque comienzan por una letra f antes de las comillas de apertura.

print(f"Me llamo {nombre} y tengo {edad} años.") """
