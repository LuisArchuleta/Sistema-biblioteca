import tkinter as tk
from libro import Libro
from CatalogoLibros import catalogoLibros
from tkinter import ttk

class Menulibros:
    
   def menuLibros():
    print("""
Alta y gestion de libros
----------------------------
1.Registrar libro
2.-Consultar disponibilidad
3.-Buscar por titulo o autor
4.-Volver
----------------------------
    """)

def crearLibros():
  