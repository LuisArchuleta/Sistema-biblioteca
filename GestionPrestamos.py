import datetime

class GestionPrestamos:
    def __init__(self, prestamos = []):
        self.prestamos = prestamos 

    def realizar_prestamo(self, isbn, id_usuario, catalogo_l, catalogo_u):
        libro = catalogo_l.libros.get(isbn)
        usuario = catalogo_u.usuarios.get(id_usuario)

        # Reglas
        if not libro or not usuario:
            return "Error: Datos no encontrados."
        
        if int(libro.n_ejemplares) <= 0:
            return "No hay ejemplares disponibles."

        # Contar préstamos actuales del usuario
        prestamos_del_usuario = 0
        for p in self.prestamos:
            if p[1] == id_usuario:
                prestamos_del_usuario += 1

        if prestamos_del_usuario >= 3:
            return "El usuario ya tiene el máximo de 3 libros."

        # Validar duplicado
        for p in self.prestamos:
            if p[0] == isbn and p[1] == id_usuario:
                return "Ya tiene este libro prestado."

        # Registro de prestamo
        fecha = str(datetime.date.today())
        registro = (isbn, id_usuario, fecha)
        self.prestamos.append(registro)
        
        # Actualizar datos
        int(libro.n_ejemplares) -= 1
        libro.veces_prestado += 1

        return f"Se realizo el prestamo {libro.titulo} a {usuario.nombre}"

    def devolver(self, isbn, id_usuario, catalogo_l):
        for i, p in enumerate(self.prestamos):
            if p[0] == isbn and p[1] == id_usuario:
                self.prestamos.pop(i)
                catalogo_l.libros[isbn].n_ejemplares += 1
                return "Devolución exitosa."
        return "No se encontró el préstamo."