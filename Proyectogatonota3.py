import random                               #Este import random nos servira despues, para hacer el juego contra la maquina.
def mostrar_tablero(tablero):               #Esta funcion nos permite imprimir el tablero
    print(f"{tablero[0]} {tablero[1]} {tablero[2]} {tablero[3]} {tablero[4]}")
    print("---------")
    print(f"{tablero[5]} {tablero[6]} {tablero[7]} {tablero[8]} {tablero[9]}")
    print("---------")
    print(f"{tablero[10]} {tablero[11]} {tablero[12]} {tablero[13]} {tablero[14]}")

def check_winner(tablero, player):           #Esta funcion nos permite verificar si hay un ganador depues de cada jugada
    win_positions = [
        [0, 2, 4], [5, 7, 9], [10, 12, 14],  #Estas son todas las posibilidades de ganar
        [0, 5, 10], [2, 7, 12], [4, 9, 14],  
        [0, 7, 14], [4, 7, 10]               
    ]
    for pos in win_positions:
        if all(tablero[i] == player for i in pos):   #Este "for" es lo que verifica si hay un ganador
            return True
    return False

def j1_vs_j2():                                     #Esta funcion es para el modo de juego 1vs1
    tablero = [1, "|", 2, "|", 3, 4, "|", 5, "|", 6, 7, "|", 8, "|", 9]  #Esta es la lista mas importante, ya que aqui se iran reemplazando los numeros con las X e O de cada jugada
    mostrar_tablero(tablero)     #Esto muestra el tablero inicial ya que aun no se han hecho cambios
    
    nombrex = input("Ingrese el nombre del jugador X: ")
    nombrey = input("Ingrese el nombre del jugador O: ")          #Aqui pedimos los nombres de cada jugador para que sepan con que juega cada uno y para mencionar al ganador (En el caso de que haya uno)
    
    posiciones_ocupadas = []                            #Esta lista sera importante a la hora de que algun jugador seleccione una casilla ocupada
    turno_actual = "X"                                  #Esta X es para que comience este jugador
    
    for i in range(9):  # Este for nos permitira repetir el proceso de las jugadas. 9 es el maximo de jugadas que se pueden realizar.
        while True:     # Con este while true, repetimos el proceso para no depender de una condicional
            try:        # Este try no ayuda a que el programa se siga ejecutando siempre y cuando no sea una excepcion
                posicion = int(input(f"{nombrex if turno_actual == 'X' else nombrey} ingrese la posición que desea ocupar: ")) #Aqui le pedimos al jugador que ingrese el numero de la casilla que desea elegir
                if posicion < 1 or posicion > 9 or posicion in posiciones_ocupadas:
                    print("Posición no válida o ya ocupada, por favor intentelo nuevamente.")           #Aqui verivicamos que el numero que haya elegido este en el rango de 1 a 9 y que no este en la lista de posiciones ya ocupadas
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")        #ValueError nos ayuda para que cualquier valor que ingrese el usuario que no este dentro de lo que pedimos sea reconocido y nos muestre el mensaje para ingresar otro numero

        index = tablero.index(posicion)   #Esto es para saber la ubicacion del numero ingresado en la lista para posteriormente remplazarlo
        tablero[index] = turno_actual     #Aqui el numero se reemplaza segun el de quien sea el turno (X, O)
        posiciones_ocupadas.append(posicion) #Aqui agregamos la jugada a la lista de posiciones ocupadas
        mostrar_tablero(tablero)          #Aqui mostramos el tablero cada vez que se realice una jugada 

        if check_winner(tablero, turno_actual):
            print(f"¡{nombrex if turno_actual == 'X' else nombrey} ha ganado!")  #Este "if" es lo que verifica si hay un ganador despues de cada jugada 
            return
        
        turno_actual = "O" if turno_actual == "X" else "X"   #Esto nos permite cambiar de jugador en cada jugada (X, O)
    
    print("¡Es un empate!") #Este es el mensaje que se muestra luego de que pasan los 9 turnos sin ningun ganador

def jug_vs_COM():                       #Esto define la funcion que utilizaremos para jugar contra la maquina
    tablero = [1, "|", 2, "|", 3, 4, "|", 5, "|", 6, 7, "|", 8, "|", 9]             #Esta es la lista mas importante, ya que aqui se iran reemplazando los numeros con las X e O de cada jugada
    mostrar_tablero(tablero)                                                        #Esto muestra el tablero inicial ya que aun no se han hecho cambios
    
    nombrex = input("Ingrese el nombre del jugador X: ")                  #En esta ocasion solo requeriremos un solo nombre
    
    posiciones_ocupadas = []                #Esta lista sera importante a la hora de que el jugador seleccione una casilla ocupada y para que la maquina no seleccione una casilla ocupada
    turno_actual = "X"                      #Esto es para que el jugador comience
    
    for i in range(9):  # Este for nos permitira repetir el proceso de las jugadas. 9 es el maximo de jugadas que se pueden realizar.
        if turno_actual == "X":  #Esto se refiere a que lo que programemos a continuacion solo contara para el jugador
            while True:   # Con este while true, repetimos el proceso para no depender de una condicional
                try:            # Este try no ayuda a que el programa se siga ejecutando siempre y cuando no sea una excepcion
                    posicion = int(input(f"{nombrex} ingrese la posición que desea ocupar: "))          #Aqui le pedimos al jugador que ingrese el numero de la casilla que desea elegir
                    if posicion < 1 or posicion > 9 or posicion in posiciones_ocupadas:
                        print("Posición no válida o ya ocupada. Intente nuevamente.")                   #Aqui verivicamos que el numero que haya elegido este en el rango de 1 a 9 y que no este en la lista de posiciones ya ocupadas
                        continue
                    break
                except ValueError:                                           #ValueError nos ayuda para que cualquier valor que ingrese el usuario que no este dentro de lo que pedimos sea reconocido y nos muestre el mensaje para ingresar otro numero
                    print("Por favor, ingrese un número válido.")
        else:
            posicion = random.choice([pos for pos in range(1, 10) if pos not in posiciones_ocupadas])           #Esta parte es para que la maquina elija un numero al azar entre el 1 y el 9 y que no este en la lista de posiciones ocupadas
            print(f"El jugador O (máquina) elige la posición: {posicion}") #Este es un mensaje para el usuario mostrando el numero que escogio la maquina

        index = tablero.index(posicion)     #Esto es para saber la ubicacion del numero ingresado en la lista para posteriormente remplazarlo
        tablero[index] = turno_actual       #Aqui el numero se reemplaza segun de quien sea el turno (X, O)
        posiciones_ocupadas.append(posicion)        #Aqui agregamos la jugada a la lista de posiciones ocupadas
        mostrar_tablero(tablero)            #Aqui mostramos el tablero cada vez que se realice una jugada 

        if check_winner(tablero, turno_actual):
            print(f"¡{nombrex} ha ganado!" if turno_actual == "X" else "¡El jugador O (máquina) ha ganado!")        #Este "if" es lo que verifica si hay un ganador despues de cada jugada
            return
        
        turno_actual = "O" if turno_actual == "X" else "X"          #Esto nos permite cambiar de jugador en cada jugada (X, O)
    
    print("¡Es un empate!")             #Este es el mensaje que se muestra luego de que pasan los 9 turnos sin ningun ganador

print("Bienvenido a mi código :) !!!")    #Aqui le damos la bienvenida al usuario

while True: #Hacemos el while true para que nuestro menu se repita las veces que queramos
    res = int(input("1.-Versus(P1 VS P2)\n2.-Nueva partida(P1 VS COM)\n3.- Salir\nPara comenzar a jugar, por favor selecciona una opción: ")) #Pedimos al usuario que seleccione una opcion del menu 
    if res == 1:
        j1_vs_j2()      #Llamamos a la funcion de jugador contra jugador si el usuario selecciona la opcion 1
    elif res == 2:
        jug_vs_COM()    #Llamamos a la funcion contra la maquina si el usuario selecciona la opcion 2
    elif res == 3:
        print("Gracias por ocupar mi código!!!!! ;)")
        break  #Es para que salgamos de nuestro codigo con un mensaje de agradecimiento al usuario si es que selecciona la opcion 3
    else:
        print("¡Opción no válida! Intente nuevamente.") #Muestra este mensaje si la opcion no esta en el menu
