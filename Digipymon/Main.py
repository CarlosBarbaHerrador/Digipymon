import random, os, time
from ListaNombres import ListaNombres
from Jugador import Jugador
from Enemigo import Enemigo
from Inventario import Inventario
from Digipymon import Digipymon

#TODO ============================ GENERAR DIGIPYMON ALEATORIO ===================================
def generar_digipymon_aleatorio():
    lista = ListaNombres()
    #Genera el tipo del digipymon de manera aleatoria del array
    tipos = ["Planta", "Fuego", "Agua"]
    tipo_seleccionado = random.choice(tipos)
    
    # Genera un nombre aleatorio proveniente de la clase ListaNombres
    nombre_aleatorio = lista.obtener_nombre_digipymon()
    
    #Genera estadisticas aleatorias (Vida,Ataque,Nivel)
    numero_aleatorio_vida = random.randint(10,20)
    numero_aleatorio_ataque = random.randint(1,10)
    numero_aleatorio_nivel = random.randint(1,3)
    
    #Selecciona los parametros
    digipymon = Digipymon(nombre_aleatorio, numero_aleatorio_vida, numero_aleatorio_ataque, numero_aleatorio_nivel, tipo_seleccionado)
    
    return digipymon

#TODO =====================================  MENU  ===============================================
def menu():
    print("---------------DIGIPYMON!---------------")
    print("****************************************")
    print("1. Buscar Digipymon")
    print("2. Luchar contra un entrenador")
    print("3. Ir a la tienda")
    print("4. Usar objetos")
    print("5. Consultar inventario")
    print("6. Consultar Digipymons")
    print("7. Casino")
    print("8. Salir")
    print("****************************************")
    operacion = int(input())
    return operacion

#TODO ================================= BUSCAR DIGIPYMON  ========================================
def buscar_digipymon(jugador, inventario):
    
    print("Estas buscando digipymons en tu zona", end=" ")
    for _ in range(3):
        print(".", end=" ", flush=True)
        time.sleep(1)  # Pausa de 1 segundo entre cada punto suspensivo
        
    print()
    digipymon_encontrado = generar_digipymon_aleatorio()
    print(digipymon_encontrado)
    
    # Calcula la probabilidad de captura 100-nivel*10
    probabilidad_captura = 100 - (digipymon_encontrado.obtener_nivel() * 10)
    
    # Muestra la probabilidad de captura al jugador
    print(f"La probabilidad de capturar este Digipymon es del {probabilidad_captura}%.\n")
   
    # Verifica si la clave 'balls' está presente en el diccionario 'inventario.objetos'
    if 'balls' in inventario.objetos:
        balls_disponibles = inventario.objetos['balls']
        Captura = str(input("¿Quieres intentar capturarlo? Te quedan " + str(balls_disponibles) + " balls   Si/No\n"))

        texto_captura = Captura.lower()

        # comprueba si tienes balls y quieres capturarlo
        if texto_captura == "si" and inventario.objetos['balls'] > 0 and jugador.cantidad_digipymon < 6:

            # Realiza el intento de captura 
            if random.randint(1, 100) <= probabilidad_captura:
                jugador.añadir_digipymon(digipymon_encontrado)
                print("¡Has capturado al Digipymon!")
                print("")
                inventario.objetos["balls"] -= 1
            else:
                print("El Digipymon ha escapado.")
                inventario.objetos["balls"] -= 1
        # Si tienes más de 6 digipymons no te dejará
        elif jugador.cantidad_digipymon >= 6:
            print("Ya tienes 6 digipymons!!")

        elif inventario.objetos['balls'] <= 0:
            print("No tienes bolas jaja\n")
        
        else:
            print("Has huido del Digipymon!! Un poco cobarde por tu parte 🐓🐓🐓")
    else:
        print("Estas intentando capturar digipymons sin balls?? En serio??\n")

#TODO ================================  FUNCION COMBATE  =========================================
def combate(jugador, enemigo):
    lista = ListaNombres()
    ronda_ganada = 0
    ronda_perdida = 0
    nombre_aleatorio_entrenador = lista.obtener_nombre_entrenador()
    
    print("Si evitas la pelea perderás 1 Digicoin")
    peleita = str(input("¿Estás seguro de querer combatir? Si/No\n"))
    pelea = peleita.lower()
    # Bucle para agregar los Digipymons del jugador al enemigo
    for _ in range(jugador.cantidad_digipymon):
            digipymon_entrenador = generar_digipymon_aleatorio()
            enemigo.añadir_digipymon(digipymon_entrenador)
    if pelea == "si":
        os.system("cls")
        print("Te has encontrado a:",nombre_aleatorio_entrenador ,"Preparate para luchar!!")
        print("")
        # Bucle para agregar los Digipymons del jugador al enemigo (Lo pongo de nuevo para que actualice los digipymons que ha capturado en la ronda anterior en jugador)
        for _ in range(jugador.cantidad_digipymon):
            digipymon_entrenador = generar_digipymon_aleatorio()
            enemigo.añadir_digipymon(digipymon_entrenador)
     

        if jugador.cantidad_digipymon == 0:
            print("No tienes Digipymons para combatir.")
            
        else:
            
            # Itera sobre los Digipymons del jugador y del enemigo
            for i in range(min(jugador.cantidad_digipymon, enemigo.cantidad_digipymon)):
                if i < len(jugador.lista_digipymon) and i < len(enemigo.lista_digipymon):
                    digipymon_jugador = jugador.lista_digipymon[i]
                    digipymon_enemigo = enemigo.lista_digipymon[i]
                    
                    # Compara los ataques de los Digipymons
                    if digipymon_jugador.ataque > digipymon_enemigo.ataque:
                        # El jugador gana el combate
                        print("¡Tu Digipymon ha ganado el combate!")
                        diferencia_ataque = digipymon_jugador.ataque - digipymon_enemigo.ataque
                        enemigo.lista_digipymon.remove(digipymon_enemigo)
                        ronda_ganada += 1
                        
                        if digipymon_enemigo.vida <= 0:
                            print("¡El Digipymon enemigo ha sido derrotado!(Debilitado)")
                            enemigo.lista_digipymon.remove(digipymon_enemigo)
                            enemigo.cantidad_digipymon -= 1
                            ronda_ganada += 1
                                  
                    elif digipymon_jugador.ataque < digipymon_enemigo.ataque:
                        # El jugador pierde el combate
                        print("¡Tu Digipymon ha perdido el combate!")
                        diferencia_ataque = digipymon_enemigo.ataque - digipymon_jugador.ataque
                        digipymon_jugador.vida -= diferencia_ataque
                        ronda_perdida += 1 
                        enemigo.lista_digipymon.remove(digipymon_enemigo)
                        if digipymon_jugador.vida <= 0:
                            print("¡Tu Digipymon ha sido derrotado!(Debilitado)")
                            jugador.lista_digipymon.remove(digipymon_jugador)
                            jugador.cantidad_digipymon -= 1
                            
                    else:
                        # Empate, ambos Digipymons pierden vida
                        print("¡El combate ha terminado en empate!")
                        diferencia_ataque = 0  # No hay diferencia de ataque en caso de empate
                        digipymon_jugador.vida -= diferencia_ataque
                        digipymon_enemigo.vida -= diferencia_ataque
                        enemigo.lista_digipymon.remove(digipymon_enemigo)
                        
                        if digipymon_jugador.vida <= 0:
                            print("¡Tu Digipymon ha sido derrotado!")
                            jugador.lista_digipymon.remove(digipymon_jugador)
                            jugador.cantidad_digipymon -= 1
                            
                        if digipymon_enemigo.vida <= 0:
                            print("¡El Digipymon enemigo ha sido derrotado!")
                            enemigo.lista_digipymon.remove(digipymon_enemigo)
                            enemigo.cantidad_digipymon -= 1
                    
                    print("         ", "Tu","/","Enemigo")
                    print("Marcador: ", ronda_ganada ,"/", ronda_perdida)
                    print("----------------------------------------")
                
            # si ganas te da dinero y si pierdes te lo quita
            if ronda_ganada > ronda_perdida:
                print("----------------------------------------")
                print("Has derrotado a:", nombre_aleatorio_entrenador)
                print("Has recibido", ronda_ganada, "Digicoins por ganar")
                print("----------------------------------------")
                jugador.digicoins += ronda_ganada
            elif ronda_ganada < ronda_perdida:
                print("----------------------------------------")
                print("Has sido derrotado por:", nombre_aleatorio_entrenador)
                print("Has perdido", ronda_perdida, "Digicoins por perder")
                print("----------------------------------------")
                #se asegura que no puedas tener dinero negativo
                if jugador.digicoins > ronda_perdida:
                    jugador.digicoins -= ronda_perdida
                elif jugador.digicoins < ronda_perdida:
                    jugador.digicoins = 0
                    print("Eres tan pobre que no puedes perder un diero que no tienes")
                else:
                    print("Eres tan pobre que no puedes perder un diero que no tienes")
            else:
                print("----------------------------------------")
                print("Has empatado con:", nombre_aleatorio_entrenador)
                print("Al empatar no pierdes ni ganas digicoins")
                print("----------------------------------------")
             # Después de cada combate, muestra el estado actual de los Digipymons del jugador

                
                
    elif pelea == "no":
        print("Te has escondido para que el entrenador no te vea!!")
        print("Al esconderte se te ha caído una moneda al suelo!!")
        print("¡Qué cobarde eres! 🐓🐓")
        jugador.digicoins -= 1
    else:
        print("Comando inválido. Por favor, responde 'Si' o 'No'.")
       
#TODO ===============================  FUNCION DIGISHOP  =========================================
def digishop(jugador, inventario):
    print("╔═════════════════════════════════════════════════════════════════════════════╗")
    print("║                            ¡Bienvenido al Digishop!                         ║")
    print("║                                                                             ║")
    print("║                           Catálogo de la tienda:                            ║")
    print("║                                                                             ║")
    print("║ 1. Digipyballs:     5 digicoins                                             ║")
    print("║                                                                             ║")
    print("║ 2. Poción:          3 digicoins (restaura 10 puntos de vida)                ║")
    print("║                                                                             ║")
    print("║ 3. Anabolizantes:   4 digicoins (aumenta 5 puntos de ataque)                ║")
    print("║                                                                             ║")
    print("║ ¡Haz tus compras y prepárate para la batalla!                               ║")
    print("╚═════════════════════════════════════════════════════════════════════════════╝")
    
    # Obtener la selección del jugador
    print("")
    seleccion = input("¿Qué ítem deseas comprar? (1/2/3): ")
    print("")
    
    # Comprobar si el jugador tiene suficientes digicoins
    if jugador.digicoins <= 0:
        print("¡No tienes suficientes digicoins para comprar ningún ítem!")
        return
    
    # Realizar la compra según la selección del jugador
    if seleccion == '1':
        if jugador.digicoins >= 5:
            jugador.digicoins -= 5
            inventario.añadir_objeto("balls", 1)
            print("¡Has comprado Digipyballs! Ahora tienes {}.".format(inventario.objetos['balls']))
        else:
            print("¡No tienes suficientes digicoins para comprar Digipyballs!")
    elif seleccion == '2':
        if jugador.digicoins >= 3:
            jugador.digicoins -= 3
            inventario.añadir_objeto("pocion", 1)
            print("¡Has comprado una Poción! Por 3 Digicoins.")
        else:
            print("¡No tienes suficientes digicoins para comprar una Poción!")
    elif seleccion == '3':
        if jugador.digicoins >= 4:
            jugador.digicoins -= 4
            inventario.añadir_objeto("anabolizantes", 1)
            print("¡Has comprado Anabolizantes! Por 4 Digicoins")
        else:
            print("¡No tienes suficientes digicoins para comprar Anabolizantes!")
    else:
        print("Selección no válida. Por favor, elige '1', '2' o '3'.")

#TODO ==============================  FUNCION USAR OBJETO  =======================================
def usar_item(jugador, inventario):
    # Muestra el inventario
    print("--------INVENTARIO--------")
    for objeto, cantidad in inventario.objetos.items():
        print(f"{objeto}: {cantidad}")
    print("--------------------------")
    
    # Pregunta al jugador qué ítem desea usar
    seleccion = input("¿Qué ítem deseas usar? (Escribe nombre del item)").capitalize()
    
    # Verifica si el ítem seleccionado está en el inventario y realiza la acción correspondiente
    if seleccion == "Pocion":
        if "pocion" in inventario.objetos and inventario.objetos["pocion"] > 0:
            
            # Muestra los Digipymons disponibles
            print("Digipymons disponibles:")
            
            for i, digipymon in enumerate(jugador.lista_digipymon):
                print(f"{i+1}. {digipymon.nombre},vida: {digipymon.vida}")
            # Pide al jugador que elija un Digipymon
            seleccion_digipymon = int(input("Elige el número del Digipymon al que deseas aplicar la poción: ")) - 1
            
            if 0 <= seleccion_digipymon < len(jugador.lista_digipymon):
                
                # Aumenta la vida del Digipymon seleccionado en 10 puntos
                jugador.lista_digipymon[seleccion_digipymon].vida += 10
                
                # Reduce en 1 la cantidad de pociones en el inventario
                inventario.objetos["pocion"] -= 1
                print("¡Has usado una Poción! La vida de", jugador.lista_digipymon[seleccion_digipymon].nombre, "se ha aumentado en 10 puntos.")
                
            else:
                print("¡Número de Digipymon no válido!")
                
        else:
            print("¡No tienes pociones en tu inventario!")
            
    elif seleccion == "Anabolizantes":
        
        if "anabolizantes" in inventario.objetos and inventario.objetos["anabolizantes"] > 0:
            
            # Muestra los Digipymons disponibles
            print("Digipymons disponibles:")
            
            for i, digipymon in enumerate(jugador.lista_digipymon):
                print(f"{i+1}. {digipymon.nombre},Ataque: {digipymon.ataque}")
            # Pide al jugador que elija un Digipymon
            seleccion_digipymon = int(input("Elige el número del Digipymon al que deseas aplicar los anabolizantes: ")) - 1
            
            if 0 <= seleccion_digipymon < len(jugador.lista_digipymon):
                
                # Aumenta el ataque del Digipymon seleccionado en 5 puntos
                jugador.lista_digipymon[seleccion_digipymon].ataque += 5
                
                # Reduce en 1 la cantidad de anabolizantes en el inventario
                inventario.objetos["anabolizantes"] -= 1
                print("¡Has usado Anabolizantes! El ataque de", jugador.lista_digipymon[seleccion_digipymon].nombre, "se ha aumentado en 5 puntos.")
            else:
                print("¡Número de Digipymon no válido!")
        else:
            print("¡No tienes Anabolizantes en tu inventario!")
    else:
        print("¡Ítem no válido o no disponible en tu inventario!")

#TODO ================================  FUNCION CASINO  ==========================================
def casino(jugador):
    print("BIENVENIDO AL CASINO DE DIGIPYMON!! AQUI PODRAS GANAR DINERO O PERDERLO")
    print("PASALO BIEN Y RESPETA LAS NORMAS!!\n")
    
    while True:
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
            
            if suma_dados > 7:
                jugador.digicoins += pago * 2
                print("¡Felicidades! Has ganado", pago * 2 ,"Digicoins")
            else:
                print("Lo siento, no has ganado esta vez.")
                
        elif opcion_casino == "2":
            os.system("cls")
            print("Bienvenido a la RULE de DIGIPYMON!!!")
            print("Actualmente tienes", jugador.digicoins, "DIGICOINS\n")
            opciones_ruleta = ["Rojo", "Negro", "Verde","Rojo","Rojo","Rojo","Rojo","Rojo","Rojo","Rojo","Rojo","Rojo","Rojo","Rojo","Rojo","Negro","Negro","Negro","Negro","Negro","Negro","Negro","Negro","Negro","Negro","Negro","Negro","Negro","Negro","Negro","Negro","Negro",]
            opcion_rule = random.choice(opciones_ruleta).lower()
            print("Si aciertas el color GANARAS!!!")
            print("Negro = 56,35% ---> x2 ganancia")
            print("Rojo = 40,63% ----> x3 ganancia")
            print("Verde = 3,13% ----> x10 ganancia")
            color = str(input("A que color quieres apostar?? (Escribe el color a apostar): ")).lower()
            
                
            pago = int(input("Ingrese la cantidad que desea apostar: "))
            
            if pago <= 0:
                print("Por favor, ingrese una cantidad válida mayor que 0.")
                continue
            elif pago > jugador.digicoins:
                print("Lo siento, no tienes suficientes Digicoins para realizar esa apuesta.")
                continue
            
            jugador.digicoins -= pago
            
            print("Girando la ruleta", end=" ")
            for _ in range(3):
                print(".", end=" ", flush=True)
                time.sleep(1)  
            print("\nLa ruleta ha girado y el color ganador es:", opcion_rule)
            
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
                print("Lo siento, no has acertado el color esta vez.")
        elif opcion_casino == "3":
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
            
            tirar = input("Quieres hacer girar la tombola?? (Cuesta 10 DIGICOINS) (SI/NO)").lower()
            if tirar == "si" and jugador.digicoins >= 10:
                opciones_tombola = ["Mejora de stats a tu Digipymon","Bajada de stats a tu Digipymon","Digicoins","Pierdes Digicoins","Un nuevo Digipymon","Pierdes un Digipymon" ]
                opcion_tombo = random.choice(opciones_tombola).lower()
                
                print("Y ha tocacado...",opcion_tombo ,"!!!!")
                if opcion_tombo == "mejora de stats a tu digipymon":
                    print("")
                    jugador.lista_digipymon[0].vida += 10    #Restaura 10 puntos de vida al primer Digipymon
                    jugador.lista_digipymon[0].ataque += 5  # Aumenta 5 puntos de ataque al primer Digipymon
                    print("La vida de ", jugador.lista_digipymon[0].nombre, "a subido 10 puntos!!")
                    print("El ataque de ", jugador.lista_digipymon[0].nombre, "a subido 5 puntos!!")
                elif opcion_tombo == "bajada de stats a tu digipymon":
                    print("")
                    jugador.lista_digipymon[0].vida -= 10    #Resta 10 puntos de vida al primer Digipymon
                    jugador.lista_digipymon[0].ataque -= 5  # Resta 5 puntos de ataque al primer Digipymon
                    print("La vida de ", jugador.lista_digipymon[0].nombre, "a bajado 10 puntos!!")
                    print("El ataque de ", jugador.lista_digipymon[0].nombre, "a bajado 5 puntos!!")
                    print("Mas suerte la proxima vez!!")
                elif opcion_tombo == "digicoins":
                    print("")
                    jugador.digicoins += 30
                    print("Has ganado 30 DIGICOINS!!!")
                elif opcion_tombo == "pierdes digicoins":
                    jugador.digicoins = 0
                    print("")
                    print("Has perdido TODAS tus DIGICOINS!!!")
                    print("Tu cuenta ha bajado a 0 DIGICOINS, te has arruinado!!")
                    print("Apostar no es lo tuyo")
                elif opcion_tombo == "un nuevo digipymon":
                    print("")
                    print("Has ganado un nuevo copañero de aventuras!!")
                    if jugador.cantidad_digipymon >= 6:
                        print("Lo siento ya tienes el maximo de digipymons maximo")
                    else:
                        digipymon_tombo = generar_digipymon_aleatorio()
                        jugador.añadir_digipymon(digipymon_tombo)
                        print(digipymon_tombo)
                elif opcion_tombo == "pierdes un digipymon":
                    jugador.lista_digipymon.remove(digipymon_jugador)
                    print("")
                    print("Uno de tus digipymons ha desaparecido de tu inventrio!!")
                    print("No lo busques en el mercado negro (estara por piezas)")
                    print("Siento tu perdida")
                else:
                    print("Opcion no valida")
            elif jugador.digicoins < 10:
                print("Dinero insuficiente")
            else:
                print("VUELVA PRONTO!!")    
        elif opcion_casino == "4":
            print("Gracias por jugar en el casino. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")

    
#? ====================COSAS GUARDADAS POR SI LAS USO==================
#? jugador.lista_digipymon[0].vida += 10    #Restaura 10 puntos de vida al primer Digipymon
#? jugador.lista_digipymon[0].ataque += 5  # Aumenta 5 puntos de ataque al primer Digipymon
#? ====================================================================S

#TODO ==================================  FUNCION MAIN  =============================================
def main():
    jugador = Jugador("Pedro")
    inventario = Inventario()
    enemigo = Enemigo()
    """
    #! Añade "balls"
    inventario.añadir_objeto("balls",5)
   
    #! Enseña las balls retirar esto al final del codigo
    #print(inventario.objetos['balls'])
    
    #! Me da un pokemon para no tener que estar cogiendolo yo todo el rato
    digi_inicial = generar_digipymon_aleatorio()
    jugador.añadir_digipymon(digi_inicial)
    """
    
    os.system("cls")

    #Intro para dar el pokemon inicial
    pregunta1 = input("Vaya!! No te habia visto por aqui!!,\n Eres nuevo??" "(Si/No)").lower()
    print("")
    if pregunta1 == "si":
        print("Oh, entiendo entiendo.\n Te explicare un poco todo esto entonces!!\n")
        print("Este mundo se llama DIGIPYMON un mundo increible donde puedes capturar y luchar con unas criaturas increiblemente interesantes")
        aceptar_digi = input("Y hablando de esas criaturitas... Te veo escaso de un digipymon, ¿te interesaria que te de uno? (Si/No)\n").lower()
       
        if aceptar_digi == "si":
            os.system("cls")
            print("Asi se habla!!")
            digi_inicial = generar_digipymon_aleatorio()
            jugador.añadir_digipymon(digi_inicial)   
        else:
            os.system("cls")
            print("Vamos vamos no seas timido...")
            print("Aqui tienes, cogelo")
            digi_inicial = generar_digipymon_aleatorio()
            jugador.añadir_digipymon(digi_inicial)
            
        print(" **HAS RECIBIDO TU PRIMER DIGIPYMON**")
        print(digi_inicial)
        print("")
        print("Yo tengo que irme ya pero ya veraas como todo va bien.")
        print("Disfruta de tu aventura!!")
    else: 
        print("Oh, entiendo entiendo.\n Entonces dejemonos de rodeos\n")
        print("Te dare un digipymon con el que puedas empezar decentemente, Te deseo mucha suerte!!")
        
        digi_inicial = generar_digipymon_aleatorio()
        jugador.añadir_digipymon(digi_inicial)
        
        print(" **HAS RECIBIDO TU PRIMER DIGIPYMON**")
        print(digi_inicial)
        
    print("")
    print("ANTES DE IRSE EL MISTERIOSO SEÑOR HA DEJADO UNA BOLSA CON UNA NOTA: ")
    bolsa = input("Quieres leer la nota??   (Si/No)" ).lower()
    if bolsa == "si":
        print("Siento las prisas pero tenia cosas que hacer, solo por si crees necesitarlo aqui te dejo algunas cosas...\n")
        coger = input("¿Quieres coger la bolsa?   (Si/No)\n").lower()
        if coger == "si":
            print("***Has recibido 3 balls y 1 pocion***")
            inventario.añadir_objeto("balls", 3)
            inventario.añadir_objeto("pocion", 1)
        else:
            print("Te vas sin coger la bolsa")
    else:
        print("Te vas sin leer si quiera la nota")
    # Continuamos con el bucle principal del juego
    while True:
        
        opcion = menu()
        
        if opcion == 1:
            
            # Buscar Digipymon
            buscar_digipymon(jugador, inventario)
            
        elif opcion == 2:
            # Luchar contra un entrenador
            combate(jugador, enemigo)
            
        elif opcion == 3:
            # Ir a la tienda
            digishop(jugador, inventario)
            pass
        elif opcion == 4:
            # Usar objetos
            usar_item(jugador, inventario)
            pass
        elif opcion == 5:
            # Consultar inventario
            os.system("cls")
            print("DIGICOINS:", jugador.digicoins)
            inv = str(inventario.objetos)
            print("--------INVENTARIO--------")
            print(inv.replace("{"," ").replace("}"," ").replace(",","\n").replace("'"," "))
            print("--------------------------")
            
        elif opcion == 6:
            # Consultar digipymons
            os.system("cls")
            print("Tienes un total de:", jugador.cantidad_digipymon , "Digipymons\n")
            for i in jugador.lista_digipymon:
                print(i)
        elif opcion == 7:
            #Casino
            casino(jugador)
            
        elif opcion == 8:
            # Salir
            print("GRACIAS POR JUGAR!!")
            print("Saliendo", end=" ")
            for _ in range(3):
                print(".", end=" ", flush=True)
                time.sleep(1)  # Pausa de 1 segundo entre cada punto suspensivo
            break
        
            
        else:
            print("Opción inválida. Por favor, elige una opción del 1 al 7.")

main()