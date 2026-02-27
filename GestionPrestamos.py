import datetime

class GestionPrestamos:
    def __init__(self, prestamos = None):
        if prestamos is None:
            self.prestamos = []
        else:
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
        for _, id_u_p, _ in self.prestamos:
            if id_u_p == id_usuario:
                prestamos_del_usuario += 1

        if prestamos_del_usuario >= 3:
            return "El usuario {usuario.nombre} ya tiene el máximo de 3 libros."

        # Validar duplicado
        for isbn_p, id_u_p, _ in self.prestamos:
            if isbn_p == isbn and id_u_p == id_usuario:
                return "El usuariop ya cuenta con este libro en préstamo."

        # Registro de prestamo
        fecha = str(datetime.date.today())
        registro = (isbn, id_usuario, fecha)
        self.prestamos.append(registro)
        
        # Actualizar datos
        libro.n_ejemplares = int(libro.n_ejemplares) - 1
        libro.veces_prestado += 1

        return f"Se realizo el prestamo del libro {libro.titulo} a {usuario.nombre}"

    def devolver(self, isbn, id_usuario, catalogo_l):
        for i, (isbn_p, id_u_p, fecha_p) in enumerate(self.prestamos):
            if isbn_p == isbn and id_u_p == id_usuario:
                self.prestamos.pop(i)
                libro = catalogo_l.libros.get(isbn)
                if libro:
                    libro.n_ejemplares = int(libro.n_ejemplares) + 1
                return "Devolución exitosa."
        return "No se encontró un préstamo activo con estos datos."
    
    def mostrar_prestamos_activos(self):
        if not self.prestamos:
            print("No hay préstamos activos en este momento.")
        else:
            print("\n--- Listado de Préstamos Activos ---")
            for isbn, id_u, fecha in self.prestamos:
                print(f"ISBN: {isbn:<15} | Usuario ID: {id_u:<10} | Fecha: {fecha:<12}")