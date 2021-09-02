class Fourinline:
    def __init__(self, r, c):
        self.board = Board(r, c)
        self.board.initialize()
        self.board_coordinates = Board(1, c)
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
        for turn in range(1, self.board.rows * self.board.colons):
            self.turn = turn
            self.set_player()
            self.board_coordinates.display()
            self.board.display()
            self.do_turn(self.player)
            if self.check_for_winner() is not None:
                self.board.display()
                return
            if turn == self.board.rows * self.board.colons:
                print("it's a draw")

    def check_for_winner(self):
        sign = self.board.four_in_line()
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
            choice = input(player.nickname + ", choose field 1-" + str(self.board.colons) + ": ")
            if choice.isnumeric():
                choice = int(choice)
                if 1 <= choice <= self.board.colons:
                    if self.board.is_field_free(choice):
                        print("good number")
                        self.board.add_sign(player, choice)
                        break
                    else:
                        print("The spot is already taken")
                else:
                    print("error404. the number has to be between 1 through " + str(self.board.colons) + ", dummy")
            else:
                print("error404. that is not a number, bitch")
            choice = None


class Player:
    def __init__(self, nickname, sign, nature):
        self.nickname = nickname
        self.sign = sign
        self.nature = nature  # computer of human


class Board:
    def __init__(self, rows, colons):
        self.rows = rows
        self.colons = colons
        self.fields = []

    def initialize(self):
        for row in range(self.rows):
            for colon in range(self.colons):
                self.fields.append(Sign("_", row, colon))

    def numerate(self):
        for colon in range(self.colons):
            self.fields.append(Sign(str(colon + 1), 0, colon))

    def display(self):
        for field in self.fields:
            print(field.character, end="")  # end="" means stay in the same in line after print
            if field.colon == self.colons - 1:  # index last one
                print()
            else:
                print(" ", end="")
        print()

    def add_sign(self, player, number):
        n = 1
        position = (self.rows - n) * self.colons + (number - 1)
        while position >= 0:
            if self.fields[position].character == "_":
                self.fields[position].character = player.sign
                break
            else:
                n += 1
                position = (self.rows - n) * self.colons + (number - 1)
        else:
            print("This spot is taken")

    def is_field_free(self, number):
        return self.fields[number - 1].character == "_"

    def four_in_line(self):  # figure out if we have three Xs or Os in row.
        for r in range(self.rows):
            for c in range(self.colons):
                if c < self.colons - 3:
                    if \
                            self.fields[r * self.colons + c].character == \
                            self.fields[r * self.colons + c + 1].character == \
                            self.fields[r * self.colons + c + 2].character == \
                            self.fields[r * self.colons + c + 3].character != "_":
                        print("winner bitch")
                        return self.fields[r * self.colons + c]
                if r < self.rows - 3:
                    if \
                            self.fields[r * self.colons + c].character == \
                            self.fields[(r + 1) * self.colons + c].character == \
                            self.fields[(r + 2) * self.colons + c].character == \
                            self.fields[(r + 3) * self.colons + c].character != "_":
                        return self.fields[r * self.colons + c]
                if c < self.colons - 3 and r < self.rows - 3:
                    if \
                            self.fields[r * self.colons + c].character == \
                            self.fields[(r + 1) * self.colons + c + 1].character == \
                            self.fields[(r + 2) * self.colons + c + 2].character == \
                            self.fields[(r + 3) * self.colons + c + 3].character != "_":
                        return self.fields[r * self.colons + c]
                if c < self.colons - 3 and r > 3:
                    if \
                            self.fields[r * self.colons + c].character == \
                            self.fields[(r - 1) * self.colons + c + 1].character == \
                            self.fields[(r - 2) * self.colons + c + 2].character == \
                            self.fields[(r - 3) * self.colons + c + 3].character != "_":
                        return self.fields[r * self.colons + c]

class Sign:
    def __init__(self, character, row, colon):  # character stands for X, O, _
        self.character = character
        self.row = row
        self.colon = colon
        self.player = None


game = Fourinline(6, 7)
game.play()
