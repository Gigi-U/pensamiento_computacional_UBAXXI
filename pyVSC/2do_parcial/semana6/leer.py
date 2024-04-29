archivo = open("archivo.txt", "r+")

linea=archivo.readline()    
print(linea)
print("----------")
lineas= archivo.readlines()
print(lineas)

# leer=archivo.read()
# print(leer)

archivo.close()