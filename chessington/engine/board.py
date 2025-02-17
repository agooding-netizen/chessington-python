"""
A module providing a representation of a chess board. The rules of chess are not implemented - 
this is just a "dumb" board that will let you move pieces around as you like.
"""

from collections import namedtuple
from enum import Enum, auto

from chessington.engine.data import Player, Square
from chessington.engine.pieces import Pawn, Knight, Bishop, Rook, Queen, King

BOARD_SIZE = 8


class Board:
    """
    A representation of the chess board, and the pieces on it.
    """

    def __init__(self, player, board_state):
        self.current_player = Player.WHITE
        self.board = board_state
        self.en_passant_state = None

    @staticmethod
    def empty():
        return Board(Player.WHITE, Board._create_empty_board())

    @staticmethod
    def at_starting_position():
        return Board(Player.WHITE, Board._create_starting_board())

    @staticmethod
    def _create_empty_board():
        return [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    @staticmethod
    def _create_starting_board():

        # Create an empty board
        board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

        # Setup the rows of pawns
        board[1] = [Pawn(Player.WHITE) for _ in range(BOARD_SIZE)]
        board[6] = [Pawn(Player.BLACK) for _ in range(BOARD_SIZE)]

        # Setup the rows of pieces
        piece_row = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        board[0] = list(map(lambda piece: piece(Player.WHITE), piece_row))
        board[7] = list(map(lambda piece: piece(Player.BLACK), piece_row))

        return board

    def set_piece(self, square, piece):
        """
        Places the piece at the given position on the board.
        """
        self.board[square.row][square.col] = piece

    def get_piece(self, square):
        """
        Retrieves the piece from the given square of the board.
        """
        return self.board[square.row][square.col]

    def find_piece(self, piece_to_find):
        """
        Searches for the given piece on the board and returns its square.
        """
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] is piece_to_find:
                    return Square.at(row, col)
        raise Exception('The supplied piece is not on the board')

    def move_piece(self, from_square, to_square):
        """
        Moves the piece from the given starting square to the given destination square.
        """
        moving_piece = self.get_piece(from_square)
        if moving_piece is not None and moving_piece.player == self.current_player:
            self.set_piece(to_square, moving_piece)
            self.promotion_check(to_square, from_square, moving_piece)
            self.execute_en_passant(to_square, from_square, moving_piece)
            self.set_piece(from_square, None)
            self.set_en_passant_state(to_square, from_square, moving_piece)
            self.current_player = self.current_player.opponent()

    def set_en_passant_state(self, to_square, from_square, moving_piece):
        if not isinstance(moving_piece, Pawn):
            self.en_passant_state = None
            return
        if abs(to_square.row - from_square.row) > 1:
            self.en_passant_state = to_square
            return
        self.en_passant_state = None

    def execute_en_passant(self, to_square, from_square, moving_piece):
        if self.en_passant_state is None:
            return
        target_row = 2 if self.en_passant_state.row == 3 else 5
        if isinstance(moving_piece, Pawn) and to_square.col == self.en_passant_state.col and \
                target_row == to_square.row:
            self.set_piece(self.en_passant_state, None)

    def promotion_check(self, to_square, from_square, moving_piece):
        if (to_square.row == 0 or to_square.row == 7) and isinstance(self.get_piece(from_square), Pawn):
            Pawn.pawn_promotion(moving_piece, self, to_square)

    def is_square_empty(self, square):
        if self.get_piece(square) is None:
            return True
        if self.get_piece(square) is not None:
            return False

    @staticmethod
    def does_square_exist(square):
        if 0 <= square.row <= 7 and 0 <= square.col <= 7:
            return True
        else:
            return False

    def check_moves(self, current_square, current_piece, valid_moves, row_direction, col_direction):
        next_square = Square.at(current_square.row + row_direction, current_square.col + col_direction)
        if self.does_square_exist(next_square):
            if self.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not self.is_square_empty(next_square):
                piece = self.get_piece(next_square)
                valid_moves = self.check_for_capture(current_piece, piece, valid_moves, next_square)
        return valid_moves

    def check_moves_multi(self, current_square, current_piece, valid_moves, row_direction, col_direction):
        next_square = Square.at(current_square.row + row_direction, current_square.col + col_direction)
        while self.does_square_exist(next_square):
            if self.is_square_empty(next_square):
                valid_moves.append(next_square)
            elif not self.is_square_empty(next_square):
                piece = self.get_piece(next_square)
                valid_moves = self.check_for_capture(current_piece, piece, valid_moves, next_square)
                break
            next_square = Square.at(next_square.row + row_direction, next_square.col + col_direction)
        return valid_moves

    def check_for_capture(self, current_piece, check_piece, valid_moves, square):
        if check_piece.player != current_piece.player:
            valid_moves.append(square)
            self.get_move_points(square)
        return valid_moves

    def get_move_points(self, target_square):
        piece = self.get_piece(target_square)
        piece_name = type(piece).__name__
        points_dict = {
            "Pawn": 1,
            "Bishop": 3,
            "Knight": 3,
            "Rook": 5,
            "Queen": 9,
            "King": 15
        }
        points = points_dict[piece_name]
        print(piece_name)
        print(points)
        return points

