class Usuario:
    def __init__(self,id,nombre):
        self.id=id;
        self.nombre=nombre;
    
    def __str__(self):
        return f"Id: {self.id} Nombre: {self.nombre}"
