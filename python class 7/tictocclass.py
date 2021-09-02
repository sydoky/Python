class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.board.initialize()
        self.board_coordinates = Board()
        self.board_coordinates.numerate()
        self.player1 = None
        self.player2 = None
        self.player = None
        self.turn = None

    def set_player(self):
        if self.turn % 2 == 1:  # we want to know whose turn is
            self.player = self.player1
        else:
            self.player = self.player2


    def play(self):
        self.create_player()
        self.create_player()
        for turn in range(1, 10):
            self.turn = turn
            self.set_player()
            self.board_coordinates.display()
            self.board.display()
            self.do_turn(self.player)
            if self.check_for_winner() is not None:
                self.board.display()
                return
            if turn == 9:
                print("it's a draw")


    def check_for_winner(self):
        sign = self.board.three_in_line()
        if sign is not None:
            print("The winner is", self.player.nickname)
        return sign


    def create_player(self):
        nickname = input("Enter the name of the player: ")
        if self.player1 is not None:
            if self.player1.nickname is None:
                self.player1.nickname = nickname
            else:
                self.player2.nickname = nickname
            return
        character = None
        while character is None:  # while loop in this instance works as preventing from entering anything from X or O
            character = input(nickname + ", choose sign (X or O): ")
            if character.upper() not in ["X", "O"]:
                character = None
                print("Error404!")
            else:
                character = character.upper()
        self.player1 = Player(None, "X", "human")
        self.player2 = Player(None, "O", "human")
        if character == "X":
            self.player1.nickname = nickname
        else:
            self.player2.nickname = nickname

    def do_turn(self, player):
        choice = None
        while choice is None:
            choice = input(player.nickname + ", choose field 1-9: ")
            if choice.isnumeric():
                choice = int(choice)
                if 1 <= choice <= 9:
                    if self.board.is_field_free(choice):
                        print("good number")
                        self.board.add_sign(player, choice)
                        break
                    else:
                        print("The spot is already taken")
                else:
                    print("error404. the number has to be between 1 through 9, dummy")
            else:
                print("error404. that is not a number, bitch")
            choice = None


class Player:
    def __init__(self, nickname, sign, nature):
        self.nickname = nickname
        self.sign = sign
        self.nature = nature  # computer of human


class Board:
    def __init__(self):
        self.fields = []

    def initialize(self):
        for row in range(3):
            for colon in range(3):
                self.fields.append(Sign("_", row, colon))

    def numerate(self):
        for row in range(3):
            for colon in range(3):
                self.fields.append(Sign(str(row * 3 + colon + 1), row, colon))

    def display(self):
        for field in self.fields:
            print(field.character, end="") #end="" means stay in the same in line after print
            if field.colon == 2:
                print()
            else:
                print(" ", end="")
        print()

    def add_sign(self, player, number):
        self.fields[number - 1].character = player.sign  # [number - 1] because human comes from 1, program starts with a zero

    def is_field_free(self, number):
        return self.fields[number - 1].character == "_"

    def three_in_line(self):  # figure out if we have three Xs or Os in row.
        for n in range(3):
            if self.fields[n * 3].character == self.fields[n * 3 + 1].character == self.fields[n * 3 + 2].character != "_":
                return self.fields[n * 3]
            if self.fields[n].character == self.fields[n + 3].character == self.fields[n + 6].character != "_":
                return self.fields[n]
        if self.fields[0].character == self.fields[4].character == self.fields[8].character != "_":
            return self.fields[0]
        if self.fields[2].character == self.fields[4].character == self.fields[6].character != "_":
            return self.fields[2]

class Sign:
    def __init__(self, character, row, colon): #character stands for X, O, _
        self.character = character
        self.row = row
        self.colon = colon
        self.player = None

game = TicTacToe()
game.play()
print(game.player1.nickname, game.player1.sign)
print(game.player2.nickname, game.player2.sign)