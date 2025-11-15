# proyecto_BibliotecaVecinal



Este proyecto es un sistema para una biblioteca comunitaria donde se pueden gestionar libros y préstamos a socios utilizando Python. Todos los datos ingresados para libros y socios se cargan de manera automática en archivos CSV. 

A) Requisitos:
Pyhon 3 instalado. No se requieren bibliotecas externas por el uso del módulo estándar CSV. 

B) Contenidos:
Al abrir el proyecto, se abrirá una carpeta llamada datos/ donde se almacenan los archivos CSV.

main.py (Menú principal y flujo del programa)
funciones.py (lógica y persistencia)
datos/ #Carpeta donde se almacenan los datos
  -libros.csv
  -socios.csv

C) Funcionalidad del menú:
El programa opera con dos colecciones, libros y socios, después de cada modificación, los datos e interacciones se guardan en estos.

Opciones de gestion:
1. Agregar libro (libros.csv)
2. Actualizar libro (libros.csv)
3. Eliminar libro (libros.csv)
4. Listar un libro (Solo lectura)
5. Registrar un préstamo (Disminuye el stock del libro y lo agrega a un socio)
6. Registrar devolución (Aumenta el stock del libro y lo resta de un socio)
7. Registrar socio (socios.csv)
8. Eliminar socio (socios.csv)
9. Salir del programa (Sale del sistema)

D) Estructura y persistencia:
El sistema utiliza una arquitectura modular en donde cada archivo tiene una función:
main.py (Interfaz):
Inicia el sistema, cargando todos los datos en memoria al comienzo (fn.cargar_libros()). Muestra el menú y pasa las variables que contienen los datos (libros y socios) a las funciones de lógica para que estas realicen las modificaciones.

funciones.py (Lógica):

Este archivo maneja la conversión de datos y la persistencia:
Carga (Importación): Las funciones cargar_libros() y cargar_socios() leen el CSV y convierten la lista de filas en el formato de Diccionario con clave ID/RUN que usa el programa.
Guardado (Exportación): Las funciones de gestión (ej. agregar_libro) llaman a guardar_libros() o guardar_socios(). Estas funciones convierten el diccionario modificado de vuelta al formato de Lista de filas CSV y sobrescriben el archivo en el disco.

E) Ejemplos de ejecución:
  
   BIBLIOTECA VECINAL
1. Agregar libro.
2. Actualizar libro.
3. Eliminar libro.
4. Listar un libro.
5. Registrar préstamo.
6. Registrar devolución.
7. Registrar socio.
8. Eliminar socio.
9. Salir del programa.

Ingrese la opción que desea ingresar (1-9): 1

Ingrese ID del libro: L001
Ingrese el titulo del libro: El Principito
Ingrese autor del libro: Antoine de Saint-Exupéry
Ingrese el genero del libro: Fantasía
Ingrese cuantos libros va a registrar: 10
Libro registrado correctamente.
(El cambio se guardó automáticamente en datos/libros.csv)

Ingrese la opción que desea ingresar (1-9): 7

Registrar socio 
Ingrese RUN del socio: 19123456-7
Ingrese nombre COMPLETO del socio: Ana María Pérez López
Socio registrado correctamente.
(El cambio se guardó automáticamente en datos/socios.csv)

Ingrese la opción que desea ingresar (1-9): 5

Registrar prestamo
Ingrese run del socio: 19123456-7
Ingrese ID del libro que desea prestar: L001

Préstamo registrado correctamente:
Libro: El Principito (ID: L001)
Autor: Antoine de Saint-Exupéry
Socio: Ana María Pérez López (RUN: 19123456-7)
Stock restante del libro: 9 
(Los cambios se guardaron automáticamente en datos/libros.csv y datos/socios.csv)

Ingrese la opción que desea (1-9): 4

ID: L001
Título: El Principito
Autor: Antoine de Saint-Exupéry
Género: Fantasía
Stock: 9
Prestados: 1
(Otros libros si los hay)

Ingrese la opción que desea ingresar (1-9): 9

Saliendo del programa...
