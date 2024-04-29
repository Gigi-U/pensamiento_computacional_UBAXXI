
#* Archivos Planos – Archivos de Texto (txt)
# creo el archivo
archivo = open("2do_parcial/semana6/vacaloca.txt", "a")
archivo.close()

# ingreso al archivo para empezar a escribir en este
vaca_txt=open('2do_parcial/semana6/vacaloca.txt','r+')
t = vaca_txt.readline()
print(t)
t = input('Ingresá un texto con vaca: ')
while (t.lower()).count('vaca')==0:
    t = input('Ingresá un texto con vaca: ')
vaca_txt.write(t+'\n')
vaca_txt.close()

# reabre el archivo para leerlo e imprimirlo
vaca_txt=open('2do_parcial/semana6/vacaloca.txt')
todas = vaca_txt.readlines()
for linea in todas:
    print(linea.strip('\n'))
vaca_txt.close()