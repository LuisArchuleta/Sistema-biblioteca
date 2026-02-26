from CatalogoLibros import catalogoLibros 
from Libro import Libro
from Usuario import Usuario
from CatalogoUsuarios import catalogoUsuarios

libros=[]
catalogolibros=catalogoLibros(libros)

usuarios=[]
catalogousuarios=catalogoUsuarios(usuarios)

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
        
        opcion=int(input("Opcion"))
        match opcion:
            case 1:
                menuLibros()
            case 2:
                menuUsuarios()
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
        opcion=int(input("Opcion:"))
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
        opcion=int(input("Opcion:"))
        match opcion:
            case 1:
                registrarUsuario()
            case 2:
                catalogoUsuarios.mostrarUsuarios(usuarios)
            case 3:
                menuLibros()
            case _:
                print("Opcion no valida")
            
def registrarUsuario():
  id=input("ID:")
  nombre=input("Nombre:")
  usuario=Usuario(id,nombre)
  catalogousuarios.agregar(usuario)

menu_principal()