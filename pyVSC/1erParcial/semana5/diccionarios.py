#mapear valor con 1 o grupo de datos(clave). A diferencia de las listas, el acceso a los datos es mucho más flexible o customizable
# Los diccionarios son mutables (se puede editar)
#diccionario = {1:"hola",2:"chau"}

diccionario = {"saludo_inicial":"hola","saludo_final":"chau"}
print("-----acceder a todo-----")

print(diccionario)
# acceder a dato
print("-----acceder a dato-----")
print(diccionario["saludo_inicial"])

#editar diccionario
print("-----editar diccionario-----")
diccionario["saludo_navidad"]="Feliz navidad!"
print(diccionario)
print(diccionario["saludo_navidad"])

print("-----ejemplo 2-----")

amigos={
    "Juan":(25,"marzo","nos conocimos en la playa"),
    "Pedro":(30,"febrero","nos conocimos en Cordoba"),
    "María":(44,"agosto","nos conocimos en la escuela"),
    "Ana":(50,"septiembre","nos conocimos en la cancha")
}

# clear(), pop(), .items() , .keys()

print(amigos.keys())
print(amigos.items())

# update(

amigos.update(
    {"Ana":(50,"septiembre","Me equivoqué. Nos conocimos en la montaña")}
)
print(amigos["Ana"])

#! si hago update tengo que tener cuidado porque si escribo la clave diferente no va a cambiarla sino que va a agregar un elemento nuevo. Ej: poniendo "ana" en vez de "Ana"
amigos.update(
    {"ana":(50,"septiembre","Me equivoqué. Nos conocimos en la montaña")}
)
print(amigos)
