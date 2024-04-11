import random, os
from ListaNombres import ListaNombres
from Jugador import Jugador
from Enemigo import Enemigo
from Inventario import Inventario
from Digipymon import Digipymon

# Función para generar un Digipymon aleatorio
def generar_digipymon_aleatorio():
    #Genera el tipo del digipymon de manera aleatoria del array
    tipos = ["Planta", "Fuego", "Agua"]
    tipo_seleccionado = random.choice(tipos)
    
    # Genera un nombre aleatorio proveniente de la clase ListaNombres
    lista = ListaNombres()
    nombre_aleatorio = lista.obtener_nombre_digipymon()
    
    #Genera estadisticas aleatorias (Vida,Ataque,Nivel)
    numero_aleatorio_vida = random.randint(10,20)
    numero_aleatorio_ataque = random.randint(1,10)
    numero_aleatorio_nivel = random.randint(1,3)
    
    #Selecciona los parametros
    digipymon = Digipymon(nombre_aleatorio, numero_aleatorio_vida, numero_aleatorio_ataque, numero_aleatorio_nivel, tipo_seleccionado)
    
    return digipymon

# Función para mostrar el menú y obtener la opción del jugador
def menu():
    print(f"1. Buscar Digipymon \n2. Luchar contra un entrenador \n3. Ir a la tienda \n4. Usar objetos \n5. Consultar inventario \n6. Consultar digipymons \n7. Salir")
    operacion = int(input())
    return operacion

# Función para buscar un Digipymon
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
    elif jugador.cantidad_digipymon >= 6:
        print("Ya tienes 6 digipymons!!")
            
    elif inventario.objetos['balls'] <= 0:
        print("No tienes bolas jaja")
        
    else:
        # !maybe añadir algo
        pass

# Función principal del juego
def Main():
    jugador = Jugador()
    inventario = Inventario()
    # Añade "pokeballs"
    inventario.añadir_objeto("balls", 5)
   
    #! Enseña las balls retirar esto al final del codigo
    print(inventario.objetos['balls'])
    
    
    while True:
        print(jugador.cantidad_digipymon)
        opcion = menu()
        
        if opcion == 1:
            # Buscar Digipymon
            buscar_digipymon(jugador, inventario)
        elif opcion == 2:
            # Luchar contra un entrenador
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
            pass
        elif opcion == 7:
            # Salir
            break
        else:
            print("Opción inválida. Por favor, elige una opción del 1 al 7.")

Main()
