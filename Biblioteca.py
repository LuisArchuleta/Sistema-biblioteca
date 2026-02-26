from CatalogoLibros import catalogoLibros 
from Libro import Libro
from Usuario import Usuario
from CatalogoUsuarios import catalogoUsuarios
from GestionPrestamos import GestionPrestamos

libros={}
catalogolibros=catalogoLibros(libros)

usuarios={}
catalogousuarios=catalogoUsuarios(0,usuarios)

print(catalogousuarios.id)

def menu_principal():
    while True:
        print("""
    SISTEMA BIBLIOTECARIO
----------------------------
1.-Alta y gestion de libros
2.-Registro de usuarios
3.-Prestamos y devoluciones
4.-Reportes y consultas
5.-Salir
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
            case _:
                print("Opcion no valida")
            


def crearLibros():
  isbn=input("ISBN:")
  titulo=input("Titulo:")
  autor=input("Autor:")
  n_ejemplares=input("Numero de ejemplares:")
  libro=Libro(isbn,titulo,autor,n_ejemplares)
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
                menuLibros()
            case _:
                print("Opcion no valida")

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
                menuLibros()
            case _:
                print("Opcion no valida")

def menuReportesyConsultas():
     while True:
        print("""
Alta y gestion de usuarios
----------------------------
1.-Realizar reporte
2.-Realizar consulta
3.-Volver
----------------------------
        """)
        opcion=int(input("Opcion:"))
        match opcion:
            case 1:
                registrarUsuario()
            case 2:
                catalogoUsuarios.mostrarUsuarios(catalogousuarios)
            case 3:
                menuLibros()
            case _:
                print("Opcion no valida")
            
def registrarUsuario():
  nombre=input("Nombre:")
  usuario=Usuario(catalogousuarios.id,nombre)
  catalogousuarios.agregar(usuario)

if __name__ == "__main__":
    menu_principal()