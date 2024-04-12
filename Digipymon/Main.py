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
def combate(Enemigo):
    # genera un nombre aleatorio del entrenador enemigo
    nombre_aleatorio_entrenador = lista.obtener_nombre_entrenador()

    
    peleita = str(input("¿Estas seguro de querer combatir? Si/No\n"))
    pelea = peleita.lower()
    print("Si evitas la pelea perderas 1 Digicoins")
    
    if pelea == "si":
        
        # Bucle para agregar los Digipymons del jugador al enemigo
        for _ in range(jugador.cantidad_digipymon):
            digipymon_entrenador = generar_digipymon_aleatorio()
            enemigo.añadir_digipymon(digipymon_entrenador)

        print("Te has encontrado con", nombre_aleatorio_entrenador , "!!!\n" "Tiene: ", enemigo.cantidad_digipymon , " digipymons")
    
        pass
    
    elif pelea == "no":
        print("Te has escondido para que el entrenador no te vea!!")
        print("Al esconderte se te ha caido una moneda al suelo!!")
        print("Que cobarde ereeeesss!!!🐓🐓")
        jugador.digicoins - 1

    

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
            combate(enemigo)
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
