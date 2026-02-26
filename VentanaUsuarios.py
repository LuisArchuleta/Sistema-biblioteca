import tkinter as tk
from Usuario import Usuario
from CatalogoLibros import catalogoLibros
from tkinter import ttk

class VentanaUsuarios:
    
    def __init__(self,ancho,largo,ventanaPrincipal,catalogo):
        self.ancho=ancho
        self.largo=largo
        self.ventanaPrincipal=ventanaPrincipal
        self.catalogo=catalogo
        

    def abrirVentana(self):
        ventana_usuarios=tk.Toplevel(self.ventanaPrincipal)
        ventana_usuarios.geometry(f"{self.ancho}x{self.largo}+0+0")
        inputID=tk.Entry(ventana_usuarios)
        inputID.pack()
        inputNombre=tk.Entry(ventana_usuarios)
        inputNombre.pack()
        #Funcion lambda: esta funcion se hizo por que la funcion crearUsuario necesita parametros
        # y al enviarselos la funcion se ejecuta automaticamente sin esperar a que se de click en el boton
        btnRegistrarLibro = tk.Button(ventana_usuarios, text="Registrar Libro", command=lambda: self.crearUsuario(inputID, inputNombre))
        btnRegistrarLibro.pack()

        #Tabla con los usuarios 
        columnas=("ID","nombre")
        self.tabla = ttk.Treeview(ventana_usuarios, columns=columnas, show="headings")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.pack(pady=20, fill="both", expand=True)    
        self.listaUsuarios()

    def crearUsuario(self,id,nombre):
        id=id.get()
        nombre=nombre.get()
        usuario=Usuario(id,nombre)
        self.catalogo.agregar(usuario)
        self.listaUsuarios()
           
    def listaUsuarios(self):
        for u in range(len(self.catalogo)):
            self.tabla.insert("", "end", values=(self.catalogo[u].id, self.catalogo[u].nombre))
        
            
            

    