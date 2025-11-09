libro = {}
socios = {}


#agregar libro
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

#actualizar libro






#eliminar libro
def eliminar_libro(libro):
    id_libro = input("ingrese el id del libro que desea eliminar: ")

    if id_libro in libro:
        del libro[id_libro]
        print("libro eliminado correctamente.")
    else:
        print("no se encontro el libro ingresado")
