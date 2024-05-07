import random, os, time
from ListaNombres import ListaNombres
from Jugador import Jugador
from Enemigo import Enemigo
from Inventario import Inventario
from Digipymon import Digipymon
from Casino import Casino
from VenderDigipymon import VenderDigipymon


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
    print("")
    print("╔══════════════ DIGIPYMON! ═════════════╗")
    print("║ 1. Buscar Digipymon                   ║")
    print("║ 2. Luchar contra un entrenador        ║")
    print("║ 3. Ir a la tienda                     ║")
    print("║ 4. Usar objetos                       ║")
    print("║ 5. Consultar inventario               ║")
    print("║ 6. Consultar Digipymons               ║")
    print("║ 7. Casino                             ║")
    print("║ 8. Vender digipymon                   ║")
    print("║ 9. Salir                              ║")
    print("╚═══════════════════════════════════════╝")

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
def combate(jugador, enemigo, contador):
    lista = ListaNombres()
    ronda_ganada = 0
    ronda_perdida = 0
    contador[0] += 1 
    
    nombre_aleatorio_entrenador = lista.obtener_nombre_entrenador()
    
    print("Si evitas la pelea perderás 1 Digicoin")
    peleita = str(input("¿Estás seguro de querer combatir? Si/No\n"))
    pelea = peleita.lower()
    # Bucle para agregar los Digipymons del jugador al enemigo

    if pelea == "si":
        
        os.system("cls")
        print(contador[0])
        print("Te has encontrado a:",nombre_aleatorio_entrenador ,"Preparate para luchar!!")
        print("")

        if jugador.cantidad_digipymon == 0:
            print("No tienes Digipymons para combatir.")

         # Enfrentamiento contra el jefe al alcanzar la décima ronda
        elif contador[0] == 10:        
            os.system("cls")
            print("Alguien te habla, sabes quien es, su reputacion le precede... Es el gran entrenador Jose de Base de datos!!!\n")
            print("Jose: ¡EY, EY, EY! ¿Eres tú ese entrenador que ha estado machacando a todos los mindundis de esta zona? Con mi Digipymon será diferente, ¡te reto! Todos tus Digipymons contra el mío solo, a ver qué tal.\n")
            print("\n¡Te has encontrado a un jefe, prepárate para luchar....")

            # genera un daño aleatorio cada ronda para que el combate sea mas interactivo y menos estatico
            ataque_boss = random.randint(5, 35)
            
            digipymon_boss = Digipymon("", 125, ataque_boss, 10, "Fantasma")
            print(digipymon_boss)
            enemigo.añadir_digipymon(digipymon_boss)

            ataque_total_jugador = sum(digipymon.ataque for digipymon in jugador.lista_digipymon)
            ataque_total_enemigo = digipymon_boss.ataque
            
            # Simular la batalla
            while True:
                print("Peleando", end=" ")
                for _ in range(3):
                    print(".", end=" ", flush=True)
                    time.sleep(0.5)  # Pausa de 1 segundo entre cada punto suspensivo
                    
                # genera un daño aleatorio cada ronda para que el combate sea mas interactivo y menos estatico
                ataque_total_enemigo = random.randint(5, 35)
                digipymon_boss.ataque = ataque_total_enemigo
                # Calcular el ataque total del jugador
                print("")
                print(f"El enemigo ha realizado un ataque de {digipymon_boss.ataque} de fuerza")
                ataque_total_jugador = sum(digipymon.ataque for digipymon in jugador.lista_digipymon)
                
                # Simular el combate
                if ataque_total_jugador > ataque_total_enemigo:
                    # El jugador gana
                    diferencia_ataque = ataque_total_jugador - ataque_total_enemigo
                    digipymon_boss.vida -= diferencia_ataque
                    print("Tus digipymons han conseguido esquivar y contraatacar, le han quitado: ",diferencia_ataque, "de vida!!")
                    print("════════════════════════════════════════════════════════")
                    print(f"Le queda: {digipymon_boss.vida}")
                    if digipymon_boss.vida <= 0:
                        print("¡Has derrotado al jefe Digipymon!")
                        print("Por la victoria has ganado 50 digicoins!!!")
                        jugador.digicoins += 50
                        print("Jose: has luchado bien, muy bien mi mas sincer enhora buena")
                        break  # Termina la batalla
                elif ataque_total_jugador < ataque_total_enemigo:
                    # El jefe gana
                    diferencia_ataque = ataque_total_enemigo - ataque_total_jugador
                    for digipymon in jugador.lista_digipymon:
                        digipymon.vida -= diferencia_ataque
                        if digipymon.vida <= 0:
                            jugador.lista_digipymon.remove(digipymon)
                            jugador.cantidad_digipymon -= 1
                    print("Tus digipymons han sufrido ",diferencia_ataque, "de daño!!")
                    print("════════════════════════════════════════════════════════")
                    if len(jugador.lista_digipymon) == 0:
                        print("¡El jefe Digipymon te ha derrotado!")
                        print("Tus digipymons han caido en combate y los has perdido")
                        print("Un duro dia para cualquier entrenador")
                        break  # Termina la batalla
                else:
                    print("¡Ha sido un empate!")
                    print("══════════════════════════════════════")
                # Comprobar si uno de los equipos ha perdido toda su vida
                if ataque_total_jugador <= 0 or digipymon_boss.vida <= 0:
                    break  # Termina la batalla si la vida de alguno es menor o igual a 0

            
        else:
            # Bucle para agregar los Digipymons del jugador al enemigo (Lo pongo de nuevo para que actualice los digipymons que ha capturado en la ronda anterior en jugador)
            for _ in range(jugador.cantidad_digipymon):
                digipymon_entrenador = generar_digipymon_aleatorio()
                enemigo.añadir_digipymon(digipymon_entrenador)
               
            
            for i in range(len(jugador.lista_digipymon)):  
                digipymon_jugador = jugador.lista_digipymon[i]
                digipymon_enemigo = enemigo.lista_digipymon[i]
                
                # Compara los ataques de los Digipymons
                if digipymon_jugador.ataque > digipymon_enemigo.ataque:
                    # El jugador gana el combate
                    print(f"¡{jugador.nombre} ha ganado la ronda!")
                    diferencia_ataque = digipymon_jugador.ataque - digipymon_enemigo.ataque
                    ronda_ganada += 1
                    
                    if digipymon_enemigo.vida <= 0:
                        print("¡El Digipymon enemigo ha sido derrotado!(Debilitado)")
                        
                        enemigo.cantidad_digipymon -= 1
                        ronda_ganada += 1
                                
                elif digipymon_jugador.ataque < digipymon_enemigo.ataque:
                    # El jugador pierde el combate
                    print("¡Tu Digipymon ha perdido la ronda!")
                    diferencia_ataque = digipymon_enemigo.ataque - digipymon_jugador.ataque
                    digipymon_jugador.vida -= diferencia_ataque
                    ronda_perdida += 1 
                    
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
                    
                    
                    if digipymon_jugador.vida <= 0:
                        print("¡Tu Digipymon ha sido derrotado!")
                        jugador.lista_digipymon.remove(digipymon_jugador)
                        jugador.cantidad_digipymon -= 1
                        
                    if digipymon_enemigo.vida <= 0:
                        print("¡El Digipymon enemigo ha sido derrotado!")
                        
                        enemigo.cantidad_digipymon -= 1
                
                print("         ", "Tu","/","Enemigo")
                print("Marcador: ", ronda_ganada ,"/", ronda_perdida)
                print("----------------------------------------")
            enemigo.lista_digipymon.clear()
            enemigo.cantidad_digipymon = 0
            
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
                    print("Eres tan pobre que no puedes perder un dinero que no tienes")
                    
                else:
                    print("Eres tan pobre que no puedes perder un dinero que no tienes")
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
    print("DIGICOINS:", jugador.consultar_digicoins())
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

#TODO ==================================  FUNCION MAIN  ==========================================
def main():
    jugador = Jugador("*")  # Crear una instancia de Jugador
    inventario = Inventario()  # Crear una instancia de Inventario
    enemigo = Enemigo()  # Crear una instancia de Enemigo
    contador_peleas = [0]  # Inicializar un contador de peleas
    casino = Casino()
    vender = VenderDigipymon()
    # Limpiar la consola y solicitar el nombre del jugador
    os.system("cls")
    jugador.nombre = input("Bienvenido a Digipymmon!! ¿Cuál es tu nombre?\n").capitalize()

    # Introducción al juego y elección de Digipymon inicial
    pregunta1 = input("¿Eres nuevo aquí? (Si/No) ").lower()
    print("")
    if pregunta1 == "si":
        print("Oh, entiendo. Es un placer conocerte,", jugador.nombre, "\nTe explicaré un poco sobre todo esto entonces.\n")
        print("Este mundo se llama Digipymon, un lugar increíble donde puedes capturar y luchar con criaturas fascinantes.")
        aceptar_digi = input("Y hablando de esas criaturas... Veo que no tienes un Digipymon contigo. ¿Te gustaría que te diera uno? (Si/No)\n").lower()
       
        if aceptar_digi == "si":
            # Sección para elegir un Digipymon inicial
            os.system("cls")
            print("¡Así me gusta!")
            # Generar Digipymons iniciales predefinidos
            digi_inicial_fuego = Digipymon("Flamagon", 10, 5, 1, "Fuego")
            digi_inicial_planta = Digipymon("Polivine", 10, 5, 1, "Planta")
            digi_inicial_agua = Digipymon("Aqualisk", 10, 5, 1, "Agua")
            # Mostrar Digipymons iniciales disponibles
            print(digi_inicial_fuego,"\n" , digi_inicial_planta,"\n" , digi_inicial_agua)
            elige_digi = input("¿Cuál de estos Digipymons quieres? (1/2/3) ").lower()
            if elige_digi == "1":
                print("\n¡Has elegido a Flamagon!")
                jugador.añadir_digipymon(digi_inicial_fuego)
                print("** HAS RECIBIDO TU PRIMER DIGIPYMON **\n")
                print(digi_inicial_fuego)
                
            elif elige_digi == "2":
                print("\n¡Has elegido a Polivine!")
                jugador.añadir_digipymon(digi_inicial_planta)
                print("** HAS RECIBIDO TU PRIMER DIGIPYMON **\n")
                print(digi_inicial_planta)
                
            elif elige_digi == "3":
                print("\n¡Has elegido a Aqualisk!")
                jugador.añadir_digipymon(digi_inicial_agua)
                print("** HAS RECIBIDO TU PRIMER DIGIPYMON **\n")
                print(digi_inicial_agua)
                
            elif elige_digi == "666":
                # Easter egg
                os.system("cls")
                print("De debajo de tus pies algo ocurre... un portal se abre, es rojo como el mismísimo infierno y llamas salen de él.")
                print("Y de él sale un pequeño Digipymon que te mira y una voz resuena en tu cabeza diciendo: ¿Mamá?")
                print("Decides adoptar al pequeño Digipymon aunque no sabes muy bien por qué.")
                jugador.añadir_digipymon(digi_inicial_especial)
                print("** HAS RECIBIDO TU PRIMER DIGIPYMON **\n")
                print(digi_inicial_especial)
               
        else:
            os.system("cls")
            print("Vamos vamos, no seas tímido...")
            print("Aquí tienes, cógelo")
            digi_inicial = generar_digipymon_aleatorio()
            jugador.añadir_digipymon(digi_inicial)
            print("** HAS RECIBIDO TU PRIMER DIGIPYMON **")
            print(digi_inicial)
            

    else: 
        print("Oh, entiendo.\n Entonces dejémonos de rodeos.\n")
        print("Te daré un Digipymon con el que puedas empezar decentemente. ¡Te deseo mucha suerte!")
        
        digi_inicial = generar_digipymon_aleatorio()
        jugador.añadir_digipymon(digi_inicial)
        
        print("** HAS RECIBIDO TU PRIMER DIGIPYMON **")
        print(digi_inicial)
        
    # Continuación del juego...

        
    print("")
    print("ANTES DE IRSE EL MISTERIOSO SEÑOR HA DEJADO UNA BOLSA CON UNA NOTA: ")
    bolsa = input("Quieres leer la nota??   (Si/No)\n\n***Si eliges (no) no se te daran objetos iniciales para mayor dificultad***" ).lower()
    if bolsa == "si":
        os.system("cls")
        print("\nSiento las prisas pero tenia cosas que hacer, solo por si crees necesitarlo aqui te dejo algunas cosas...\n")
             
        print("***   Has recibido 10 digicoins  ***")
        print("***   Has recibido 3 balls       ***")
        print("***   Has recibido 1 pocion      ***")
        inventario.añadir_objeto("balls", 3)
        inventario.añadir_objeto("pocion", 1)
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
            combate(jugador, enemigo, contador_peleas)


            
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
            print("DIGICOINS:", jugador.consultar_digicoins())
            inv = str(inventario.objetos)
            print("╔═══════════ INVENTARIO ═══════════╗")
            print(inv.replace("{"," ").replace("}"," ").replace(",","\n").replace("'"," "))
            print("╚══════════════════════════════════╝")
            
        elif opcion == 6:
            # Consultar digipymons
            os.system("cls")
            jugador.consultar_digipymon()

        elif opcion == 7:
            #Casino
            casino.casino(jugador)
        elif opcion == 8:
            vender.vender_digipymon(jugador)
        elif opcion == 9:
            # Salir
            print("GRACIAS POR JUGAR!!")
            print("Saliendo", end=" ")
            for _ in range(3):
                print(".", end=" ", flush=True)
                time.sleep(1)  # Pausa de 1 segundo entre cada punto suspensivo
            break
        
            
        else:
            print("Opción inválida como tu. Por favor, elige una opción del 1 al 9.")

main()