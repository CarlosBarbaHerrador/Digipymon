import random, os, time
from ListaNombres import ListaNombres
from Jugador import Jugador
from Enemigo import Enemigo
from Inventario import Inventario
from Digipymon import Digipymon
lista = ListaNombres()
enemigo = Enemigo()
jugador = Jugador()
inventario = Inventario()


#TODO ====================== GENERAR DIGIPYMON ALEATORIO =============================
def generar_digipymon_aleatorio():
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


#TODO ================================  MENU  ========================================
def menu():
    print("---------------DIGIPYMON!---------------")
    print("****************************************")
    print("1. Buscar Digipymon")
    print("2. Luchar contra un entrenador")
    print("3. Ir a la tienda")
    print("4. Usar objetos")
    print("5. Consultar inventario")
    print("6. Consultar Digipymons")
    print("7. Salir")
    print("****************************************")
    operacion = int(input())
    return operacion


#TODO ================================  BUSCAR DIGIPYMON  ==================================
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
   
    Captura = str(input("¿Quieres intentar capturarlo? Te quedan {} balls   Si/No\n ".format( inventario.objetos['balls']) ))
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
    # Si tienes mas de 6 digipymons no te dejará
    elif jugador.cantidad_digipymon >= 6:
        print("Ya tienes 6 digipymons!!")
            
    elif inventario.objetos['balls'] <= 0:
        print("No tienes bolas jaja\n")
    
    else:
        print("Has huido del Combate!! Un poco cobarde por tu parte 🐓🐓🐓")


#TODO ================================  FUNCION COMBATE  ============================================
def combate(jugador, enemigo):
    ronda_ganada = 0
    ronda_perdida = 0
    nombre_aleatorio_entrenador = lista.obtener_nombre_entrenador()
    
    print("Si evitas la pelea perderás 1 Digicoin")
    peleita = str(input("¿Estás seguro de querer combatir? Si/No\n"))
    pelea = peleita.lower()
    if pelea == "si":
        os.system("cls")
        print("Te has encontrado a:",nombre_aleatorio_entrenador ,"Preparate para luchar!!")
        print("")
        # Bucle para agregar los Digipymons del jugador al enemigo
        for _ in range(jugador.cantidad_digipymon):
            digipymon_entrenador = generar_digipymon_aleatorio()
            enemigo.añadir_digipymon(digipymon_entrenador)
            
        if jugador.cantidad_digipymon == 0:
            print("No tienes Digipymons para combatir.")
            
        else:
            
            # Itera sobre los Digipymons del jugador y del enemigo
            for i in range(min(jugador.cantidad_digipymon, enemigo.cantidad_digipymon)):
                digipymon_jugador = jugador.lista_digipymon[i]
                digipymon_enemigo = enemigo.lista_digipymon[i]
                
                # Compara los ataques de los Digipymons
                if digipymon_jugador.ataque > digipymon_enemigo.ataque:
                    # El jugador gana el combate
                    print("¡Tu Digipymon ha ganado el combate!")
                    diferencia_ataque = digipymon_jugador.ataque - digipymon_enemigo.ataque
                    digipymon_enemigo.vida -= diferencia_ataque
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
                    if digipymon_jugador.vida <= 0:
                        print("¡Tu Digipymon ha sido derrotado!")
                        jugador.lista_digipymon.remove(digipymon_jugador)
                        jugador.cantidad_digipymon -= 1
                        ronda_perdida += 1
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

        
#TODO ===============================  FUNCION DIGISHOP  ==========================================
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
            inventario.añadir_objeto("poción", 1)
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

#TODO ===============================  FUNCION USAR OBJETO  ==========================================
def usar_item(jugador, inventario):
    inv = str(inventario.objetos)
    print("--------INVENTARIO--------")
    print(inv.replace("{"," ").replace("}"," ").replace(",","\n").replace("'"," "))
    print("--------------------------")
    
    # Obtener la selección del jugador
    seleccion = input("¿Qué ítem deseas usar?  ").capitalize()
    
    # Comprobar si el jugador tiene el ítem seleccionado
    if seleccion == "pocion":
        if inventario.objetos.get("poción", 0) > 0:
            # Usar la poción para aumentar la vida del primer Digipymon en 10 puntos
            jugador.lista_digipymon[0].vida += 10
            # Reducir en 1 la cantidad de pociones en el inventario
            inventario.objetos["pocion"] -= 1
            print("¡Has usado una Poción! La vida de tu Digipymon se ha aumentado en 10 puntos.")
        else:
            print("¡No tienes pociones en tu inventario!")
    elif seleccion == "Anabolizantes":
        if inventario.objetos.get("Anabolizantes", 0) > 0:
            # Usar los anabolizantes para aumentar el ataque del primer Digipymon en 5 puntos
            jugador.lista_digipymon[0].ataque += 5
            # Reducir en 1 la cantidad de anabolizantes en el inventario
            inventario.objetos["Anabolizantes"] -= 1
            print("¡Has usado Anabolizantes! El ataque de tu Digipymon se ha aumentado en 5 puntos.")
        else:
            print("¡No tienes Anabolizantes en tu inventario!")
    elif seleccion == "Digipyballs":
        print("¡No puedes usar Digipyballs en combate!")
    else:
        print("¡Ítem no válido!")

   

    
#? ====================COSAS GUARDADAS POR SI LAS USO==================
#? jugador.lista_digipymon[0].vida += 10    #Restaura 10 puntos de vida al primer Digipymon
#? jugador.lista_digipymon[0].ataque += 5  # Aumenta 5 puntos de ataque al primer Digipymon
#? ====================================================================

# Función principal del juego
def Main():

    #! Añade "balls"
    inventario.añadir_objeto("balls",5)
   
    #! Enseña las balls retirar esto al final del codigo
    #print(inventario.objetos['balls'])
    
    #! Me da un pokemon para no tener que estar cogiendolo yo todo el rato
    digi_inicial = generar_digipymon_aleatorio()
    jugador.añadir_digipymon(digi_inicial)
    
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
            # Salir
            break
        else:
            print("Opción inválida. Por favor, elige una opción del 1 al 7.")

Main()