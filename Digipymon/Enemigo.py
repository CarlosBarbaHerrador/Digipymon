class Enemigo:
    def __init__(self, nombre ):
        self.nombre = nombre
        
    def __init__(self):
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        
    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.append(digipymon)  # Añadir el digipymon a la lista
        self.cantidad_digipymon += 1  # Aumentar la cantidad de Digimon en 1
        
        