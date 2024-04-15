class Digipymon:
   
    def __init__(self, nombre, vida, ataque, nivel, tipo):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.nivel = nivel
        self.tipo = tipo

    
    def __str__(self):
        return f"Nombre: {self.nombre}\n Vida: {self.vida}\n Ataque: {self.ataque}\n Nivel: {self.nivel}\n Tipo: {self.tipo}\n"
    
    def obtener_vida(self):
        return self.vida
    
    def obtener_ataque(self):
        return self.ataque
    
    def obtener_nivel(self):
        return self.nivel
    
    def obtener_tipo(self):
        return self.tipo