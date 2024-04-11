class Inventario:
    def __init__(self):
        self.objetos = {}
        
    def añadir_objeto(self, nombre, cantidad):
        if nombre in self.objetos:
            self.objetos[nombre] += cantidad  # Si el objeto ya existe, se suma la cantidad
        else:
            self.objetos[nombre] = cantidad  # Si el objeto no existe, se añade al diccionario
            
    def usar_objeto(self, usar_objeto):
        if objeto in self.objetos:
            self.objetos[objeto] -= 1
            if self.objetos[objeto] == 0:
                del self.objetos[objeto]
            print(f"Se ha usado un/a {objeto}")
        else:
            print(f"No tienes {objeto} en tu inventario")
    