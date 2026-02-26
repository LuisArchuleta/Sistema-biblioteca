from CatalogoLibros import catalogoLibros 
from libro import Libro
from Usuario import Usuario
from CatalogoUsuarios import catalogoUsuarios
from GestionPrestamos import GestionPrestamos

libros={}
catalogolibros=catalogoLibros(libros)

usuarios={}
catalogousuarios=catalogoUsuarios(0,usuarios)

gestionPrestamos = GestionPrestamos()

def menu_principal():
    while True:
        print("""
    SISTEMA BIBLIOTECARIO
----------------------------
1.-Alta y gestion de libros
2.-Registro de usuarios
3.-Prestamos y devoluciones
4.-Reportes y consultas
5.-Salir del programa
----------------------------
    """)
        
        opcion=int(input("Opcion: "))
        match opcion:
            case 1:
                menuLibros()
            case 2:
                menuUsuarios()
            case 3:
                menuPrestamosyDevoluciones()
            case 4: 
                menuReportesyConsultas()
            case 5:
                print("\nSaliste del programa\n")
                break
            case _:
                print("Opcion no valida")
                
def menuLibros():
    while True:
        print("""
Alta y gestion de libros
----------------------------
1.-Registrar libro
2.-Consultar disponibilidad
3.-Buscar por titulo o autor
4.-Volver
----------------------------
        """)
        opcion=int(input("Opcion: "))
        match opcion:
            case 1:
                crearLibros()
            case 2:
                catalogoLibros.mostrarDisponibilidad(catalogolibros)
            case 4:
                break
            case _:
                print("Opcion no valida")
            

def crearLibros():
  isbn = input("ISBN: ")
  titulo = input("Titulo: ")
  autor = input("Autor: ")
  n_ejemplares = input("Numero de ejemplares: ")
  libro = Libro(isbn,titulo,autor,n_ejemplares)
  catalogolibros.agregar(libro)

def menuUsuarios():
    while True:
        print("""
Alta y gestion de usuarios
----------------------------
1.-Registrar usuario
2.-Consultar usuarios
3.-Volver
----------------------------
        """)
        opcion=int(input("Opcion: "))
        match opcion:
            case 1:
                registrarUsuario()
            case 2:
                catalogoUsuarios.mostrarUsuarios(catalogousuarios)
            case 3:
                break
            case _:
                print("Opcion no valida")

def registrarUsuario():
  nombre = input("Nombre: ")
  usuario = Usuario(catalogousuarios.id,nombre)
  catalogousuarios.agregar(usuario)

def menuPrestamosyDevoluciones():
     while True:
        print("""
Prestamos y Devoluciones
----------------------------
1.-Realizar prestamo
2.-Realizar devolucion
3.-Volver
----------------------------
        """)
        opcion=int(input("Opcion: "))
        match opcion:
            case 1:
                realizar_prestamo()
            case 2:
                devolver()
            case 3:
                break
            case _:
                print("Opcion no valida")

def realizar_prestamo():
    print("\n--- Realizar Préstamo ---")
    isbn = input("Ingrese el ISBN del libro: ")
    id_usuario = int(input("Ingrese el ID del usuario: "))    
    resultado = gestionPrestamos.realizar_prestamo(isbn, id_usuario, catalogolibros, catalogousuarios)
    print(f"\n{resultado}")

def devolver():
    print("\n--- Realizar Devolución ---")
    isbn = input("Ingrese el ISBN del libro: ")
    id_usuario = int(input("Ingrese el ID del usuario: "))
    resultado = gestionPrestamos.devolver(isbn, id_usuario, catalogolibros)
    print(f"\n{resultado}")

def menuReportesyConsultas():
     while True:
        print("""
Reportes y Consultas
----------------------------
1.-Top 3 de libros más prestados
2.-Listado de prestamos activos
3.-Consultas de libros por autor
4.-Volver
----------------------------
        """)
        opcion=int(input("Opcion: "))
        match opcion:
            case 1:
                tops = catalogoLibros.top3_libros()
                for i, libro in enumerate(tops, 1):
                   print(f"{i}. {libro.titulo} ({libro.veces_prestado} veces)")
            case 2:
                gestionPrestamos.mostrar_prestamos_activos()
            case 3: 
                libros_por_autor()
            case 4:
                break
            case _:
                print("Opcion no valida")

def libros_por_autor():
    autor = input("\nEscriba el nombre del autor: ")
    resultados = catalogolibros.buscar_por_autor(autor)
    if resultados:
        for l in resultados:
            print(f"\nTítulo: {l.titulo} | ISBN: {l.isbn} | Disponibles: {l.n_ejemplares}")
    else:
        print("No se encontraron libros de ese autor.")

if __name__ == "__main__":
    menu_principal()