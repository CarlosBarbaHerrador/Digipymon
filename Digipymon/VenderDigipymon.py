import random, os, time
from Jugador import Jugador
class VenderDigipymon:
    #TODO ============================= FUNCION VENDER DIGIYMON ======================================
    def vender_digipymon(self, jugador):
       
        # Muestra los Digipymons disponibles para vender.
        print("Digipymons disponibles:")
        
        # Comprueba si el jugador tiene Digipymons en su lista.
        if not jugador.lista_digipymon:
            print("No tienes Digipymons para vender.")
            return
        
        # Imprime todos los Digipymons con sus respectivas estadísticas de vida.
        for i, digipymon in enumerate(jugador.lista_digipymon):
            print(f"{i+1}. {digipymon.nombre}, vida: {digipymon.vida}")
            
        # Solicita al jugador que elija el número del Digipymon que desea vender.
        seleccion_digipymon = int(input("Elige el número del Digipymon al que deseas vender: ")) - 1
        
        # Verifica si la selección del jugador es válida.
        if 0 <= seleccion_digipymon < len(jugador.lista_digipymon):
            
            # Pregunta al jugador cómo quiere vender el Digipymon (por partes o entero).
            metodo_venta = input("\n¿Cómo quieres venderlo?\n1. Por partes\n2. Entero\n")
            
            # Si el jugador elige vender por partes:
            if metodo_venta == "1":
                # Solicita al jugador que elija qué parte del Digipymon quiere vender.
                print("\n¿Qué parte quieres vender?")
                print("1. Brazo (Perderá daño a cambio de dinero)")
                print("2. Pierna (Perderá vida a cambio de dinero)")
                print("3. Cola (Perderá daño y vida a cambio de mucho dinero)")
                print("")
                parte = input()
                
                # Si el jugador elige vender el brazo:
                if parte == "1":
                    # Calcula el dinero a recibir y actualiza las estadísticas del Digipymon.
                    ataque_anterior = jugador.lista_digipymon[seleccion_digipymon].ataque
                    jugador.lista_digipymon[seleccion_digipymon].ataque = round(ataque_anterior / 2)
                    dinero = round(ataque_anterior / 2)
                    jugador.digicoins += dinero
                    
                    # Muestra mensajes sobre la transacción.
                    print(f"Tu Digipymon ha perdido puntos de ataque (antes: {ataque_anterior}, ahora: {jugador.lista_digipymon[seleccion_digipymon].ataque}).")
                    print(f"Has ganado {dinero} Digicoins.")
                    print(f"Tus Digicoins totales ahora son: {jugador.digicoins}")
                    print(f"Has vendido el brazo de {jugador.lista_digipymon[seleccion_digipymon].nombre}.")
                    
                # Si el jugador elige vender la pierna:
                elif parte == "2":
                    # Calcula el dinero a recibir y actualiza las estadísticas del Digipymon.
                    vida_anterior = jugador.lista_digipymon[seleccion_digipymon].vida
                    jugador.lista_digipymon[seleccion_digipymon].vida = round(vida_anterior / 2)
                    dinero = round(vida_anterior / 3)
                    jugador.digicoins += dinero

                    # Muestra mensajes sobre la transacción.
                    print(f"Tu Digipymon ha perdido puntos de vida (antes: {vida_anterior}, ahora: {jugador.lista_digipymon[seleccion_digipymon].vida}).")
                    print(f"Has ganado {dinero} Digicoins.")
                    print(f"Tus Digicoins totales ahora son: {jugador.digicoins}")
                    print(f"Has vendido la pata de {jugador.lista_digipymon[seleccion_digipymon].nombre}.")
                    
                    if jugador.lista_digipymon[seleccion_digipymon].vida <= 0:
                        print(f"Has matado a {jugador.lista_digipymon[seleccion_digipymon].nombre}")
                        jugador.lista_digipymon.pop(seleccion_digipymon)
                        jugador.cantidad_digipymon -= 1
                        
                    
                # Si el jugador elige vender la cola:
                elif parte == "3":
                    # Calcula el dinero a recibir y actualiza las estadísticas del Digipymon.
                    ataque_anterior = jugador.lista_digipymon[seleccion_digipymon].ataque
                    jugador.lista_digipymon[seleccion_digipymon].ataque = round(ataque_anterior / 2)
                    vida_anterior = jugador.lista_digipymon[seleccion_digipymon].vida
                    jugador.lista_digipymon[seleccion_digipymon].vida = round(vida_anterior / 2)
                    dinero = round(vida_anterior / 3 + ataque_anterior / 2)
                    jugador.digicoins += dinero
        
                    # Muestra mensajes sobre la transacción.
                    print(f"Tu Digipymon ha perdido puntos de vida y ataque.")
                    print(f"Has ganado {dinero} Digicoins.")
                    print(f"Tus Digicoins totales ahora son: {jugador.digicoins}")
                    print(f"Has vendido la cola de {jugador.lista_digipymon[seleccion_digipymon].nombre}.")
                    
                else:
                    # Si el jugador elige una opción no válida, muestra un mensaje de error.
                    print("Opción no válida.")
                    
            # Si el jugador elige vender el Digipymon entero:
            elif metodo_venta == "2":
                # Calcula el dinero a recibir y elimina el Digipymon de la lista del jugador.
                vida_dinero = jugador.lista_digipymon[seleccion_digipymon].vida
                ataque_dinero = jugador.lista_digipymon[seleccion_digipymon].ataque
                nivel_dinero = jugador.lista_digipymon[seleccion_digipymon].nivel
                dinero = vida_dinero + ataque_dinero + nivel_dinero
                    
                jugador.digicoins += dinero
                    
                jugador.lista_digipymon.pop(seleccion_digipymon)
                jugador.cantidad_digipymon -= 1
                # Muestra mensajes sobre la transacción.
                print(f"Has ganado {vida_dinero} por la vida")
                print(f"Has ganado {ataque_dinero} por el ataque")
                print(f"Has ganado {nivel_dinero} por el nivel")
                print(f"En total has ganado {dinero} Digicoins")
                    
            else:
                # Si el jugador elige una opción no válida, muestra un mensaje de error.
                print("Opción no válida.")
                    
        else:
            # Si el jugador elige un número de Digipymon no válido, muestra un mensaje de error.
            print("Número de Digipymon seleccionado no válido.")