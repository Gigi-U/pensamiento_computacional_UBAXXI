
lista_personas = [
    ("Juan", 25),
    ("María", 30),
    ("Pedro", 40),
    ("Ana", 35),
    ("Luis", 28),
    ("Laura", 42),
    ("Carlos", 20),
    ("Sofía", 33),
    ("David", 27),
    ("Elena", 38)
]

# Encontrar con TRUE y FALSE   elemento in lista ->True o false
resultado = ("Elena",38) in lista_personas #true
print(resultado)
resultado = ("Gisela",44) in lista_personas #false
print(resultado)

# En que posición  está:   -> index 

resultado = lista_personas.index(("Carlos",20))
print(resultado)

# ordenar una lista:
print("----------ordena: ")

lista_personas.sort()
print(lista_personas)

print("----------reverso: ")
lista_personas.sort(reverse=True)
print(lista_personas)

def edad(lista_personas):
    return lista_personas[1]

print("----------key edad: ")
lista_personas.sort(key=edad)
print(lista_personas)
