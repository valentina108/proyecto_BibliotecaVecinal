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
        print("7. Registrar socio.")
        print("8. eliminar socio")
        print("9. salir del programa")


        opc = int(input("Ingrese a la opción que desea ingresar 1-8: "))

        if opc == 1:
            fn.agregar_libro(libro) 
        elif opc == 2:
            fn.actualizar_libro(libro)
        elif opc == 3:
            fn.eliminar_libro(libro)
        elif opc == 4:
            fn.listar_libro(libro)
        elif opc == 5:
            fn.registrar_prestamo(libro,socios)
        elif opc == 6:
            fn.registrar_devolucion(libro,socios)
        elif opc == 7:
            fn.registrar_socio(socios)
        elif opc == 8:
            fn.eliminar_socio(socios)
        elif opc == 9:
            print("Saliendo del programa...")
            break