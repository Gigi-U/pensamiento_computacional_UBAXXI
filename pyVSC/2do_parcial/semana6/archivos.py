# los archivos hacen que la info persista en el tiempo y q se pueda trabajar con mucha info
#& ejemplo crea txt y escribe
archivo = open("archivo.txt", "a")
archivo.write("Buenas")
archivo.writelines(["\nhola", "adios"])
archivo.writelines("\nchau")
archivo.close()

archivo = open("archivo.txt", "r+")
leer=archivo.read()
linea=archivo.readline()
lineas= archivo.readlines()
print(leer)
# print(linea)
# print(lineas)
archivo.close()

#& ejemplo csv

