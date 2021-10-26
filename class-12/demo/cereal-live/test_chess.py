from chess import ChessBoard


def test_is_under_attack():
    board = ChessBoard()
    board.add_blue(0, 1)
    board.add_red(0, 7)

    actual = board.is_under_attack()
    assert actual == True
