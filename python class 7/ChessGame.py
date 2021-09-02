class ChessBoard:
    def __init__(self):
        self.fields = {}
        self.black_field = "◼"
        self.white_field = "◻"
        self.pieces = "♟♜♞♝♛♚♝♞♜♙♖♘♗♕♔♗♘♖"
        self.initialize()
        self.move_history = []
        self.check_check = False
        self.check_mate = False
        self.king_attacker = None
        self.king_under_attack = None
        self.stale_mate_detected = False

    def initialize(self):
        letters = "abcdefgh"
        for ch in letters:
            self.fields[ch] = []
            for _ in range(9):
                self.fields[ch].append("")
        c = 1  # colon number we start with 1
        for colon in self.fields.values():
            for row in range(1, 9):
                if (c + row) % 2 == 0:
                    colon[row] = Field("black", self.black_field, (letters[c - 1], row))
                else:
                    colon[row] = Field("white", self.white_field, (letters[c - 1], row))
            c += 1
        for c in letters:
            self.initialize_piece("black", "pawn", self.pieces[0], c, 7)
            self.initialize_piece("white", "pawn", self.pieces[9], c, 2)
        letter = 0
        for piece in ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]:
            for color in ["white", "black"]:
                self.initialize_piece(color, piece, self.pieces[letter + 1 if color == "black" else letter + 10],\
                                      letters[letter], 1 if color == "white" else 8)
            letter += 1

    def add_move_to_history(self, piece, new_position):
        self.move_history.append((piece.get_color(), piece.get_name(), tuple(piece.get_position()), new_position))

    def get_last_move(self):
        return self.move_history[-1]

    def get_current_player(self):
        if len(self.move_history) % 2 == 0:
            return "white"
        return "black"

    def show_history(self):
        print(self.move_history)

    def initialize_piece(self, color, name, icon, letter, number):
        piece = Piece(color, name, icon, [letter, number], (letter, number))
        self.set_valid_moves(piece)
        self.fields[letter][number] = piece

    def __str__(self):
        rows = {}
        for i in range(8, 0, -1):
            rows[i] = []
        for fields in self.fields.values():  # values what inside [] in self.fields
            for field in range(1, 9):
                rows[field].append(fields[field])
        board_string = ""
        for row in rows.values():
            for field in row:
                board_string += field.get_icon() + "\t"
            board_string = board_string[:-1] + "\n"
        return board_string

    def set_king_moves(self):
        moves = []
        for r in range(-1, 2):
            for c in range(-1, 2):
                if r == c == 0:
                    continue
                moves.append((r, c))
        return moves

    def set_queen_moves(self):
        moves = []
        for r in range(-7, 8):
            for c in range(-7, 8):
                if r == c == 0:  # this line means the queen cannot move to the same position.
                    continue
                if abs(r) == abs(c) or r == 0 or c == 0:
                    moves.append((r, c))
        return moves

    def set_bishop_moves(self):
        moves = []
        for r in range(-7, 8):
            for c in range(-7, 8):
                if r == c == 0:
                    continue
                if abs(r) == abs(c):  # abs absolute value , compare only values, don't care about numbers
                    moves.append((r, c))
        return moves

    def set_rook_moves(self):
        moves = []
        for r in range(-7, 8):
            for c in range(-7, 8):
                if r == c == 0:
                    continue
                if r == 0 or c == 0:
                    moves.append((r, c))
        return moves

    def set_knight_moves(self):
        moves = []
        for r in range(-2, 3):
            for c in range(-2, 3):
                if r == c == 0:
                    continue
                if (abs(r) == 2 and abs(c) == 1) or (abs(r) == 1 and abs(c) == 2):
                    moves.append((r, c))
        return moves

    def set_pawn_moves(self):
        moves = []
        for r in range(-1, 2):
            for c in range(-1, 2):
                if r == c == 0:
                    continue
                if abs(r) == abs(c):
                    moves.append((r, c))
        for r in range(-2, 3):
            if r == 0:
                continue
            else:
                moves.append((r, 0))
        return moves

    def set_valid_moves(self, piece):
        if piece.get_name() == "king":
            piece.set_valid_moves(self.set_king_moves())
        if piece.get_name() == "queen":
            piece.set_valid_moves(self.set_queen_moves())
        if piece.get_name() == "bishop":
            piece.set_valid_moves(self.set_bishop_moves())
        if piece.get_name() == "rook":
            piece.set_valid_moves(self.set_rook_moves())
        if piece.get_name() == "knight":
            piece.set_valid_moves(self.set_knight_moves())
        if piece.get_name() == "pawn":
            piece.set_valid_moves(self.set_pawn_moves())
            if piece.get_color() == "white":
                piece.set_move_restrictions([(-1, -1), (-1, 0), (-1, 1), (-2, 0)])
            if piece.get_color() == "black":
                piece.set_move_restrictions([(1, -1), (1, 0), (1, 1), (2, 0)])

    def check_valid_turn(self, piece):
        if not isinstance(piece, Piece):
            print("You are moving an empty spot. Use other figure")
            return False
        if len(self.move_history) > 0:
            if self.get_last_move()[0] == piece.get_color():
                print("It is not " + piece.get_color() + "'s turn")
                return False
        else:
            if piece.get_color() == "black":
                print("Black cannot move first")
                return False
        return True

    def pawn_swap(self, piece, move):
        last_row = -1
        next_to_the_last_row = -1
        color = ""
        queen_icon_number = -1
        rook_icon_number = -1
        bishop_icon_number = -1
        knight_icon_number = -1
        if piece.get_color() == "white":
            last_row = 8
            next_to_the_last_row = 7
            color = "white"
            queen_icon_number = 13
            rook_icon_number = 17
            bishop_icon_number = 15
            knight_icon_number = 16
        if piece.get_color() == "black":
            last_row = 1
            next_to_the_last_row = 2
            color = "black"
            queen_icon_number = 4
            rook_icon_number = 1
            bishop_icon_number = 3
            knight_icon_number = 2
        if move[1] == last_row:
            print("You have reached the end of the board. Choose a piece u would like swap for")
            print("1. queen\n2. bishop\n3. rook\n4. knight\n")
            choose = input("Choose your piece for swapping: ")
            choose = int(choose)
            swap_piece = piece
            if choose == 1:
                swap_piece = Piece(color, "queen", self.pieces[queen_icon_number], [move[0], move[1]], ("d", last_row))
            if choose == 2:
                swap_piece = Piece(color, "bishop", self.pieces[bishop_icon_number], [move[0], move[1]], ("c", last_row))
            if choose == 3:
                swap_piece = Piece(color, "rook", self.pieces[rook_icon_number], [move[0], move[1]], ("a", last_row))
            if choose == 4:
                swap_piece = Piece(color, "knight", self.pieces[knight_icon_number], [move[0], move[1]], ("b", last_row))
            self.set_valid_moves(swap_piece)
            self.fields[move[0]][move[1]] = swap_piece
            letters = "abcdefgh"
            if (letters.index(piece.get_colon()) + 1 + piece.get_row()) % 2 == 0:
                self.fields[move[0]][next_to_the_last_row] = \
                    Field("black", self.black_field, (move[0], next_to_the_last_row))
            else:
                self.fields[move[0]][next_to_the_last_row] = \
                    Field("white", self.black_field, (move[0], next_to_the_last_row))
            self.add_move_to_history(piece, move)
            self.show_history()
            return True
        return False

    def pawn_attack_in_front(self, piece, move):
        if self.check_field(move) == "piece" and move[0] == piece.get_colon():
            print("The pawn cannot take over an opponent piece by moving forward")
            return True
        return False

    def pawn_en_passant(self, piece, move):
        if piece.get_color() == "white":
            if piece.get_row() >= 4:
                piece.add_move_restriction((2, 0))
            if piece.get_row() == 5:
                if piece.get_colon() != move[0]:
                    if self.check_field((move[0], piece.get_row())) == "piece":
                        last_move = self.get_last_move()
                        if last_move[3] == (move[0], piece.get_row()):
                            if last_move[0] == "black" and last_move[1] == "pawn":
                                print("En passant")
                                field = self.fields[last_move[3][0]][last_move[3][1]]
                                letters = "abcdefgh"
                                if (letters.index(last_move[3][0]) + 1 + last_move[3][1]) % 2 == 0:
                                    self.fields[last_move[3][0]][last_move[3][1]] = \
                                        Field("black", self.black_field, (last_move[3][0], last_move[3][1]))
                                else:
                                    self.fields[last_move[3][0]][last_move[3][1]] = \
                                        Field("white", self.black_field, (last_move[3][0], last_move[3][1]))
        if piece.get_color() == "black":
            if piece.get_row() <= 5:
                piece.add_move_restriction((-2, 0))
            if piece.get_row() == 4:
                if piece.get_colon() != move[0]:
                    if self.check_field((move[0], piece.get_row())) == "piece":
                        last_move = self.get_last_move()
                        if last_move[3] == (move[0], piece.get_row()):
                            if last_move[0] == "white" and last_move[1] == "pawn":
                                print("En passant")
                                field = self.fields[last_move[3][0]][last_move[3][1]]
                                letters = "abcdefgh"
                                if (letters.index(last_move[3][0]) + 1 + last_move[3][1]) % 2 == 0:
                                    self.fields[last_move[3][0]][last_move[3][1]] = \
                                        Field("black", self.black_field, (last_move[3][0], last_move[3][1]))
                                else:
                                    self.fields[last_move[3][0]][last_move[3][1]] = \
                                        Field("white", self.black_field, (last_move[3][0], last_move[3][1]))
    def check(self, color, spot):
        if color == "white":
            search_for = "black"
        else:
            search_for = "white"
        letters = "abcdefgh"
        for ch in letters:
            for n in range(1, 9):
                if self.check_field((ch, n)) == "piece":
                    piece = self.get_piece((ch, n))
                    if piece.get_color() == search_for:
                        if not piece.get_name() == "knight":
                            new_position = self.relative_coordinates(piece.get_position(), spot)
                            if new_position not in piece.get_valid_moves() or new_position in piece.get_move_restrictions():
                                continue
                            if piece.get_name() == "pawn":
                                if new_position[1] == 0:
                                    continue
                            row_difference = new_position[0]
                            colon_difference = new_position[1]
                            row_difference_sign = 0
                            colon_difference_sign = 0
                            if row_difference != 0:
                                row_difference_sign = row_difference // abs(row_difference)
                            if colon_difference != 0:
                                colon_difference_sign = colon_difference // abs(colon_difference)
                            stopping_point = max(abs(row_difference), abs(colon_difference))
                            current_row = 0
                            current_colon = 0
                            for i in range(1, stopping_point + 1):
                                if row_difference != 0:
                                    current_row += row_difference_sign
                                if colon_difference != 0:
                                    current_colon += colon_difference_sign
                                current_field = self.position_relative_coordinate(piece, (current_row, current_colon))
                                if self.check_field(current_field) == "piece" and i != stopping_point:
                                    break
                                if current_field == spot:
                                    if self.stale_mate():
                                        return True
                                    print(current_field, "Field is under attack by", str(piece))
                                    return True
        return False

    def check_two(self, color, spot):
        if color == "white":
            search_for = "black"
        else:
            search_for = "white"
        letters = "abcdefgh"
        for ch in letters:
            for n in range(1, 9):
                if self.check_field((ch, n)) == "piece":
                    piece = self.get_piece((ch, n))
                    if piece.get_color() == search_for:
                        if not piece.get_name() == "knight":
                            new_position = self.relative_coordinates(piece.get_position(), spot)
                            if new_position not in piece.get_valid_moves() or new_position in piece.get_move_restrictions():
                                continue
                            if piece.get_name() == "pawn":
                                if new_position[1] == 0:
                                    continue
                            row_difference = new_position[0]
                            colon_difference = new_position[1]
                            row_difference_sign = 0
                            colon_difference_sign = 0
                            if row_difference != 0:
                                row_difference_sign = row_difference // abs(row_difference)
                            if colon_difference != 0:
                                colon_difference_sign = colon_difference // abs(colon_difference)
                            stopping_point = max(abs(row_difference), abs(colon_difference))
                            current_row = 0
                            current_colon = 0
                            for i in range(1, stopping_point + 1):
                                if row_difference != 0:
                                    current_row += row_difference_sign
                                if colon_difference != 0:
                                    current_colon += colon_difference_sign
                                current_field = self.position_relative_coordinate(piece, (current_row, current_colon))
                                if self.check_field(current_field) == "piece" and i != stopping_point:
                                    break
                                if current_field == spot:

                                    #print(current_field, "Field is under attack by", str(piece))
                                    return True
        return False
    def stale_mate(self):
        print("stalemate")
        letters = "abcdefgh"
        king = None
        for ch in letters:
            for n in range(1, 9):
                if self.check_field((ch, n)) == "piece":
                    piece = self.get_piece((ch, n))
                    if piece.get_name() == "king" and piece.get_color() == self.get_current_player():
                        king = piece
                        break
        print(king.get_name())
        if king.get_name() == "king":
            king_surrounded = True
            empty_fields = 0
            for mov in king.get_valid_moves():
                letters = "abcdefgh"
                king_colon = letters.index(king.get_colon()) + 1
                king_row = king.get_row()
                potential_colon = king_colon + mov[0]
                potential_row = king_row + mov[1]
                if 1 <= potential_colon <= 8:
                    if 1 <= potential_row <= 8:
                        if self.check_field((letters[potential_colon - 1], potential_row)) == "field":
                            empty_fields = 1
                            if not self.check_two(king.get_color(), (letters[potential_colon - 1], potential_row)):
                                king_surrounded = False
            print(king_surrounded, "after four")
            if empty_fields == 0:
                king_surrounded = False
            print("King is surrounded", king_surrounded)
            if king_surrounded:
                if self.attack_not_possible():
                    self.stale_mate_detected = True
                    return True
        return False

    def attack_not_possible(self):
        letters = "abcdefgh"
        attack_found = False
        for ch in letters:
            for n in range(1, 9):
                if self.check_field((ch, n)) == "piece":
                    piece = self.get_piece((ch, n))
                    if piece.get_color() == self.get_current_player():
                        for mov in piece.get_valid_moves():
                            if mov not in piece.get_move_restrictions():
                                piece_colon = letters.index(piece.get_colon()) + 1
                                piece_row = piece.get_row()
                                potential_colon = piece_colon + mov[0]
                                potential_row = piece_row + mov[1]
                                if 1 <= potential_colon <= 8:
                                    if 1 <= potential_row <= 8:
                                        if self.check_field((letters[potential_colon - 1], potential_row)) == "piece":
                                            potential_target = self.get_piece((letters[potential_colon - 1], potential_row))
                                            if potential_target.get_color() != self.get_current_player():
                                                if abs(potential_colon) == 1 and abs(potential_row) == 1:
                                                    attack_found = True
                                                if potential_target.get_name() == "knight":
                                                    attack_found = True
        return attack_found

    def any_valid_move(self):
        letters = "abcdefgh"
        valid_move_found = False
        for ch in letters:
            for n in range(1, 9):
                if self.check_field((ch, n)) == "piece":
                    piece = self.get_piece((ch, n))
                    if piece.get_color() == self.get_current_player():
                        for mov in piece.get_valid_moves():
                            if mov not in piece.get_move_restrictions():
                                piece_colon = letters.index(piece.get_colon()) + 1
                                piece_row = piece.get_row()
                                potential_colon = piece_colon + mov[0]
                                potential_row = piece_row + mov[1]
                                if 1 <= potential_colon <= 8:
                                    if 1 <= potential_row <= 8:
                                        if self.check_field((letters[potential_colon - 1], potential_row)) == "field":
                                            valid_move_found = True
        return valid_move_found
    def attack_king(self, piece):
        king_under_attack = True
        if piece.get_color() == "white":
            search_for = "black"
        else:
            search_for = "white"
        letters = "abcdefgh"
        for ch in letters:
            for n in range(1, 9):
                if self.check_field((ch, n)) == "piece":
                    king = self.get_piece((ch, n))
                    if king.get_color() == search_for:
                        if king.get_name() == "king":
                            new_position = self.relative_coordinates(piece.get_position(), king.get_position())
                            row_difference = new_position[0]
                            colon_difference = new_position[1]
                            row_difference_sign = 0
                            colon_difference_sign = 0
                            if row_difference != 0:
                                row_difference_sign = row_difference // abs(row_difference)
                            if colon_difference != 0:
                                colon_difference_sign = colon_difference // abs(colon_difference)
                            stopping_point = max(abs(row_difference), abs(colon_difference))
                            current_row = 0
                            current_colon = 0
                            for i in range(1, stopping_point + 1):
                                if row_difference != 0:
                                    current_row += row_difference_sign
                                if colon_difference != 0:
                                    current_colon += colon_difference_sign
                                current_field = self.position_relative_coordinate(piece, (current_row, current_colon))
                                if current_field[1] > 8:
                                    continue
                                if self.check_field(current_field) == "piece" and i != stopping_point:
                                    king_under_attack = False
        if king_under_attack:
            print(new_position, "attack king")
            self.king_attacker = piece
            self.king_under_attack = king
            self.check_check = True

    def king_scouts_danger(self, piece, move):
        return self.check(piece.get_color(), move)


    def castling(self, piece, move):
        king = piece
        king_row = -1
        rook_colon = ""
        if king.get_color() == "white":
            king_row = 1
            king_icon_number = 5
        if king.get_color() == "black":
            king_row = 8
            king_icon_number = 14

        if king.get_row() != king_row or king.get_colon() != "e":
            return False
        if move[1] != king_row or move[0] not in "cg":
            return False
        path = ""
        if move[0] == "c":
            rook_colon = "a"
            path = "bcd"
        if move[0] == "g":
            rook_colon = "h"
            path = "fg"
        if self.check_field((rook_colon, king_row)) == "piece":
            rook = self.get_piece((rook_colon, king_row))
            if rook.get_name() != "rook":
                return False
        for field in path:
            if self.check_field((field, king_row)) == "piece":
                return False
        print(piece.get_colon(), king_row)
        for mv in self.move_history:
            if mv[2] == (king.get_colon(), king_row):
                return False
            if mv[2] == (rook_colon, king_row):
                return False
        for field in king.get_colon() + path:
            if self.check(king.get_color(), (field, king_row)):
                return False
        return True

    def move_piece(self, piece, move):
        #self.check("black", ("d", 5))
        if not self.check_valid_turn(piece):
            return False
        if piece.get_name() == "pawn":
            if self.pawn_swap(piece, move):
                g_o = self.three_fold()
                if g_o:
                    return True
                return False
            if self.pawn_attack_in_front(piece, move):
                return False
            self.pawn_en_passant(piece, move)
        relative_coords = self.relative_coordinates(piece.get_position(), move)
        if piece.get_name() == "king":
            if self.king_scouts_danger(piece, move):
                return False
            if self.castling(piece, move):
                #here we call a method to move both the king and the rook
                print("castling, bitch")
                letters = "abcdefgh"
                if (letters.index(piece.get_colon()) + 1 + piece.get_row()) % 2 == 0:
                    self.fields[piece.get_colon()][piece.get_row()] = Field("black", self.black_field,
                                                                            (letters.index(move[0]) + 1, move[1]))
                else:
                    self.fields[piece.get_colon()][piece.get_row()] = Field("white", self.white_field,
                                                                            (letters.index(move[0]) + 1, move[1]))
                self.add_move_to_history(piece, move)
                piece.set_position(move)
                self.fields[move[0]][move[1]] = piece
                self.show_history()
                g_o = self.three_fold()
                if g_o:
                    return True
                if move[0] == "c":
                    rook_colon = "a"
                    rook_new_colon = "d"
                else:
                    rook_colon = "h"
                    rook_new_colon = "f"
                piece = self.get_piece((rook_colon, move[1]))
                if (letters.index(piece.get_colon()) + 1 + piece.get_row()) % 2 == 0:
                    self.fields[piece.get_colon()][piece.get_row()] = Field("black", self.black_field,
                                                                            (letters.index(rook_new_colon) + 1, move[1]))
                else:
                    self.fields[piece.get_colon()][piece.get_row()] = Field("white", self.white_field,
                                                                            (letters.index(rook_new_colon) + 1, move[1]))
                self.add_move_to_history(piece, move)
                piece.set_position(move)
                self.fields[rook_new_colon][move[1]] = piece
                self.show_history()
                g_o = self.three_fold()
                if g_o:
                    return True
                return False


        if relative_coords not in piece.get_valid_moves() or relative_coords in piece.get_move_restrictions():
            print("That's not a valid move for", piece.get_name())
            return False
        if self.check_field(move) == "piece":
            if self.get_piece(move).get_color() == piece.get_color():
                print("The spot is taken by your other figure")
                return False
        if not piece.get_name() == "knight":
            new_position = self.relative_coordinates(piece.get_position(), move)
            row_difference = new_position[0]
            colon_difference = new_position[1]
            row_difference_sign = 0
            colon_difference_sign = 0
            if row_difference != 0:
                row_difference_sign = row_difference // abs(row_difference)
            if colon_difference != 0:
                colon_difference_sign = colon_difference // abs(colon_difference)
            stopping_point = max(abs(row_difference), abs(colon_difference))
            current_row = 0
            current_colon = 0
            for i in range(1, stopping_point + 1):
                if row_difference != 0:
                    current_row += row_difference_sign
                if colon_difference != 0:
                    current_colon += colon_difference_sign
                current_field = self.position_relative_coordinate(piece, (current_row, current_colon))
                if self.check_field(current_field) == "piece" and i != stopping_point:
                    print("Error! You cannot ride over other pieces")
                    return False
        if self.king_under_attack:
            if piece == self.king_under_attack:
                print("king saved, bitch")
                self.check_check = False
                self.king_attacker = None
                self.king_under_attack = None
            elif not self.king_saved(move):
                print("Your king is under the attack. You must protect him")
                return False
        # else:
        #     if piece.get_name() == "king":
        #         king_surrounded = True
        #         empty_fields = 0
        #         for mov in piece.get_valid_moves():
        #             letters = "abcdefgh"
        #             king_colon = letters.index(piece.get_colon()) + 1
        #             king_row = piece.get_row()
        #             potential_colon = king_colon + mov[0]
        #             potential_row = king_row + mov[1]
        #             if 1 <= potential_colon <= 8:
        #                 if 1 <= potential_row <= 8:
        #                     if self.check_field((letters[potential_colon - 1], potential_row)) == "field":
        #                         empty_fields = 1
        #                         if not self.check(piece.get_color(), (letters[potential_colon - 1], potential_row)):
        #                             king_surrounded = False
        #         if empty_fields == 0:
        #             king_surrounded = False
        #         print("King is surrounded", king_surrounded)
        #         if king_surrounded:
        #             return True

                                #print(letters[potential_colon - 1], potential_row, self.check(piece.get_color(), \
                                                                             #(letters[potential_colon - 1], potential_row)))

        letters = "abcdefgh"
        if (letters.index(piece.get_colon()) + 1 + piece.get_row()) % 2 == 0:
            self.fields[piece.get_colon()][piece.get_row()] = Field("black", self.black_field, (letters.index(move[0]) + 1, move[1]))
        else:
            self.fields[piece.get_colon()][piece.get_row()] = Field("white", self.white_field, (letters.index(move[0]) + 1, move[1]))
        self.add_move_to_history(piece, move)
        piece.set_position(move)
        self.fields[move[0]][move[1]] = piece
        self.show_history()
        g_o = self.three_fold()
        if g_o:
            return True
        self.attack_king(piece)
        return False

    def three_fold(self):
        if len(self.move_history) >= 12:
            if str(self.move_history[-4:]) == str(self.move_history[-8:-4]) == str(self.move_history[-12:-8]):
                print("three fold, bitch")
                return True
        return False

    def king_saved(self, move):
        attacker = self.king_attacker
        print(attacker.get_position(), "###", move)
        if attacker.get_position()[0] == move[0] and attacker.get_position()[1] == move[1]:
            print("king saved, bitch")
            self.check_check = False
            self.king_attacker = None
            self.king_under_attack = None
            return True
        for mv in attacker.valid_moves:
            #print(mv)
            new_position = mv
            if new_position not in attacker.get_valid_moves() or new_position in attacker.get_move_restrictions():
                continue
            #if attacker.get_name() == "pawn":
            #    if new_position[1] == 0:
            #        continue
            row_difference = new_position[0]
            colon_difference = new_position[1]
            row_difference_sign = 0
            colon_difference_sign = 0
            if row_difference != 0:
                row_difference_sign = row_difference // abs(row_difference)
            if colon_difference != 0:
                colon_difference_sign = colon_difference // abs(colon_difference)
            stopping_point = max(abs(row_difference), abs(colon_difference))
            current_row = 0
            current_colon = 0
            for i in range(1, stopping_point + 1):
                if row_difference != 0:
                    current_row += row_difference_sign
                if colon_difference != 0:
                    current_colon += colon_difference_sign
                #print(current_row, current_colon, "+++")
                if current_colon is None:
                    continue
                current_field = self.position_relative_coordinate(attacker, (current_row, current_colon))
                #print(current_field, "***", move)
                if current_field == move and self.spot_that_saves_the_king(move):
                    print("king saved, bitch")
                    self.check_check = False
                    self.king_attacker = None
                    self.king_under_attack = None
                    return True
            #test_position = self.position_relative_coordinate(self.king_attacker, mv)
            #print(test_position)
        return False

    def spot_that_saves_the_king(self, move):
        king_row = self.king_under_attack.get_row()
        king_colon = self.king_under_attack.get_colon()
        attacker_row = self.king_attacker.get_row()
        attacker_colon = self.king_attacker.get_colon()
        if king_colon == attacker_colon == move[0]:
            if move[1] > min(king_row, attacker_row) and move [1] < max(king_row, attacker_row):
                return True
        if king_row == attacker_row == move[1]:
            if move[0] > min(king_colon, attacker_colon) and move [0] < max(king_colon, attacker_colon):
                return True
        letters = "abcdefgh"
        king_colon = letters.index(king_colon) + 1
        attacker_colon = letters.index(attacker_colon) + 1
        move_colon = letters.index(move[0]) + 1
        if abs(king_colon - attacker_colon) == abs(king_row - attacker_row):
            if abs(king_colon - move_colon) == abs(king_row - move[1]):
                if abs(attacker_colon - move_colon) == abs(attacker_row - move[1]):
                    if move_colon > min(king_colon, attacker_colon):
                        if move_colon < max(king_colon, attacker_colon):
                            if move[1] > min(king_row, attacker_row):
                                if move[1] < max(king_row, attacker_row):
                                    return True
        return False



    def relative_coordinates(self, current_position, move):
        letters = "abcdefgh"
        current_colon = letters.index(current_position[0]) + 1
        current_row = current_position[1]
        move_colon = letters.index(move[0]) + 1
        move_row = move[1]
        return move_row - current_row, move_colon - current_colon


    def position_relative_coordinate(self, piece, relative_coordinates):
        position = piece.get_position()
        letters = "abcdefgh"
        current_colon = letters.index(position[0])
        new_colon_index = current_colon + relative_coordinates[1]
        relative_colon = new_colon_index if new_colon_index >= 0 else None
        new_row_index = position[1] + relative_coordinates[0]
        relative_row = new_row_index if new_row_index >= 0 else None
        if relative_colon is None:
            return None, relative_row
        if relative_colon > len(letters)-1:
            return None, relative_row
        return letters[relative_colon], relative_row


    def check_field(self, spot):
        field = self.fields[spot[0]][int(spot[1])]
        if isinstance(field, Piece):  # isinstance will give me true if the thing on the left is object of class on the right
            return "piece"
        return "field"

    def get_piece(self, spot):
        return self.fields[spot[0]][int(spot[1])]


class Field:
    def __init__(self, color, icon, position):
        self.color = color
        self.icon = icon
        self.position = position

    def get_icon(self):
        return self.icon


class Piece:
    def __init__(self, color, name, icon, position, initial_position):
        self.color = color
        self.name = name
        self.icon = icon
        self.position = position
        self.initial_position = initial_position
        self.valid_moves = None
        self.move_restrictions = []

    def __str__(self):
        return self.icon + " " + self.color + " " + self.name + ", " + self.position[0] + str(self.position[1])

    def get_name(self):
        return self.name

    def get_icon(self):
        return self.icon

    def get_valid_moves(self):
        return self.valid_moves

    def set_valid_moves(self, valid_moves):
        self.valid_moves = valid_moves

    def get_move_restrictions(self):
        return self.move_restrictions

    def set_move_restrictions(self, move_restrictions):
        self.move_restrictions = move_restrictions

    def add_move_restriction(self, move):
        self.move_restrictions.append(move)

    def remove_move_restriction(self):
        self.move_restrictions.pop()

    def set_position(self, new_position):
        self.position = list(new_position)

    def get_position(self):
        return self.position

    def get_row(self):
        return self.position[1]

    def get_colon(self):
        return self.position[0]

    def get_color(self):
        return self.color


CB = ChessBoard()
print(CB)
while True:
    #CB.check("black", ("d", 5))
    if CB.check_check:
        print("The {} king is under attack!!!".format(CB.get_current_player()))
    piece = input("Mr/Mrs " + CB.get_current_player() + ", what piece do you want to move? ")
    move = input("Where do you want to move it? ")
    game_over = CB.move_piece(CB.fields[piece[0]][int(piece[1])], (move[0], int(move[1])))
    print(CB)
    if CB.three_fold():
        print("It's a draw, dude.")
    if CB.stale_mate_detected:
        print("It's a stalemate, man.")
        break
    if game_over:
        break
print("Game over")





