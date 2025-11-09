import funciones as fn
libro = {}
socios = {}


while True:
        print("BIBLIOTECA VECINAL")
        print("1. Agregar libro.")
        print("2. Actualizar libro.")
        print("3. Eliminar libro.")
        print("4. Listar un libro.")
        print("5. Registrar préstamo.")
        print("6. Registrar devolución.")
        print("7. Reporte libros prestados.")
        print("8. Salir.")

        opc = int(input("Ingrese a la opción que desea ingresar 1-8: "))

        if opc == 1:
            fn.agregar_libro(libro) 
        elif opc == 2:
              pass
        elif opc == 3:
              fn.eliminar_libro(libro)
        elif opc == 4:
              pass
        elif opc == 5:
              pass
        elif opc == 6:
              pass
        elif opc == 7:
              pass
        elif opc == 8:
              print("Saliendo del programa...")
              break