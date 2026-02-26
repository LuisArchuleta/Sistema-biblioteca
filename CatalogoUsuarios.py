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
        self.usuarios.append(u)

    def __getitem__(self,usuario):
        return self.usuarios[usuario]
    
    def __len__(self):
        return len(self.usuarios)
    
    def mostrarUsuarios(self):
        for usuario in self.usuarios:
            print(f"Id: {usuario.id} Nombre: {usuario.nombre}")
            