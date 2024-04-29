# los archivos hacen que la info persista en el tiempo y q se pueda trabajar con mucha info
#& ejemplo crea txt y escribe
archivo = open("archivo.txt", "a")
archivo.writelines(["\nhola", "\nadios"])
archivo.writelines("\nchau")
archivo.close()

#& ejemplo csv

