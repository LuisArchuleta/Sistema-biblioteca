#Ventana

from CatalogoLibros import catalogoLibros 
from libro import Libro

libros=[]
catalogolibros=catalogoLibros(libros)

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
            case _:
                print("Opcion no valida")


def crearLibros():
  isbn=input("ISBN:")
  titulo=input("Titulo:")
  autor=input("Autor:")
  n_ejemplares=input("Numero de ejemplares:")
  libro=Libro(isbn,titulo,autor,n_ejemplares)
  catalogolibros.agregar(libro)

menu_principal()