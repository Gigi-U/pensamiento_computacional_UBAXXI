
def anteriorYSiguiente():
    numero =int(input("Ingresa un número : "))
    numero_anterior= numero-1
    numero_siguiente= numero+1
    return  numero, numero_anterior, numero_siguiente

numero, numero_anterior, numero_siguiente= anteriorYSiguiente()    

print("el numero anterior a "+ str(numero)+ " es: "+ str(numero_anterior) +" y el siguiente es: "+ str( numero_siguiente))