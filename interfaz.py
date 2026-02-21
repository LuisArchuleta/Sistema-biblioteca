import tkinter as tk
from VentanaLibros import VentanaLibros
from CatalogoLibros import catalogoLibros
catalogo=catalogoLibros(libros=[])
ventanaMenu=tk.Tk()


ventanaMenu.title("Ventana")
ancho=ventanaMenu.winfo_screenwidth()
largo=ventanaMenu.winfo_screenheight()

ventanalibros=VentanaLibros(largo,ancho,ventanaMenu,catalogo)

ventanaMenu.geometry(f"{ancho}x{largo}+0+0")

etiqueta =tk.Label(ventanaMenu,text="Sistema bibliotecario")
etiqueta.pack(pady=20)

botonGestionar= tk.Button(ventanaMenu,text="Gestionar libros",command=ventanalibros.abrirVentana)
botonGestionar.pack(pady=20)


botonRegistrar= tk.Button(ventanaMenu,text="Registrar Usuarios")
botonRegistrar.pack(pady=20)

botonPrestDev= tk.Button(ventanaMenu,text="Prestamos y devoluciones")
botonPrestDev.pack(pady=20)

botonReportes=tk.Button(ventanaMenu,text="Realizar reportes o consultas")
botonReportes.pack(pady=20)
ventanaMenu.mainloop()

for l in catalogo:
    print(l)

