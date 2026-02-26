

class catalogoUsuarios:
    """Clase catalogoUsuarios: Para crear una coleccion de Usuarios
    Input: recibe objetos tipo Usuario
    outuput:None
    Functions:
            agregar: Esta funcion se utiliza para...
    """
    
    def __init__(self,id,usuarios = {}):
        self.id=id
        self.usuarios = usuarios
    
    def agregar(self,u):
        self.id+=1
        self.usuarios[self.id]=u

    def __getitem__(self,usuario):
        return self.usuarios[usuario]
    
    def __len__(self):
        return len(self.usuarios)
    
    def mostrarUsuarios(self):
        for usuario in self.usuarios:
            print(f"Id: {self.id} Nombre: {usuario.nombre}")
            