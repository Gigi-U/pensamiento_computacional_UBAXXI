nombre="Gisela"
apellido="Urriza"

#conocer largo de un string
largo_nombre=len(nombre)
print(largo_nombre)
print("↑↑↑↑↑↑↑contando↑↑↑↑↑↑↑")

#concatenar nombre y apellido
nombre_completo=nombre+" "+apellido
print(nombre_completo)
print("↑↑↑↑↑↑↑concatenando↑↑↑↑↑↑↑")

# cortar un string 
#operando[::]
##operando[desde donde:hasta donde: cada cuantas letras] o [start:stop:step]
apodo= nombre[0:2:]
apodo2= apellido[:4:] # otra forma de hacer lo mismo
apodo_concatenado=apodo + ' '+apodo2
print(apodo_concatenado)
print("↑↑↑↑↑↑↑cortando↑↑↑↑↑↑↑")
