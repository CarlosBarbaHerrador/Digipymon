import random
class ListaNombres:
    def __init__(self):
        self.lista_nombre_digipymon = ["Antoniopymon", "Paupymon", "Estebanpymon", "Alexpymon", "Becapymon", "Charpymon", "Bulbapymon", "Squirtlepymon", "Pikapymon", "Jigglypuffpymon", "Geodudepymon", "Eeveepymon", "Snorlaxpymon", "Psyduckpymon", "Gengarpymon", "Lucariopymon", "Mewtwopymon", "Torchicpymon", "Mudkipymon", "Pipluppymon", "Chimcharpymon", "Turtwigpymon", "Treeckopymon", "Torchpymon", "Mudpymon", "Leafeonpymon", "Glaceonpymon", "Vaporeonpymon", "Jolteonpymon", "Flareonpymon", "Sylveonpymon", "Espeopymon", "Umbreopymon", "Jolteopymon", "Glacpymon", "Flareopymon", "Sylveopymon", "Espypymon", "Umbrepymon", "Joltapymon", "Glacipymon", "Flarepymon", "Sylveepymon", "Espypymon", "Umbreonpymon", "Garchompymon", "Rayquazapymon", "Kyogrepymon", "Groudopymon", "Dialgapymon"]
        self.lista_nombre_entrenador = ["Pedro", "Antonio", "Juan", "María", "Luis", "Ana", "Carlos", "Laura", "Miguel", "Elena", "Sara", "David", "Isabel", "Javier", "Sofía", "Daniel", "Lucía", "Fernando", "Carmen", "Diego", "Patricia", "Manuel", "Rosa", "José", "Marta", "Jorge", "Paula", "Pablo", "Eva", "Francisco", "Silvia", "Álvaro", "Natalia", "Raúl", "Cristina", "Rubén", "Beatriz", "Iván", "Mercedes", "Adrián", "Nerea", "Alejandro", "Victoria", "Alberto", "Verónica"]
    
    def obtener_nombre_digipymon(self):
        return random.choice(self.lista_nombre_digipymon)
    
    def obtener_nombre_entrenador(self):
        return random.choice(self.lista_nombre_entrenador)