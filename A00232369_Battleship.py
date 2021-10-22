# Proyecto Battleship
# Josué Aldaco _ Gustavo Lares
# A00232369 _ A01254066
# TC1028 Gpo 3
# 18 Oct 2021


from random import randint

board = []
t = ""
for x in range(5):
    board.append(["O"] * 5 )
    t = t + "O"*5
tablero = open("Tablero.txt","w")
tablero.write(t)
tablero.close()

def print_board(board):
    for row in board:
        print (" ".join(row))

print("Bienvenido a Battleship de Josué y Gustavo")
print("En este juego, ustedes trataran de adivinaran la fila y la columna en la que las naves se encuentran, los turnos seran altenados, empezando con el jugador 1 y siguiendo con el jugador 2, cada jugador dispone de 4 intentos, Nota: Las filas y las columnas van del 0 al 4")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
ship2_row = random_row(board)
ship2_col = random_col(board)
ship3_row = random_row(board)
ship3_col = random_col(board)



puntos=0
puntos2=0

for turn in range(8):
    print ("Turn", turn + 1)
    
    guess_row = int(input("Adivine la fila: "))
    guess_col = int(input("Adivine la columna: "))

    if (guess_row == ship_row and guess_col == ship_col) or (guess_row == ship2_row and guess_col == ship2_col) or (guess_row == ship3_row and guess_col == ship3_col):
        print("ACERTASTE, Nave enemiga eliminada")
        tablero = open("Tablero.txt","r")
        tab = tablero.read()
        tablero.close()
        tab=list(tab)
        tab[guess_row*5 + guess_col] = "T"
        t=""
        for i in tab:
            t=t+i
        tablero = open("Tablero.txt","w")
        tablero.write(t)
        tablero.close()
        board[guess_row][guess_col] = "T"
        if turn == 7:
            print("El juego termino")
        print_board(board)
        if turn % 2 == 0:
            puntos2 = puntos2+1
        else:
            puntos=puntos+1
    else:
        if guess_row > (4) or guess_col > (4):
            print("FALLASTE, Ese punto no se encuentra en el oceano")
        elif board[guess_row][guess_col] == "X":
            print("FALLASTE, Ya introduciste ese punto repetidamente")
        else:
            print("FALLASTE, No se acerto en la nave")
            tablero = open("Tablero.txt","r")
            tab = tablero.read()
            tablero.close()
            tab=list(tab)
            tab[guess_row*5 + guess_col] = "X"
            t=""
            for i in tab:
                t=t+i
            tablero = open("Tablero.txt","w")
            tablero.write(t)
            tablero.close()
            board[guess_row][guess_col] = "X"
            if turn == 7:
                print("El juego termino")
            print_board(board)

if puntos > puntos2:
    print("Gano el jugador 1")
elif puntos2>puntos:
    print("Gano jugador 2")
else:
    print(" Ambos jugadores obtuvieron los mismos puntos, es un Empate")