import random, os, time
from Jugador import Jugador
class Casino:
    #TODO ================================  FUNCION CASINO  ==========================================
    def casino(self, jugador):
        #jugador = Jugador("*")
        print("BIENVENIDO AL CASINO DE DIGIPYMON!! AQUI PODRAS GANAR DINERO O PERDERLO")
        print("PASALO BIEN Y RESPETA LAS NORMAS!!\n")
        
        while True:
            # Menú principal del casino
            print("╔═══════════════════════════════════════╗")
            print("║         ¡Bienvenido al Casino!        ║")
            print("╠═══════════════════════════════════════╣")
            print("║           Seleccione un juego:        ║")
            print("║           1. Lanzamiento de dados     ║")
            print("║           2. Ruleta                   ║")
            print("║           3. Tombola                  ║")
            print("║           4. Salir                    ║")
            print("╚═══════════════════════════════════════╝")
            opcion_casino = input("Ingrese el número del juego que desea jugar: ")
            
            if opcion_casino == "1":
                # Juego de lanzamiento de dados
                if jugador.digicoins <= 0:
                    print("Lo siento, no tienes suficientes Digicoins para jugar.")
                    continue
                
                os.system("cls")
                print("Estás jugando al lanzamiento de dados!!")
                print("Si la suma de los dados es mayor que 7, ¡ganarás!")
                
                # Pedir al jugador que ingrese la cantidad de apuesta
                while True:
                    pago = int(input("Ingrese la cantidad que desea apostar: "))
                    if pago <= 0:
                        print("Por favor, ingrese una cantidad válida mayor que 0.")
                    elif pago > jugador.digicoins:
                        print("Lo siento, no tienes suficientes Digicoins para realizar esa apuesta.")
                    else:
                        break
                    
                jugador.digicoins -= pago
                
                # Simulación del lanzamiento de dados
                print("Lanzando dados", end=" ")
                for _ in range(3):
                    print(".", end=" ", flush=True)
                    time.sleep(1)  # Pausa de 1 segundo entre cada punto suspensivo
                
                print("")
                dado1 = random.randint(1, 6)
                dado2 = random.randint(1, 6)
                print("\nHas lanzado los dados y obtuviste:", dado1, "y", dado2)
                suma_dados = dado1 + dado2
                print("La suma de los dados es:", suma_dados)
                
                # Determinar el resultado del juego
                if suma_dados > 7:
                    jugador.digicoins += pago * 2
                    print("¡Felicidades! Has ganado", pago * 2 ,"Digicoins")
                else:
                    print("Lo siento, no has ganado esta vez.")
                    
            elif opcion_casino == "2":
                # Juego de ruleta
                os.system("cls")
                print("Bienvenido a la RULE de DIGIPYMON!!!")
                print("Actualmente tienes", jugador.digicoins, "DIGICOINS\n")
                opciones_ruleta = ["Rojo", "Negro", "Verde","Rojo","Rojo","Rojo","Rojo","Rojo","Rojo","Rojo","Rojo","Rojo","Rojo","Rojo","Rojo","Negro","Negro","Negro","Negro","Negro","Negro","Negro","Negro","Negro","Negro","Negro","Negro","Negro","Negro","Negro","Negro","Negro",]
                opcion_rule = random.choice(opciones_ruleta).lower()
                print("Si aciertas el color GANARAS!!!")
                print("Negro = 56,35% ---> x2 ganancia")
                print("Rojo = 40,63% ----> x3 ganancia")
                print("Verde = 3,13% ----> x10 ganancia")
                color = str(input("\nA que color quieres apostar?? (Escribe el color a apostar): \n")).lower()
                
                # Pedir al jugador que ingrese la cantidad de apuesta
                pago = int(input("Ingrese la cantidad que desea apostar: \n"))
                
                if pago <= 0:
                    print("\nPor favor, ingrese una cantidad válida mayor que 0.\n")
                    continue
                elif pago > jugador.digicoins:
                    print("\nLo siento, no tienes suficientes Digicoins para realizar esa apuesta.\n")
                    continue
                
                jugador.digicoins -= pago
                os.system("cls")
                # Simulación del giro de la ruleta
                print("Girando la ruleta", end=" ")
                for _ in range(3):
                    print(".", end=" ", flush=True)
                    time.sleep(1)  
                print("\nLa ruleta ha girado y el color ganador es:", opcion_rule)
                
                # Determinar el resultado del juego
                if opcion_rule == "verde" and color == "verde":
                    jugador.digicoins += pago * 10
                    print("¡Felicidades! Has acertado el color verde y has ganado", pago * 10 ,"Digicoins")
                elif opcion_rule == "negro" and color == "negro":
                    jugador.digicoins += pago * 2
                    print("¡Felicidades! Has acertado el color y has ganado", pago * 2 ,"Digicoins")
                elif opcion_rule == "rojo" and color == "rojo":
                    jugador.digicoins += pago * 3
                    print("¡Felicidades! Has acertado el color y has ganado", pago * 3 ,"Digicoins")
                else:
                    print("No has escrito bien el color y te has quedado sin dinero jajajaja")
                    
            elif opcion_casino == "3":
                # Juego de tombola
                os.system("cls")
                print("Bienvenido a la tombolaaaaaaaaa, donde puedes ganar una gran cantidad de premios aleatoriooos")
                print("╔════════════════ PREMIOS O CASTIGOS ═════════════════╗")
                print("║                                                     ║")
                print("║  1. Mejora de stats a tu Digipymon                  ║")
                print("║  2. Bajada de stats a tu Digipymon                  ║")
                print("║  3. Digicoins                                       ║")
                print("║  4. Pierdes Digicoins                               ║")
                print("║  5. Un nuevo Digipymon                              ║")
                print("║  6. Pierdes un Digipymon                            ║")
                print("║                                                     ║")
                print("╚═════════════════════════════════════════════════════╝")
                
                # Permitir al jugador tirar la tombola
                tirar = input("Quieres hacer girar la tombola?? (Cuesta 10 DIGICOINS) (SI/NO)\n").lower()
                if tirar == "si" and jugador.digicoins >= 10:
                    opciones_tombola = ["Mejora de stats a tu Digipymon","Bajada de stats a tu Digipymon","Digicoins","Pierdes Digicoins","Un nuevo Digipymon","Pierdes un Digipymon" ]
                    opcion_tombo = random.choice(opciones_tombola).lower()
                    os.system("cls")
                    
                    print("\nGirando tombola", end=" ")
                    for _ in range(3):
                        print(".", end=" ", flush=True)
                        time.sleep(1)  # Pausa de 1 segundo entre cada punto suspensivo
                        
                    print("\nY ha tocacado...",opcion_tombo ,"!!!!\n")
                    
                    # Determinar el premio o castigo y aplicar las consecuencias
                    if opcion_tombo == "mejora de stats a tu digipymon":
                        # Mejora las estadísticas del primer Digipymon
                        jugador.lista_digipymon[0].vida += 10    
                        jugador.lista_digipymon[0].ataque += 5  
                        print("La vida de ", jugador.lista_digipymon[0].nombre, "a subido 10 puntos!!")
                        print("El ataque de ", jugador.lista_digipymon[0].nombre, "a subido 5 puntos!!")
                    elif opcion_tombo == "bajada de stats a tu digipymon":
                        # Reduce las estadísticas del primer Digipymon
                        jugador.lista_digipymon[0].vida -= 10    
                        jugador.lista_digipymon[0].ataque -= 5  
                        print("La vida de ", jugador.lista_digipymon[0].nombre, "a bajado 10 puntos!!")
                        print("El ataque de ", jugador.lista_digipymon[0].nombre, "a bajado 5 puntos!!")
                        print("Mas suerte la proxima vez!!")
                    elif opcion_tombo == "digicoins":
                        # Otorga 30 Digicoins al jugador
                        jugador.digicoins += 30
                        print("Has ganado 30 DIGICOINS!!!")
                    elif opcion_tombo == "pierdes digicoins":
                        # Reduce los Digicoins del jugador a 0
                        jugador.digicoins = 0
                        print("Has perdido TODAS tus DIGICOINS!!!")
                        print("Tu cuenta ha bajado a 0 DIGICOINS, te has arruinado!!")
                        print("Apostar no es lo tuyo")
                    elif opcion_tombo == "un nuevo digipymon":
                        # Agrega un nuevo Digipymon al inventario del jugador si no tiene el máximo
                        print("Has ganado un nuevo compañero de aventuras!!")
                        if jugador.cantidad_digipymon >= 6:
                            print("Lo siento ya tienes el máximo de digipymons")
                        else:
                            digipymon_tombo = generar_digipymon_aleatorio()
                            jugador.añadir_digipymon(digipymon_tombo)
                            print(digipymon_tombo)
                    elif opcion_tombo == "pierdes un digipymon":
                        # Elimina un Digipymon del inventario del jugador
                        jugador.lista_digipymon.remove(digipymon_jugador)
                        print("Uno de tus digipymons ha desaparecido de tu inventario!!")
                        print("No lo busques en el mercado negro (estará por piezas)")
                        print("Siento tu pérdida")
                    else:
                        print("Opción no válida")
                elif jugador.digicoins < 10:
                    print("Dinero insuficiente")
                else:
                    print("VUELVA PRONTO!!")    
            elif opcion_casino == "4":
                print("Gracias por jugar en el casino. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, elige 1, 2 o 3.")