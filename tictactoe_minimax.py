from abc import ABC, abstractmethod
from random import randint


def check_index(function):
    def whatever_decorator(other, index):
        if index not in range(other.board_size ** 2):
            print("Error. Index should be between 0 and {}".format(other.board_size ** 2 - 1))
            return
        function(other, index)

    return whatever_decorator


def check_field_availability(function):
    def whatever_decorator(other, index):
        if other.board[index] != "_":
            print("This spot is already taken")
            return
        function(other, index)

    return whatever_decorator


def show_field_numbers(function):
    def whatever_decorator(other, board):
        function(other, other.field_numbers)  # no () because it's a list
        function(other, board)

    return whatever_decorator


class TicTacToe:

    def __init__(self, number_players=1, board_size=3, winner_line=3, player1_symbol="X", player2_symbol="O", empty_field="_"):
        self.board_size = board_size
        self.winner_line = winner_line if winner_line <= board_size else board_size
        self.number_of_fields = self.board_size ** 2
        self.empty_field = empty_field
        self.board = [self.empty_field] * self.number_of_fields
        self.field_numbers = list(range(1, self.number_of_fields + 1))  # 10 is not included
        self.optimize_field_numbers()
        self.player1_symbol = player1_symbol
        self.player2_symbol = player2_symbol
        self.player1 = None
        self.player2 = None
        self.create_players(number_players)
        self.current_player = self.player1  # we always start with the 1st player
        self.current_winner = None

    def num_empty_squares(self):
        return self.board.count(self.empty_field)

    def board_full(self):
        return self.empty_field not in self.board

    def available_moves(self):
        index = 0
        available_moves_list = []
        for field in self.board:
            if field == self.empty_field:
                available_moves_list.append(index)
            index += 1
        return available_moves_list

    def make_move(self, move, symbol):
        self.board[move] = symbol
        # if self.detect_winner():
        #     self.current_winner = self.current_player.get_symbol()

    def optimize_field_numbers(self):
        index = 0
        for number in self.field_numbers:
            number = str(number)
            number_of_digits = len(number)
            highest_number = str(self.number_of_fields)
            number = "0" * (len(highest_number) - number_of_digits) + number
            self.field_numbers[index] = number
            index += 1

        # number_of_digits = 0
        # while self.number_of_fields >= 10 ** number_of_digits:
        #     number_of_digits += 1

    # we have to convert that into a string

    def create_players(self, number_players):
        self.player1 = Human()
        if number_players == 2:
            self.player2 = Human()
        else:
            self.player2 = Computer()
        self.player1.set_symbol(self.player1_symbol)
        self.player2.set_symbol(self.player2_symbol)

    @show_field_numbers
    def show_board(self, board):
        print()
        for row in range(self.board_size):
            for colon in range(self.board_size):
                print(board[row * self.board_size + colon], end=" ")
            print()

    def switch_turn(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def detect_winner(self):
        size = self.board_size
        line = self.winner_line
        empty = self.empty_field
        rows = size - line + 1
        colons = rows
        for row in range(size):  # 3 is not included  # we have to check all the rows and colons
            for colon in range(size - line + 1):
                row_line = self.board[row * size + colon] != empty
                for symbol in range(line):
                    row_line = row_line and self.board[row * size + colon + symbol] == self.board[row * size + colon]
                if row_line:
                    return True
        for row in range(size - line + 1):  # 3 is not included  # we have to check all the rows and colons
            for colon in range(size):
                col_line = self.board[row * size + colon] != empty
                for symbol in range(line):
                    col_line = col_line and self.board[row * size + colon + symbol * size] == self.board[
                        row * size + colon]
                if col_line:
                    return True
        for row in range(size - line + 1):
            for colon in range(size - line + 1):
                diagonal_line = self.board[row * size + colon] != empty
                for symbol in range(line):
                    diagonal_line = diagonal_line and self.board[row * size + colon + symbol * size + symbol] == self.board[
                        row * size + colon]
                if diagonal_line:
                    return True
        for row in range(line - 1, size):
            for colon in range(size - line + 1):
                diagonal_line = self.board[row * size + colon] != empty
                for symbol in range(line):
                    diagonal_line = diagonal_line and self.board[row * size + colon - symbol * size + symbol] == \
                                    self.board[
                                        row * size + colon]
                if diagonal_line:
                    return True
                # if self.board[colon] == self.board[colon + size] == self.board[colon + size * 2] != empty:
                #     return True
                # if self.board[row * size] == self.board[row * size + size + 1] == \
                #         self.board[row * size + size * 2 + 2] != empty:
                #     return True
                # if row > size - 2 and colon < size - 2:
                #     if self.board[row * size] == self.board[row * size - size + 1] == \
                #             self.board[row * size - size * 2 + 2] != empty:
                #         return True
        return False

    # 4 by 4, 5 by 5 ,,,,,mini max
    def play(self):
        while True:
            self.show_board(self.board)
            if self.current_player == self.player1:
                self.player1.move(self)
            else:
                self.player2.smart_move(self)
            if self.detect_winner():
                print("Well done {}, you are the winner".format(self.current_player.get_name()))
                self.show_board(self.board)
                break
            if self.board_full():
                print("It's a tie. No one wins")
                self.show_board(self.board)
                break
            self.switch_turn()

    @check_index
    @check_field_availability
    def place_symbol(self, index):
        self.board[index] = self.current_player.get_symbol()

    def get_number_of_fields(self):
        return self.number_of_fields

    def get_board(self):
        return self.board

    def get_empty_field(self):
        return self.empty_field

    def get_current_player(self):
        return self.current_player


class Player(ABC):
    count = 0

    def __init__(self, name, symbol=None):
        self.name = name
        self.symbol = symbol

    @abstractmethod
    def move(self, game):
        pass

    def get_symbol(self):
        return self.symbol  # this is a field it is why w/o ()

    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_name(self):
        return self.name


class Computer(Player):
    def __init__(self):
        if Player.count < 2:
            super().__init__("Computer")
            Player.count += 1
        else:
            print("There can be only 2 players")

    def move(self, game):
        number_of_fields = game.get_number_of_fields()
        board = game.get_board()
        index = randint(0, number_of_fields - 1)
        while board[index] != game.get_empty_field():
            index = randint(0, number_of_fields - 1)
        game.place_symbol(index)
        print("\n{} puts {} to {}".format(self.name, self.symbol, index + 1))

    def smart_move(self, game):
        result = self.minimax(game, self.symbol)
        #index = self.minimax(game, self.symbol)["position"]
        index = result["position"]
        print(result)
        game.place_symbol(index)
        print("\n{} puts {} to {}".format(self.name, self.symbol, index + 1))

    #why is always zero {'position': 2, 'score': 0}

    def minimax(self, state, player):  # state = game
        max_player = self.symbol  # yourself
        other_player = state.player2_symbol if player == state.player1_symbol else state.player1_symbol
        if state.detect_winner():
            state.current_winner = other_player

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                            state.num_empty_squares() + 1)}
        elif state.board_full():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -11}  # each score should maximize
        else:
            best = {'position': None, 'score': 11}  # each score should minimize
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = state.empty_field
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best


class Human(Player):
    def __init__(self):
        if Player.count < 2:
            name = input("Player {} enter your name: ".format(Player.count + 1))
            super().__init__(name)
            Player.count += 1
        else:
            print("There can be only 2 players")

    def move(self, game):
        while True:
            print()
            player_move = input("{} please, make your move: ".format(self.name))
            if player_move.isnumeric():
                game.place_symbol(int(player_move) - 1)
                break


tictactoe = TicTacToe(1, 3, 3)

tictactoe.play()
