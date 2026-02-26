class catalogoUsuarios:
    """Clase catalogoUsuarios: Para crear una coleccion de Usuarios
    Input: recibe objetos tipo Usuario
    outuput:None
    Functions:
            agregar: Esta funcion se utiliza para...
    """

    usuarios=[]#Creamos una lista vacia
    def __init__(self,usuarios=[]):
        self.usuarios=usuarios
    
    def agregar(self,u):
        self.libros.append(u)

    def __getitem__(self,usuario):
        return self.libros[usuario]
    
    def __len__(self):
        return len(self.usuarios)
            