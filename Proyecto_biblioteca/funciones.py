libro = {}
socios = {}


#1 agregar libro
def agregar_libro(libro):
    id_libro = input("Ingrese ID del libro: ")
    titulo_libro = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese autor del libro: ")
    genero = input("Ingrese el genero del libro: ")
    stock = input("ingrese cuantos libros va a registrar: ")

    libro[id_libro] = {
    "titulo": titulo_libro,
    "autor": autor,
    "genero": genero,
    "stock": stock
}
    
    print("Libro registrado correctamente.")
    print(libro)

#2 actualizar libro

def actualizar_libro(libro):
        print("\n--- ACTUALIZAR LIBRO ---")
        id_libro = input("Ingrese el ID del libro que desea actualizar: ")

        if id_libro in libro:
            libro_encontrado = libro[id_libro]
            while True:
                    print("\n ACTUALIZAR LIBRO")
                    print("1.Actualizar título.")
                    print("2.Actualizar autor.")
                    print("3.Actualizar género.")
                    print("4.Actualizar stock.")
                    print("5. Salir.")

                    try:
                        opc_act=int(input("Ingrese una opción (1-5): "))
                    except ValueError:
                            print("Ingrese una opción válida.")

                    if opc_act == 1:
                        nuevo_titulo = input("Ingrese el nuevo título para el libro: ")
                        libro_encontrado["titulo"] = nuevo_titulo
                        print("Titulo actualizado correctamente")

                    elif opc_act ==2:
                        nuevo_autor = input("Ingrese el nuevo autor: ")
                        libro_encontrado["autor"] = nuevo_autor
                        print("Autor actualizado correctamente")

                    elif opc_act==3:
                        nuevo_genero = input("Ingrese nuevo género para el libro: ")
                        libro_encontrado["genero"] = nuevo_genero
                        print("Género actualizado correctamente")

                    elif opc_act==4:
                        nuevo_stock = int(input("Ingrese el nuevo stock: "))
                        libro_encontrado["stock"] = (nuevo_stock)
                        print("Stock actualizado correctamente")
                            
                    elif opc_act==5:
                        print("Volviendo al menú principal...")
                        break
                    else:
                        print("Debe ingresar una opción válida.")

        else:
            libro_encontrado
            print("Error: No se encontró un libro con ese ID.")

           
              


#3 eliminar libro
def eliminar_libro(libro):
    id_libro = input("Ingrese el ID del libro que desea eliminar: ")

    if id_libro in libro:
        del libro[id_libro]
        print("Libro eliminado correctamente.")
    else:
        print("no se encontro el libro ingresado")


#4 listar libros
def listar_libro(libro):
    print("\n--- LIBROS ---")
    for id_libro, datos in libro.items():
        print(f"ID: {id_libro}")
        print(f"Título: {datos['titulo']}")
        print(f"Autor: {datos['autor']}")
        print(f"Stock: {datos['stock']}")






#5 registrar prestamo
def registrar_prestamo(libro, socios):
    print("\n- Registrar prestamo")
    
    if not socios:
        print("No hay socios registrados.")
        return
    if not libro:
        print("No hay libros registrados.")
        return
    run_socio = input("Ingrese run del socio: ")
    
    if run_socio not in socios:
        print("No existe un socio con ese run.")
        return
        
    
    id_libro = input("Ingrese ID del libro que desea prestar: ")
    
    if id_libro not in libro:
        print("Error: No existe un libro con ese ID.")
        return
    
    if libro[id_libro]["stock"] <= 0:
        print("Error: No hay ejemplares disponibles de este libro.")
        return
    

    libro[id_libro]["stock"] -= 1
    libro[id_libro]["prestados"] += 1
    socios[run_socio]["prestamos_activos"].append(id_libro)
    
    print(f"\nPréstamo registrado correctamente:")
    print(f"Libro: {libro[id_libro]['titulo']} (ID: {id_libro})")
    print(f"Autor: {libro[id_libro]['autor']}")
    print(f"Socio: {socios[run_socio]['nombre']} (RUN: {run_socio})")
    print(f"Stock restante del libro: {libro[id_libro]['stock']}")


#6. registrr devolucion

def registrar_devolucion(libro, socios):
    print("\n--- DEVOLUCIÓN ---")
    
    run = input("RUN socio: ")
    
    if run not in socios:
        print("No existe socio")
        return
    
    prestamos = socios[run]["prestamos_activos"]
    if not prestamos:
        print("Sin préstamos")
        return
    
    print("Libros prestados:")
    for i, id_libro in enumerate(prestamos, 1):
        print(f"{i}. {libro[id_libro]['titulo']}")
    
    num = int(input("Número: ")) - 1
    id_libro = prestamos[num]
    
    libro[id_libro]["stock"] += 1
    prestamos.pop(num)
    
    print("Devolución hecha")




#7 registrar socio
def registrar_socio(socios):
    print("\n registrar socio ")
    run_socio = input("Ingrese RUN del socio: ")
    
    if run_socio in socios:
        print("Error: Ya existe un socio con ese run.")
        return
    
    nombre = input("Ingrese nombre COMPLETO del socio: ")

    socios[run_socio] = {
        "nombre": nombre,
    }
    
    print("Socio registrado correctamente.")
    print(socios)


#8 eliminar socio
def eliminar_socio(socios):
    print("\n Eliminar socio")
    run_socio = input("Ingrese RUN del socio que desea eliminar: ")

    if run_socio in socios:
        del socios[run_socio]
        print("Socio eliminado correctamente.")
    else:
        print("Error: No se encontró un socio con ese RUN.")



