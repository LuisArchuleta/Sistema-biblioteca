class catalogoLibros:
    """Clase catalogoLibros: Para crear una coleccion de libros
    Input: recibe objetos tipo libros
    outuput:None
    Functions:
            agregar: Esta funcion se utiliza para...
    """

    def __init__(self,libros = {}):
        self.libros=libros
    
    def agregar(self,l):
        self.libros[l.isbn] = l


    def mostrarDisponibilidad(self):
        if len(self.libros)==0:
            print("No hay libros registrados")
        else:
            for libro in self.libros.values():
                print(f"Libro: {libro.titulo} Ejemplares disponibles: {libro.n_ejemplares}")