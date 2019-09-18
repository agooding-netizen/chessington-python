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
        if self.player == Player.WHITE:
            next_square = Square.at(current_square.row + 1, current_square.col)
            if current_square.row == 1:
                next_square_two_step = Square.at(current_square.row + 2, current_square.col)
                return [next_square, next_square_two_step]
            return [next_square]

        if self.player == Player.BLACK:
            next_square = Square.at(current_square.row - 1, current_square.col)
            if current_square.row == 6:
                next_square_two_step = Square.at(current_square.row - 2, current_square.col)
                return [next_square, next_square_two_step]
            return [next_square]


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
        find_piece
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