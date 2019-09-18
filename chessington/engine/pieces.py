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
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []