from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Pawn, Rook, Bishop, Knight, Queen, King

class TestPawns:

    @staticmethod
    def test_white_pawns_can_move_up_one_square():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(2, 4) in moves

    @staticmethod
    def test_black_pawns_can_move_down_one_square():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(6, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(5, 4) in moves

    @staticmethod
    def test_white_pawn_can_move_up_two_squares_if_not_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) in moves

    @staticmethod
    def test_black_pawn_can_move_down_two_squares_if_not_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(6, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) in moves

    @staticmethod
    def test_white_pawn_cannot_move_up_two_squares_if_already_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        starting_square = Square.at(1, 4)
        board.set_piece(starting_square, pawn)

        intermediate_square = Square.at(2, 4)
        pawn.move_to(board, intermediate_square)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) not in moves

    @staticmethod
    def test_black_pawn_cannot_move_down_two_squares_if_already_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        starting_square = Square.at(6, 4)
        board.set_piece(starting_square, pawn)

        intermediate_square = Square.at(5, 4)
        pawn.move_to(board, intermediate_square)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) not in moves

    @staticmethod
    def test_white_pawn_cannot_move_if_piece_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(5, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_black_pawn_cannot_move_if_piece_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(3, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_pawn_cannot_move_two_squares_if_piece_two_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(6, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert obstructing_square not in moves

    @staticmethod
    def test_black_pawn_cannot_move_two_squares_if_piece_two_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(2, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert obstructing_square not in moves

    @staticmethod
    def test_white_pawn_cannot_move_two_squares_if_piece_one_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(1, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(2, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) not in moves

    @staticmethod
    def test_black_pawn_cannot_move_two_squares_if_piece_one_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(6, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(5, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) not in moves

    @staticmethod
    def test_white_pawn_cannot_move_at_top_of_board():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(7, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_black_pawn_cannot_move_at_bottom_of_board():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(0, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_pawns_can_capture_diagonally():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        enemy1 = Pawn(Player.BLACK)
        enemy1_square = Square.at(4, 5)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.BLACK)
        enemy2_square = Square.at(4, 3)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves

    @staticmethod
    def test_black_pawns_can_capture_diagonally():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        enemy1 = Pawn(Player.WHITE)
        enemy1_square = Square.at(2, 5)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.WHITE)
        enemy2_square = Square.at(2, 3)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves

    @staticmethod
    def test_white_pawns_cannot_move_diagonally_except_to_capture():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        friendly = Pawn(Player.WHITE)
        friendly_square = Square.at(4, 5)
        board.set_piece(friendly_square, friendly)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 3) not in moves
        assert Square.at(4, 5) not in moves

    @staticmethod
    def test_black_pawns_cannot_move_diagonally_except_to_capture():

         # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        friendly = Pawn(Player.BLACK)
        friendly_square = Square.at(2, 5)
        board.set_piece(friendly_square, friendly)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) not in moves
        assert Square.at(2, 5) not in moves

class TestRooks:

    @staticmethod
    def test_rooks_cannot_move_off_the_board():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(0, 0)
        board.set_piece(rook_square, rook)

        friendly_1 = Pawn(Player.WHITE)
        friendly_1_square = Square.at(1, 0)
        board.set_piece(friendly_1_square, friendly_1)

        friendly_2 = Pawn(Player.WHITE)
        friendly_2_square = Square.at(0, 1)
        board.set_piece(friendly_2_square, friendly_2)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_rooks_can_move_vertically():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(3, 4)
        board.set_piece(rook_square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(0, 4) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(2, 4) in moves
        assert Square.at(4, 4) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(6, 4) in moves
        assert Square.at(7, 4) in moves

    @staticmethod
    def test_rooks_can_move_horizontally():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(3, 4)
        board.set_piece(rook_square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(3, 0) in moves
        assert Square.at(3, 1) in moves
        assert Square.at(3, 2) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 5) in moves
        assert Square.at(3, 6) in moves
        assert Square.at(3, 7) in moves

    @staticmethod
    def test_rooks_cannot_move_vertically_through_pieces():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(4, 4)
        board.set_piece(rook_square, rook)

        enemy_1 = Pawn(Player.BLACK)
        enemy_1_square = Square.at(6, 4)
        board.set_piece(enemy_1_square, enemy_1)

        enemy_2 = Pawn(Player.BLACK)
        enemy_2_square = Square.at(3, 4)
        board.set_piece(enemy_2_square, enemy_2)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(7, 4) not in moves
        assert Square.at(2, 4) not in moves

    @staticmethod
    def test_rooks_cannot_move_horizontally_through_pieces():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(4, 4)
        board.set_piece(rook_square, rook)

        enemy_1 = Pawn(Player.BLACK)
        enemy_1_square = Square.at(4, 3)
        board.set_piece(enemy_1_square, enemy_1)

        enemy_2 = Pawn(Player.BLACK)
        enemy_2_square = Square.at(4, 6)
        board.set_piece(enemy_2_square, enemy_2)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(4, 7) not in moves
        assert Square.at(4, 2) not in moves

    @staticmethod
    def test_rooks_can_capture_vertically():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(4, 4)
        board.set_piece(rook_square, rook)

        enemy_1 = Pawn(Player.BLACK)
        enemy_1_square = Square.at(6, 4)
        board.set_piece(enemy_1_square, enemy_1)

        enemy_2 = Pawn(Player.BLACK)
        enemy_2_square = Square.at(3, 4)
        board.set_piece(enemy_2_square, enemy_2)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(6, 4) in moves
        assert Square.at(3, 4) in moves

    @staticmethod
    def test_rooks_can_capture_horizontally():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(4, 4)
        board.set_piece(rook_square, rook)

        enemy_1 = Pawn(Player.BLACK)
        enemy_1_square = Square.at(4, 3)
        board.set_piece(enemy_1_square, enemy_1)

        enemy_2 = Pawn(Player.BLACK)
        enemy_2_square = Square.at(4, 6)
        board.set_piece(enemy_2_square, enemy_2)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(4, 6) in moves
        assert Square.at(4, 3) in moves

class TestBishops:

    @staticmethod
    def test_bishop_cannot_move_off_board():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        bishop_square = Square.at(0, 0)
        board.set_piece(bishop_square, bishop)

        friendly = Pawn(Player.WHITE)
        friendly_square = Square.at(1, 1)
        board.set_piece(friendly_square, friendly)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_bishop_cannot_move_through_pieces_up_and_right():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        bishop_square = Square.at(4, 4)
        board.set_piece(bishop_square, bishop)

        friendly = Pawn(Player.WHITE)
        friendly_square = Square.at(5, 5)
        board.set_piece(friendly_square, friendly)
        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(6, 6) not in moves

    @staticmethod
    def test_bishop_cannot_move_through_pieces_up_and_left():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        bishop_square = Square.at(4, 4)
        board.set_piece(bishop_square, bishop)

        friendly = Pawn(Player.WHITE)
        friendly_square = Square.at(5, 3)
        board.set_piece(friendly_square, friendly)
        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(6, 2) not in moves

    @staticmethod
    def test_bishop_cannot_move_through_pieces_down_and_right():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        bishop_square = Square.at(4, 4)
        board.set_piece(bishop_square, bishop)

        friendly = Pawn(Player.WHITE)
        friendly_square = Square.at(3, 5)
        board.set_piece(friendly_square, friendly)
        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(2, 6) not in moves

    @staticmethod
    def test_bishop_cannot_move_through_pieces_down_and_left():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        bishop_square = Square.at(4, 4)
        board.set_piece(bishop_square, bishop)

        friendly = Pawn(Player.WHITE)
        friendly_square = Square.at(3, 3)
        board.set_piece(friendly_square, friendly)
        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(2, 2) not in moves

    @staticmethod
    def test_bishop_can_move_up_and_right():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        bishop_square = Square.at(4, 4)
        board.set_piece(bishop_square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(5, 5) in moves
        assert Square.at(6, 6) in moves
        assert Square.at(7, 7) in moves

    @staticmethod
    def test_bishop_can_move_up_and_left():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        bishop_square = Square.at(4, 4)
        board.set_piece(bishop_square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(5, 3) in moves
        assert Square.at(6, 2) in moves
        assert Square.at(7, 1) in moves

    @staticmethod
    def test_bishop_can_move_down_and_right():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        bishop_square = Square.at(4, 4)
        board.set_piece(bishop_square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(3, 5) in moves
        assert Square.at(2, 6) in moves
        assert Square.at(1, 7) in moves

    @staticmethod
    def test_bishop_can_move_down_and_left():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        bishop_square = Square.at(4, 4)
        board.set_piece(bishop_square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(3, 3) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(1, 1) in moves
        assert Square.at(0, 0) in moves

    @staticmethod
    def test_bishop_can_capture_up_and_right():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        bishop_square = Square.at(4, 4)
        board.set_piece(bishop_square, bishop)

        enemy = Pawn(Player.BLACK)
        enemy_square = Square.at(6, 6)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(6, 6) in moves

    @staticmethod
    def test_bishop_can_capture_up_and_left():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        bishop_square = Square.at(4, 4)
        board.set_piece(bishop_square, bishop)

        enemy = Pawn(Player.BLACK)
        enemy_square = Square.at(6, 2)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(6, 2) in moves

    @staticmethod
    def test_bishop_can_capture_down_and_right():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        bishop_square = Square.at(4, 4)
        board.set_piece(bishop_square, bishop)

        enemy = Pawn(Player.BLACK)
        enemy_square = Square.at(2, 6)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(2, 6) in moves

    @staticmethod
    def test_bishop_can_capture_down_and_left():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        bishop_square = Square.at(4, 4)
        board.set_piece(bishop_square, bishop)

        enemy = Pawn(Player.BLACK)
        enemy_square = Square.at(2, 2)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(2, 2) in moves

class TestKnights:

    @staticmethod
    def test_knight_cannot_move_to_friendly_square():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        knight_square = Square.at(4, 4)
        board.set_piece(knight_square, knight)

        friendly = Pawn(Player.WHITE)
        friendly_square = Square.at(5, 6)
        board.set_piece(friendly_square, friendly)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(5, 6) not in moves

    @staticmethod
    def test_knight_can_move_in_an_l_up_right():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        knight_square = Square.at(4, 4)
        board.set_piece(knight_square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(6, 5) in moves

    @staticmethod
    def test_knight_can_move_in_an_l_right_up():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        knight_square = Square.at(4, 4)
        board.set_piece(knight_square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(5, 6) in moves

    @staticmethod
    def test_knight_can_move_in_an_l_right_down():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        knight_square = Square.at(4, 4)
        board.set_piece(knight_square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(3, 6) in moves

    @staticmethod
    def test_knight_can_move_in_an_l_down_right():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        knight_square = Square.at(4, 4)
        board.set_piece(knight_square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(2, 5) in moves

    @staticmethod
    def test_knight_can_move_in_an_l_down_left():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        knight_square = Square.at(4, 4)
        board.set_piece(knight_square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) in moves

    @staticmethod
    def test_knight_can_move_in_an_l_left_down():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        knight_square = Square.at(4, 4)
        board.set_piece(knight_square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(3, 2) in moves

    @staticmethod
    def test_knight_can_move_in_an_l_left_up():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        knight_square = Square.at(4, 4)
        board.set_piece(knight_square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(5, 2) in moves

    @staticmethod
    def test_knight_can_move_in_an_l_up_left():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        knight_square = Square.at(4, 4)
        board.set_piece(knight_square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(6, 3) in moves

    @staticmethod
    def test_knights_can_capture():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        knight_square = Square.at(4, 4)
        board.set_piece(knight_square, knight)

        enemy = Pawn(Player.BLACK)
        enemy_square = Square.at(6, 5)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(6, 5) in moves

    @staticmethod
    def test_knights_cannot_move_off_board():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        knight_square = Square.at(0, 0)
        board.set_piece(knight_square, knight)

        friendly_1 = Pawn(Player.WHITE)
        friendly_1_square = Square.at(2, 1)
        board.set_piece(friendly_1_square, friendly_1)

        friendly_2 = Pawn(Player.WHITE)
        friendly_2_square = Square.at(1, 2)
        board.set_piece(friendly_2_square, friendly_2)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert len(moves) == 0


class TestQueens:
    @staticmethod
    def test_queens_cannot_move_off_the_board():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        queen_square = Square.at(0, 0)
        board.set_piece(queen_square, queen)

        friendly_1 = Pawn(Player.WHITE)
        friendly_1_square = Square.at(1, 0)
        board.set_piece(friendly_1_square, friendly_1)

        friendly_2 = Pawn(Player.WHITE)
        friendly_2_square = Square.at(0, 1)
        board.set_piece(friendly_2_square, friendly_2)

        friendly_3 = Pawn(Player.WHITE)
        friendly_3_square = Square.at(1,1)
        board.set_piece(friendly_3_square, friendly_3)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_queens_can_move_vertically():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        queen_square = Square.at(3, 4)
        board.set_piece(queen_square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(0, 4) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(2, 4) in moves
        assert Square.at(4, 4) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(6, 4) in moves
        assert Square.at(7, 4) in moves

    @staticmethod
    def test_queens_can_move_horizontally():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        queen_square = Square.at(3, 4)
        board.set_piece(queen_square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(3, 0) in moves
        assert Square.at(3, 1) in moves
        assert Square.at(3, 2) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 5) in moves
        assert Square.at(3, 6) in moves
        assert Square.at(3, 7) in moves

    @staticmethod
    def test_queens_cannot_move_vertically_through_pieces():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        queen_square = Square.at(4, 4)
        board.set_piece(queen_square, queen)

        enemy_1 = Pawn(Player.BLACK)
        enemy_1_square = Square.at(6, 4)
        board.set_piece(enemy_1_square, enemy_1)

        enemy_2 = Pawn(Player.BLACK)
        enemy_2_square = Square.at(3, 4)
        board.set_piece(enemy_2_square, enemy_2)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(7, 4) not in moves
        assert Square.at(2, 4) not in moves

    @staticmethod
    def test_queens_cannot_move_horizontally_through_pieces():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        queen_square = Square.at(4, 4)
        board.set_piece(queen_square, queen)

        enemy_1 = Pawn(Player.BLACK)
        enemy_1_square = Square.at(4, 3)
        board.set_piece(enemy_1_square, enemy_1)

        enemy_2 = Pawn(Player.BLACK)
        enemy_2_square = Square.at(4, 6)
        board.set_piece(enemy_2_square, enemy_2)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(4, 7) not in moves
        assert Square.at(4, 2) not in moves

    @staticmethod
    def test_queens_can_capture_vertically():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        queen_square = Square.at(4, 4)
        board.set_piece(queen_square, queen)

        enemy_1 = Pawn(Player.BLACK)
        enemy_1_square = Square.at(6, 4)
        board.set_piece(enemy_1_square, enemy_1)

        enemy_2 = Pawn(Player.BLACK)
        enemy_2_square = Square.at(3, 4)
        board.set_piece(enemy_2_square, enemy_2)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(6, 4) in moves
        assert Square.at(3, 4) in moves

    @staticmethod
    def test_queens_can_capture_horizontally():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        queen_square = Square.at(4, 4)
        board.set_piece(queen_square, queen)

        enemy_1 = Pawn(Player.BLACK)
        enemy_1_square = Square.at(4, 3)
        board.set_piece(enemy_1_square, enemy_1)

        enemy_2 = Pawn(Player.BLACK)
        enemy_2_square = Square.at(4, 6)
        board.set_piece(enemy_2_square, enemy_2)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(4, 6) in moves
        assert Square.at(4, 3) in moves


class TestKings:

    @staticmethod
    def test_kings_cannot_move_off_the_board():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(0, 0)
        board.set_piece(king_square, king)

        friendly_1 = Pawn(Player.WHITE)
        friendly_1_square = Square.at(1, 0)
        board.set_piece(friendly_1_square, friendly_1)

        friendly_2 = Pawn(Player.WHITE)
        friendly_2_square = Square.at(0, 1)
        board.set_piece(friendly_2_square, friendly_2)

        friendly_3 = Pawn(Player.WHITE)
        friendly_3_square = Square.at(1,1)
        board.set_piece(friendly_3_square, friendly_3)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_kings_can_capture():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(4, 4)
        board.set_piece(king_square, king)

        enemy_1 = Pawn(Player.BLACK)
        enemy_1_square = Square.at(4, 3)
        board.set_piece(enemy_1_square, enemy_1)

        enemy_2 = Pawn(Player.BLACK)
        enemy_2_square = Square.at(3, 4)
        board.set_piece(enemy_2_square, enemy_2)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(4, 3) in moves
        assert Square.at(3, 4) in moves


    @staticmethod
    def test_kings_cannot_move_to_friendly_square():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(4, 4)
        board.set_piece(king_square, king)

        friendly_1 = Pawn(Player.BLACK)
        friendly_1_square = Square.at(4, 3)
        board.set_piece(friendly_1_square, friendly_1)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(4, 3) not in moves

    @staticmethod
    def test_kings_can_move_one_step_up():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(4, 4)
        board.set_piece(king_square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(5, 4) in moves

    @staticmethod
    def test_kings_can_move_one_step_up_and_right():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(4, 4)
        board.set_piece(king_square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(5, 5) in moves

    @staticmethod
    def test_kings_can_move_one_step_right():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(4, 4)
        board.set_piece(king_square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(4, 5) in moves

    @staticmethod
    def test_kings_can_move_one_step_down_right():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(4, 4)
        board.set_piece(king_square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(3, 5) in moves

    @staticmethod
    def test_kings_can_move_one_step_down():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(4, 4)
        board.set_piece(king_square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) in moves

    @staticmethod
    def test_kings_can_move_one_step_down_and_left():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(4, 4)
        board.set_piece(king_square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(3, 3) in moves

    @staticmethod
    def test_kings_can_move_one_step_left():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(4, 4)
        board.set_piece(king_square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(4, 3) in moves

    @staticmethod
    def test_kings_can_move_one_step_up_and_left():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(4, 4)
        board.set_piece(king_square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(5, 3) in moves
