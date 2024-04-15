import random, os
from ListaNombres import ListaNombres
from Jugador import Jugador
from Enemigo import Enemigo
from Inventario import Inventario
from Digipymon import Digipymon
lista = ListaNombres()
enemigo = Enemigo()
jugador = Jugador()
inventario = Inventario()


#TODO FUNCION PARA GENERAR UN DIGIPYMON ALEATORIO
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

#TODO FUNCION PARA GENERAR MENU
def menu():
    print(f"1. Buscar Digipymon \n2. Luchar contra un entrenador \n3. Ir a la tienda \n4. Usar objetos \n5. Consultar inventario \n6. Consultar digipymons \n7. Salir")
    operacion = int(input())
    return operacion

#TODO FUNCION PARA BUSCAR DIGIPYMON
def buscar_digipymon(jugador, inventario):
    
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

#TODO FUNCION COMBATE
def combate(jugador, enemigo):
    ronda_ganada = 0
    ronda_perdida = 0
    nombre_aleatorio_entrenador = lista.obtener_nombre_entrenador()
    print("Si evitas la pelea perderás 1 Digicoin")
    peleita = str(input("¿Estás seguro de querer combatir? Si/No\n"))
    pelea = peleita.lower()
    if pelea == "si":
        print("Te has encontrado a:",nombre_aleatorio_entrenador ,"Preparate para luchar!!")
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
                print("")
            
            if ronda_ganada > ronda_perdida:
                print("Has derrotado a:", nombre_aleatorio_entrenador)
                print("Has recibido", ronda_ganada, "Digicoins por ganar")
                jugador.digicoins += ronda_ganada
                
    elif pelea == "no":
        print("Te has escondido para que el entrenador no te vea!!")
        print("Al esconderte se te ha caído una moneda al suelo!!")
        print("¡Qué cobarde eres! 🐓🐓")
        jugador.digicoins -= 1
    else:
        print("Comando inválido. Por favor, responde 'Si' o 'No'.")


    

# Función principal del juego
def Main():

    #! Añade "balls"
    inventario.añadir_objeto("balls",5)
   
    #! Enseña las balls retirar esto al final del codigo
    print(inventario.objetos['balls'])
    
    
    while True:
        
        opcion = menu()
        print(enemigo.cantidad_digipymon)
        if opcion == 1:
            
            # Buscar Digipymon
            buscar_digipymon(jugador, inventario)
            
        elif opcion == 2:
            # Luchar contra un entrenador
            combate(jugador, enemigo)
            pass
        elif opcion == 3:
            # Ir a la tienda
            pass
        elif opcion == 4:
            # Usar objetos
            pass
        elif opcion == 5:
            # Consultar inventario
            pass
        elif opcion == 6:
            # Consultar digipymons
            print("Tienes un total de:", jugador.cantidad_digipymon , "Digipymons\n")
            for i in jugador.lista_digipymon:
                print(i)
            
        elif opcion == 7:
            # Salir
            break
        else:
            print("Opción inválida. Por favor, elige una opción del 1 al 7.")

Main()