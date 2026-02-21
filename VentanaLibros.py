import tkinter as tk
from libro import Libro
from CatalogoLibros import catalogoLibros
from tkinter import ttk

class VentanaLibros:
    
    def __init__(self,ancho,largo,ventanaPrincipal,catalogo):
        self.ancho=ancho
        self.largo=largo
        self.ventanaPrincipal=ventanaPrincipal
        self.catalogo=catalogo
        

    def abrirVentana(self):
        ventana_libros=tk.Toplevel(self.ventanaPrincipal)
        ventana_libros.geometry(f"{self.ancho}x{self.largo}+0+0")

        inputISBN=tk.Entry(ventana_libros)
        inputISBN.pack()
        inputTitulo=tk.Entry(ventana_libros)
        inputTitulo.pack()
        inputAutor=tk.Entry(ventana_libros)
        inputAutor.pack()
        inputEjemplares=tk.Entry(ventana_libros)
        inputEjemplares.pack()
        #Funcion lambda: esta funcion se hizo por que la funcion crearLibro necesita parametros
        # y al enviarselos la funcion se ejecuta automaticamente sin esperar a que se de click en el boton
        btnRegistrarLibro = tk.Button(ventana_libros, text="Registrar Libro", command=lambda: self.crearLibro(inputISBN, inputTitulo, inputAutor, inputEjemplares))
        btnRegistrarLibro.pack()

        #Tabla con los 
        columnas=("isbn","titulo","autor","ejemplares")
        self.tabla = ttk.Treeview(ventana_libros, columns=columnas, show="headings")
        self.tabla.heading("isbn", text="ISBN")
        self.tabla.heading("titulo", text="Título")
        self.tabla.heading("autor", text="Autor")
        self.tabla.heading("ejemplares", text="Cant.")
        self.tabla.pack(pady=20, fill="both", expand=True)
        
        self.listaLibros()



    def crearLibro(self,ISBN,Titulo,Autor,Ejemplares):
        isbn=ISBN.get()
        titulo=Titulo.get()
        autor=Autor.get()
        ejemplares=Ejemplares.get()
        libro=Libro(isbn,titulo,autor,ejemplares)
        self.catalogo.agregar(libro)
        self.listaLibros()
           
    
    def listaLibros(self):
        for l in range(len(self.catalogo)):
            self.tabla.insert("", "end", values=(self.catalogo[l].titulo, self.catalogo[l].titulo, self.catalogo[l].autor, self.catalogo[l].n_ejemplares))
        
            
            

    