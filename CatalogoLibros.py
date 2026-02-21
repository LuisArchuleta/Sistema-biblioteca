class catalogoLibros:
    """Clase catalogoLibros: Para crear una coleccion de libros
    Input: recibe objetos tipo libros
    outuput:None
    Functions:
            agregar: Esta funcion se utiliza para...
    """

    libros=[]#Creamos una lista vacia
    def __init__(self,libros=[]):
        self.libros=libros
    
    def agregar(self,l):
        self.libros.append(l)

    def __getitem__(self,posicion):
        return self.libros[posicion]
    
    def __len__(self):
        return len(self.libros)
            