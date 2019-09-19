"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square


class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):

        current_square = board.find_piece(self)
        row_direction = 0
        start_row = 0
        if self.player == Player.WHITE:
            row_direction = 1
            start_row = 1
        elif self.player == Player.BLACK:
            row_direction = -1
            start_row = 6

        valid_moves = self.check_move_exists(board, row_direction, start_row, current_square)

        return valid_moves

    def check_move_exists(self, board, row_direction, start_row, current_square):
        valid_moves = []
        move = self.move_one_step(board, row_direction, current_square)
        if move:
            valid_moves.append(move)
        move = self.move_two_steps(board, row_direction, current_square, start_row)
        if move:
            valid_moves.append(move)
        move = self.capture_left(board, row_direction, current_square)
        if move:
            valid_moves.append(move)
        move = self.capture_right(board, row_direction, current_square)
        if move:
            valid_moves.append(move)
        return valid_moves

    @staticmethod
    def move_one_step(board, direction, current_square):
        next_square = Square.at(current_square.row + direction, current_square.col)
        if board.does_square_exist(next_square) and board.is_square_empty(next_square):
            return next_square
        return

    @staticmethod
    def move_two_steps(board, direction, current_square, start_row):
        inter_square = Square.at(current_square.row + direction, current_square.col)
        next_square = Square.at(inter_square.row + direction, inter_square.col)
        if current_square.row == start_row and board.is_square_empty(next_square) \
                and board.is_square_empty(inter_square):
            return next_square
        return

    def capture_left(self, board, direction, current_square):
        col_direction = -1
        next_square = Square.at(current_square.row + direction, current_square.col + col_direction)
        if board.does_square_exist(next_square) and not board.is_square_empty(next_square):
            piece = board.get_piece(next_square)
            if piece.player != self.player:
                return next_square
        return

    def capture_right(self, board, direction, current_square):
        col_direction = 1
        next_square = Square.at(current_square.row + direction, current_square.col + col_direction)
        if board.does_square_exist(next_square) and not board.is_square_empty(next_square):
            piece = board.get_piece(next_square)
            if piece.player != self.player:
                return next_square
        return


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):

        current_square = board.find_piece(self)

        move_vectors = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]

        valid_moves = []

        for vector in range(0, len(move_vectors)):
            valid_moves = self.get_moves(board, current_square, valid_moves, move_vectors[vector][0],
                                         move_vectors[vector][1])

        return valid_moves

    def get_moves(self, board, current_square, valid_moves, row_direction, col_direction):

        next_square = Square.at(current_square.row + row_direction, current_square.col + col_direction)
        if board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
        return valid_moves


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):

        current_square = board.find_piece(self)

        move_vectors = [[1, 1], [-1, 1], [-1, -1], [1, -1]]

        valid_moves = []

        for vector in range(0, len(move_vectors)):
            valid_moves = self.get_moves(board, current_square, valid_moves, move_vectors[vector][0],
                                         move_vectors[vector][1])

        return valid_moves

    def get_moves(self, board, current_square, valid_moves, row_direction, col_direction):
        next_square = Square.at(current_square.row + row_direction, current_square.col + col_direction)
        while board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
                break
            next_square = Square.at(next_square.row + row_direction, next_square.col + col_direction)
        return valid_moves


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):

        current_square = board.find_piece(self)

        valid_moves = []

        valid_moves = self.get_moves_up(board, current_square, valid_moves)

        valid_moves = self.get_moves_down(board, current_square, valid_moves)

        valid_moves = self.get_moves_left(board, current_square, valid_moves)

        valid_moves = self.get_moves_right(board, current_square, valid_moves)

        return valid_moves

    def get_moves_up(self, board, current_square, valid_moves):
        next_square = Square.at(current_square.row + 1, current_square.col)
        while board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
                break
            next_square = Square.at(next_square.row + 1, next_square.col)
        return valid_moves

    def get_moves_down(self, board, current_square, valid_moves):
        next_square = Square.at(current_square.row - 1, current_square.col)
        while board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
                break
            next_square = Square.at(next_square.row - 1, next_square.col)
        return valid_moves

    def get_moves_left(self, board, current_square, valid_moves):
        next_square = Square.at(current_square.row, current_square.col - 1)
        while board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
                break
            next_square = Square.at(next_square.row, next_square.col - 1)

        return valid_moves

    def get_moves_right(self, board, current_square, valid_moves):
        next_square = Square.at(current_square.row, current_square.col + 1)
        while board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
                break
            next_square = Square.at(next_square.row, next_square.col + 1)
        return valid_moves


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)

        valid_moves = []

        valid_moves = self.get_moves_up(board, current_square, valid_moves)

        valid_moves = self.get_moves_down(board, current_square, valid_moves)

        valid_moves = self.get_moves_left(board, current_square, valid_moves)

        valid_moves = self.get_moves_right(board, current_square, valid_moves)

        valid_moves = self.get_moves_up_and_right(board, current_square, valid_moves)

        valid_moves = self.get_moves_up_and_left(board, current_square, valid_moves)

        valid_moves = self.get_moves_down_and_right(board, current_square, valid_moves)

        valid_moves = self.get_moves_down_and_left(board, current_square, valid_moves)

        return valid_moves

    def get_moves_up(self, board, current_square, valid_moves):
        next_square = Square.at(current_square.row + 1, current_square.col)
        while board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
                break
            next_square = Square.at(next_square.row + 1, next_square.col)
        return valid_moves

    def get_moves_down(self, board, current_square, valid_moves):
        next_square = Square.at(current_square.row - 1, current_square.col)
        while board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
                break
            next_square = Square.at(next_square.row - 1, next_square.col)
        return valid_moves

    def get_moves_left(self, board, current_square, valid_moves):
        next_square = Square.at(current_square.row, current_square.col - 1)
        while board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
                break
            next_square = Square.at(next_square.row, next_square.col - 1)

        return valid_moves

    def get_moves_right(self, board, current_square, valid_moves):
        next_square = Square.at(current_square.row, current_square.col + 1)
        while board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
                break
            next_square = Square.at(next_square.row, next_square.col + 1)
        return valid_moves

    def get_moves_up_and_right(self, board, current_square, valid_moves):
        next_square = Square.at(current_square.row + 1, current_square.col + 1)
        while board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
                break
            next_square = Square.at(next_square.row + 1, next_square.col + 1)
        return valid_moves

    def get_moves_up_and_left(self, board, current_square, valid_moves):
        next_square = Square.at(current_square.row + 1, current_square.col - 1)
        while board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
                break
            next_square = Square.at(next_square.row + 1, next_square.col - 1)
        return valid_moves

    def get_moves_down_and_right(self, board, current_square, valid_moves):
        next_square = Square.at(current_square.row - 1, current_square.col + 1)
        while board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
                break
            next_square = Square.at(next_square.row - 1, next_square.col + 1)
        return valid_moves

    def get_moves_down_and_left(self, board, current_square, valid_moves):
        next_square = Square.at(current_square.row - 1, current_square.col - 1)
        while board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
                break
            next_square = Square.at(next_square.row - 1, next_square.col - 1)
        return valid_moves


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)

        valid_moves = []

        valid_moves = self.get_moves_up(board, current_square, valid_moves)

        valid_moves = self.get_moves_down(board, current_square, valid_moves)

        valid_moves = self.get_moves_left(board, current_square, valid_moves)

        valid_moves = self.get_moves_right(board, current_square, valid_moves)

        valid_moves = self.get_moves_up_and_right(board, current_square, valid_moves)

        valid_moves = self.get_moves_up_and_left(board, current_square, valid_moves)

        valid_moves = self.get_moves_down_and_right(board, current_square, valid_moves)

        valid_moves = self.get_moves_down_and_left(board, current_square, valid_moves)

        return valid_moves

    def get_moves_up(self, board, current_square, valid_moves):
        next_square = Square.at(current_square.row + 1, current_square.col)
        if board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
        return valid_moves

    def get_moves_down(self, board, current_square, valid_moves):
        next_square = Square.at(current_square.row - 1, current_square.col)
        if board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
        return valid_moves

    def get_moves_left(self, board, current_square, valid_moves):
        next_square = Square.at(current_square.row, current_square.col - 1)
        if board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
        return valid_moves

    def get_moves_right(self, board, current_square, valid_moves):
        next_square = Square.at(current_square.row, current_square.col + 1)
        if board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
        return valid_moves

    def get_moves_up_and_right(self, board, current_square, valid_moves):
        next_square = Square.at(current_square.row + 1, current_square.col + 1)
        if board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
        return valid_moves

    def get_moves_up_and_left(self, board, current_square, valid_moves):
        next_square = Square.at(current_square.row + 1, current_square.col - 1)
        if board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
        return valid_moves

    def get_moves_down_and_right(self, board, current_square, valid_moves):
        next_square = Square.at(current_square.row - 1, current_square.col + 1)
        if board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
        return valid_moves

    def get_moves_down_and_left(self, board, current_square, valid_moves):
        next_square = Square.at(current_square.row - 1, current_square.col - 1)
        if board.does_square_exist(next_square):
            if board.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not board.is_square_empty(next_square):
                piece = board.get_piece(next_square)
                if piece.player != self.player:
                    valid_moves.append(next_square)
        return valid_moves
