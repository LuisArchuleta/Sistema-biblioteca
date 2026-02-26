class Libro:
    def __init__(self,isbn,titulo,autor,n_ejemplares):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.n_ejemplares = int(n_ejemplares)
        print("Se ha creado el libro",self.titulo)    
    
    