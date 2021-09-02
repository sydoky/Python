fields = [1, 2, 3, 4, 5, 6, 7, 8, 9]

board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
def draw_board(Game):
    print(Game[0], Game[1], Game[2])
    print(Game[3], Game[4], Game[5])
    print(Game[6], Game[7], Game[8])

def winner_check(Board):
    winner = False
    if Board[0] == Board[1] and Board[1] == Board[2] and board[2] != "_":
        winner = True
    if Board[3] == Board[4] and Board[4] == Board[5] and board[5] != "_":
        winner = True
    if Board[6] == Board[7] and Board[7] == Board[8] and board[8] != "_":
        winner = True
    if Board[0] == Board[3] and Board[3] == Board[6] and board[6] != "_":
        winner = True
    if Board[1] == Board[4] and Board[4] == Board[7] and board[7] != "_":
        winner = True
    if Board[2] == Board[5] and Board[5] == Board[8] and board[8] != "_":
        winner = True
    if Board[0] == Board[4] and Board[4] == Board[8] and board[8] != "_":
        winner = True
    if Board[2] == Board[4] and Board[4] == Board[6] and board[6] != "_":
        winner = True
    return winner

player = None
while player == None:
    player = input("Please, choose a side X or O: ")
    player = player.upper()
    if player != "X" and player != "O":
        player = None
        print("Error! That is neither X, nor O")


draw_board(fields)

for turn in range(1, 10):
    print() #one line empty. it means nothing
    user_choice = None
    while user_choice == None:
        user_choice = input("Please, take your turn: ")
        user_choice = int(user_choice)          #a string converts into a number, comes a number in quotes. get rid of quotes
        if user_choice < 1 or user_choice > 9:
            user_choice = None
            print("Error. The number has to be between 1 & 9")
        elif board[user_choice -1]!= "_":       #else if number is not taken
            user_choice = None
            print("This field is taken")
    print("Your move is ", user_choice)
    move = "X"
    if turn in [2, 4, 6, 8]:
        move = "O"
    board[user_choice -1] = move        #this inserts X or O on the board
    draw_board(board)
    if winner_check(board):
        print("The winner is", move)
        break
print("Game Over")



