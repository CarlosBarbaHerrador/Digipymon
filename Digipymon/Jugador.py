class Jugador:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_digipymon = [] #instanciada a una lista vacía
        self.cantidad_digipymon = 0
        self.digicoins = 10

    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.append(digipymon)  # Añadir el digipymon a la lista
        self.cantidad_digipymon += 1  # Aumentar la cantidad de Digimon en 1
        
    def consultar_digipymon(self):
        print("Tienes un total de:", self.cantidad_digipymon, "Digipymons\n")
        for digipymon in self.lista_digipymon:
            print(digipymon)
        
    def consultar_digicoins(self):
        return self.digicoins  # Imprimir la cantidad de Digicoins
