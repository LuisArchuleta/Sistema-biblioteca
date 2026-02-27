from Libro import Libro

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
    
    def crearLibros(self):
        isbn = input("ISBN: ")
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        n_ejemplares = input("Numero de ejemplares: ")
        libro = Libro(isbn,titulo,autor,n_ejemplares)
        self.agregar(libro)


    def top_3_libros(self):
        libros_ordenados = sorted(self.libros.values(), key=lambda x: x.veces_prestado, reverse=True)
        return libros_ordenados[:3]
    
    def buscar_por_autor(self, autor):
        encontrados = []
        for l in self.libros.values():
            if l.autor.lower() == autor.lower():
                encontrados.append(l)
        return encontrados
    
    def buscar_por_titulo(self, titulo):
        encontrados = []
        for l in self.libros.values():
            if l.titulo.lower() == titulo.lower():
                encontrados.append(l)
        return encontrados

    def libros_por_autor(self):
        autor = input("\nEscriba el nombre del autor: ")
        resultados = self.buscar_por_autor(autor)
        if resultados:
            for l in resultados:
                print(f"\nTítulo: {l.titulo} | ISBN: {l.isbn} | Disponibles: {l.n_ejemplares}")
        else:
            print("No se encontraron libros de ese autor.")

    def libros_por_titulo(self):
        titulo = input("\nEscriba el titulo del libro: ")
        resultados = self.buscar_por_titulo(titulo)
        if resultados:
            for l in resultados:
                print(f"\nTítulo: {l.titulo} | ISBN: {l.isbn} | Disponibles: {l.n_ejemplares}")
        else:
            print("No se encontro el libro.")
