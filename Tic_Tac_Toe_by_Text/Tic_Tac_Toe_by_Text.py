import numpy as np
from input import vaild # the class i created to check the input value is int or not.
Borad = np.array([[" "," "," "],[" "," "," "],[" ", " ", " "]]) 

def print_board(): # the the function to print the board.
    print('-------------')
    for row in Borad:
        print('| ' + ' | '.join(row) + ' |')
        print('-------------')

def winner(): 
    # for row winner
    for row in Borad:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True
    #for col
    for col in range(3):
        if Borad[0][col] == Borad[1][col] == Borad[2][col] and Borad[0][col] != " ":
            return True
    # for diagonals
    if Borad[0][0] == Borad[1][1] == Borad[2][2] and Borad[0][0] != " ":
        return True
    if Borad[0][2] == Borad[1][1] == Borad[2][0] and Borad[0][2] != " ":
        return True
    return False

# the method play 
def play():
    player = "X"
    while True:
        print_board()
        print("player " + player)
        row = vaild("choose the row(0 to 2)")
        col = vaild("Choose the Col from(0 to 2)")
        if Borad[row][col] != " ":
            print("That spot is already taken. Try again.")
            continue
        Borad[row][col] = player
        if winner():
            print_board()
            print("player " + player + " wins!")
            break
        if np.all(Borad != " "):
            print_board()
            print("Tie game")
            break
        player = "O" if player == "X" else "X"


#calling the method          
play()

    


        






