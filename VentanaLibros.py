import tkinter as tk
from libro import Libro
from CatalogoLibros import catalogoLibros
from tkinter import ttk

class Menulibros:
    
   def menuLibros():
    print("""
Alta y gestion de libros
----------------------------
1.-Registrar libro
2.-Consultar disponibilidad
3.-Buscar por titulo o autor
4.-Volver
----------------------------
    """)

def crearLibros():
    print("\n--- Registro de Nuevo Libro ---")
    isbn = input("Ingrese ISBN: ")
    titulo = input("Ingrese Título: ")
    autor = input("Ingrese Autor: ")
    n_ejemplares = int(input("Número de ejemplares: "))
    
    nuevo_libro = Libro(isbn, titulo, autor, n_ejemplares)
    
    catalogoLibros.agregar(nuevo_libro)
    
    print(f"Se ha añadido el libro '{titulo}' al catálogo.")  