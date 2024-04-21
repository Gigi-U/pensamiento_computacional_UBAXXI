""" 1. En una escuela se quiere tener un sistema para guardar la información de sus estudiantes para tener
mejor organizado sus datos.
a. Crear un diccionario que sirve para representar a una persona en este contexto, pensar en las
características que se consideren más relevantes para identificar a una persona (su nombre,
DNI, edad, etc).
b. Agregar al diccionario creado, un campo que sea otro diccionario y sirva para guardar el curso
del estudiante y sus características (año, división, orientación, etc).
c. Teniendo una lista de diccionarios de estudiantes, buscar en la lista la persona con mayor edad
e imprimirla por pantalla. """

""" 2. En un vivero se guardan las plantas en una lista de diccionario con la siguiente información: especie, si
necesita luz solar o no, y el precio. (OBSERVACIÓN: ¿Qué tipo de dato nos permitía guardar si algo es
verdad o no?). Ahora se necesita un sistema que guarde las plantas a medida que van llegando. Se pide
hacer una función que reciba la lista de diccionarios de plantas, y los datos de la planta nueva y agregue
esa planta a la lista de diccionarios. """

""" 3. Se representa un ticket de supermercado como una lista de diccionarios, donde cada diccionario tiene
la siguiente información:
● Nombre del producto
● Precio por unidad
● Cantidad
Se pide hacer una función que reciba el ticket y devuelva el monto total a pagar.
 """

""" 4. Sol tiene una lista de diccionarios donde guarda todas las películas que vió. La información que tiene
para cada una es: el nombre de la serie, año en que salió, y la puntuación que le puso del 1 al 10. Hace
mucho que quiere que Tomás empiece a ver las películas que ella considera que son las mejores que
vio.
Hacer una función que reciba el diccionario de las películas que vió Sol, y que devuelva una nueva lista
de diccionarios donde sólo estén las películas que tienen puntaje mayor a 7.
 """

""" 5. Un profesor guarda las notas del primer parcial de sus alumnos en una lista de diccionarios que guarda
la siguiente información:
● Nombre
● Apellido
● Intento
● Nota
Donde ”intento” es la instancia que está rindiendo, 1 si es la primera vez que rinde el parcial, 2 si es el
primer recuperatorio y 3 si es el segundo recuperatorio.
Se pide hacer una función que, dado esta lista de diccionarios, devuelva el promedio de las notas en la
primera oportunidad que rindieron los alumnos.
¿Cómo harían para generalizar la función y que el intento sea parametrizable? Es decir, que no
solamente sirve para el intento 1, sino que también pueda servir para los demás.
2
Diccionarios GUIA DE EJERCICIOS Nº 5
 """

""" 6. En una fábrica, se hace un chequeo de calidad a los productos antes de cada entrega. El resultado del
chequeo de la entrega se guarda en una lista de diccionarios, donde cada diccionario tiene la siguiente
información de cada producto:
● Código del producto
● Fecha de vencimiento
● Si pasó el chequeo de calidad o no
Se pide hacer una función que reciba esta lista de diccionarios y elimine todos los productos que no
pasaron el chequeo de calidad. Devolver en una tupla el diccionario con los elementos eliminados y la
cantidad de elementos que quedaron en el diccionario.
Dado que la tupla es inmutable y nosotros no podemos ir agregando elementos a una tupla, ¿En qué
momento deberíamos crear la tupla?
 """

""" 7. Se quiere guardar la información de un grupo de maratonistas. Se necesita guardar su nombre, DNI, y
todas las maratones que corrió, de la cual a su vez se quiere tener el nombre de cada una, el año, el
puesto en que salió el maratonista, y el tiempo que tardó en terminarla.
a. Crear el diccionario que represente esta situación.
AYUDA: Queremos guardar muchos maratonistas, y a su vez, muchas maratones para cada
maratonista, entonces ¿Qué tipo de dato debería ser el campo que guarda todas las
maratones? ¿Y qué tipo de dato es la maratón en sí?
b. Teniendo una lista de diccionarios de maratonistas, ordenarlos alfabéticamente.
c. Ordenar las maratones de cada maratonista según el tiempo que tardó en completar cada una
de forma ascendente.
 """