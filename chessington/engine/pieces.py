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
        valid_moves = []
        move_vectors = []

        if self.player == Player.WHITE:
            row_direction = 1
            start_row = 1
            move_vectors = [[1, 1], [1, -1]]

        elif self.player == Player.BLACK:
            row_direction = -1
            start_row = 6
            move_vectors = [[-1, 1], [-1, -1]]

        valid_moves = self.move_one_step(board, row_direction, current_square, valid_moves)

        valid_moves = self.move_two_steps(board, row_direction, current_square, start_row, valid_moves)

        if len(move_vectors) == 2:
            for vector in range(0, len(move_vectors)):
                valid_moves = self.prawn_capture(board, current_square, valid_moves, move_vectors[vector][0],
                                                 move_vectors[vector][1])

        if board.en_passant_state:
            valid_moves = self.en_passant(board, valid_moves, current_square, row_direction)

        return valid_moves

    @staticmethod
    def move_one_step(board, direction, current_square, valid_moves):
        next_square = Square.at(current_square.row + direction, current_square.col)
        if board.does_square_exist(next_square) and board.is_square_empty(next_square):
            valid_moves.append(next_square)
        return valid_moves

    @staticmethod
    def move_two_steps(board, direction, current_square, start_row, valid_moves):
        inter_square = Square.at(current_square.row + direction, current_square.col)
        next_square = Square.at(inter_square.row + direction, inter_square.col)
        if current_square.row == start_row and board.is_square_empty(next_square) \
                and board.is_square_empty(inter_square):
            valid_moves.append(next_square)
        return valid_moves

    def prawn_capture(self, board, current_square, valid_moves, row_direction, col_direction):
        next_square = Square.at(current_square.row + row_direction, current_square.col + col_direction)
        if board.does_square_exist(next_square) and not board.is_square_empty(next_square):
            piece = board.get_piece(next_square)
            if piece.player != self.player:
                valid_moves.append(next_square)
        return valid_moves

    def pawn_promotion(self, board, square):
        queen = Queen(self.player)
        board.set_piece(square, queen)

    @staticmethod
    def en_passant(board, valid_moves, current_square, row_direction):
        victim_square = board.en_passant_state
        if victim_square.row == current_square.row:
            if victim_square.col == current_square.col + 1:
                next_square = Square.at(current_square.row + row_direction, current_square.col + 1)
                valid_moves.append(next_square)
            if victim_square.col == current_square.col - 1:
                next_square = Square.at(current_square.row + row_direction, current_square.col - 1)
                valid_moves.append(next_square)
        return valid_moves


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):

        current_square = board.find_piece(self)
        current_piece = board.get_piece(current_square)

        move_vectors = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]

        valid_moves = []

        for vector in range(0, len(move_vectors)):
            valid_moves = board.check_moves(board, current_square, current_piece, valid_moves,
                                            move_vectors[vector][0], move_vectors[vector][1])

        return valid_moves


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):

        current_square = board.find_piece(self)
        current_piece = board.get_piece(current_square)

        move_vectors = [[1, 1], [-1, 1], [-1, -1], [1, -1]]

        valid_moves = []

        for vector in range(0, len(move_vectors)):
            valid_moves = board.check_moves_multi(board, current_square, current_piece, valid_moves,
                                                  move_vectors[vector][0], move_vectors[vector][1])

        return valid_moves


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):

        current_square = board.find_piece(self)
        current_piece = board.get_piece(current_square)

        move_vectors = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        valid_moves = []

        for vector in range(0, len(move_vectors)):
            valid_moves = board.check_moves_multi(board, current_square, current_piece, valid_moves,
                                                  move_vectors[vector][0], move_vectors[vector][1])

        return valid_moves


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        current_piece = board.get_piece(current_square)

        move_vectors = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]

        valid_moves = []

        for vector in range(0, len(move_vectors)):
            valid_moves = board.check_moves_multi(board, current_square, current_piece, valid_moves,
                                                  move_vectors[vector][0], move_vectors[vector][1])

        return valid_moves


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        current_piece = board.get_piece(current_square)

        valid_moves = []

        move_vectors = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]

        for vector in range(0, len(move_vectors)):
            valid_moves = board.check_moves(board, current_square, current_piece, valid_moves,
                                            move_vectors[vector][0], move_vectors[vector][1])

        return valid_moves
