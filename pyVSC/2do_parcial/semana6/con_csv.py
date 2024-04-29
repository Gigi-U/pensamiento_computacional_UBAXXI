import csv
#* Archivos Planos – Comma Separated Values (csv)
# creo los archivos
archivo1 = open("2do_parcial/semana6/datos1.csv", "a")
archivo1.close()

archivo2 = open("2do_parcial/semana6/datos2.csv", "a")
archivo2.close()

archivo3 = open("2do_parcial/semana6/datos3.csv", "a")
archivo3.close()

# creo la info que va en los archivos
import csv

data1 = [
    ['Luciana', 'Juárez', 'Santiago del Estero', 95],
    ['Martín', 'López', 'Córdoba', 40],
    ['Valeria', 'Gómez', 'Buenos Aires', 28],
    ['Joaquín', 'Martínez', 'Rosario', 35],
    ['Carolina', 'Rodríguez', 'Mendoza', 50]
]

data2 = [
    ['Jazmín', 'Gerez', 'Formosa', 95],
    ['Ana Laura', 'Jiménez', 'Chaco', 98],
    ['Roberto', 'Luna', 'Corrientes', 68],
    ['Joaquín', 'Ortiz Alba', 'Entre Ríos', 88],
    ['Antonio', 'Peñate', 'Río Negro', 83],
    ['Marcelo', 'Villate', 'Santa Cruz', 99],
    ['Mariano', 'Villafáñez', 'Santa Cruz', 98],
    ['Nicolás', 'Luzuriaga', 'Santa Cruz', 97],
    ['Agustín', 'Méndez', 'Formosa', 77]
]

data3 = [
    ['Andrés', 'Gil Gómez', 'CABA', 85],
    ['Andrea', 'Paz', 'CABA', 99],
    ['Pablo', 'Paz Iraola', 'Buenos Aires', 77],
    ['Paulina', 'Estarda', 'La Pampa', 88],
    ['Paula', 'García', 'Río Negro', 83],
    ['Lucía', 'González', 'Neuquén', 99],
    ['María', 'López', 'Córdoba', 65],
    ['Marcos', 'Fernández', 'Mendoza', 75],
    ['Diego', 'Martínez', 'Salta', 70],
    ['Luciano', 'Pinto', 'La Rioja', 81],
    ['Rossana', 'del Olmo', 'Chubut', 84],
    ['Victoria', 'Antón', 'Salta', 62]
]

# Nombres de los archivos CSV
nombre_archivo1 = '2do_parcial/semana6/datos1.csv'
nombre_archivo2 = '2do_parcial/semana6/datos2.csv'
nombre_archivo3 = '2do_parcial/semana6/datos3.csv'

# Función para escribir datos en archivo CSV
def escribir_datos_csv(nombre_archivo, datos):
    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        for fila in datos:
            writer.writerow(fila)
        print(f'Se ha escrito exitosamente en {nombre_archivo}')

# Escribir datos en cada archivo CSV
escribir_datos_csv(nombre_archivo1, data1)
escribir_datos_csv(nombre_archivo2, data2)
escribir_datos_csv(nombre_archivo3, data3)

# creo el archivo único y agrego los otros archivos

archivo_unico = open("2do_parcial/semana6/datosCompletos.csv", "a")
archivo_unico.close()

archivo_unico = open("2do_parcial/semana6/datosCompletos.csv", "w")
b=[]

dat= open('2do_parcial/semana6/datos1.csv')
a= dat.readlines()
dat.close()

for i in range(len(a)):
    a[i]=a[i].strip('\n')
    a[i]=a[i].split(',')
    a[i][3]=int(a[i][3])
b=b+a

dat= open('2do_parcial/semana6/datos2.csv')
a= dat.readlines()
dat.close()

for i in range(len(a)):
    a[i]=a[i].strip('\n')
    a[i]=a[i].split(',')
    a[i][3]=int(a[i][3])
b=b+a

dat= open('2do_parcial/semana6/datos3.csv')
a= dat.readlines()
dat.close()

for i in range(len(a)):
    a[i]=a[i].strip('\n')
    a[i]=a[i].split(',')
    a[i][3]=int(a[i][3])
b=b+a

b.sort(reverse=True,key=lambda b:(b[3],b[2]))
for elemento in b:
    print(elemento)

for elemento in b: 
    elemento[3]=str(elemento[3])
    ele=';'.join(elemento)+'\n'
    archivo_unico.write(ele)
archivo_unico.close()    