# Josué Aldaco
# A00232369

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

print("Let´s play Battleship")
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
    
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if (guess_row == ship_row and guess_col == ship_col) or (guess_row == ship2_row and guess_col == ship2_col) or (guess_row == ship3_row and guess_col == ship3_col):
        print("Congratulations! You sank a battleship")
        if turn % 2 == 0:
            puntos2 = puntos2+1
        else:
            puntos=puntos+1
    else:
        if guess_row > (4) or guess_col > (4):
            print("Oops, that´s not even in the ocean")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already")
        else:
            print("You missed my battleship!")
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
                print("Game over")
            print_board(board)

if puntos > puntos2:
    print("Gano el jugador 1")
elif puntos2>puntos:
    print("Gano jugador 2")
else:
    print("Empate")