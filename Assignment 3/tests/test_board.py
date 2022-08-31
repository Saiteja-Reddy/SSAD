"""This is used for testing Gameplay class"""

from ..mypkg.boardclass import Board
from ..mypkg.blockclass import BlockBlock

__author__ = 'Saiteja'

class Test_Board(object):
    """Class for testing Board Class"""

    def test_board_empty_initially(self):
        """Method for testing if board is initially empty"""
        board = Board()
        number = 0
        boardgiven = board.getboard()
        for i in range(30):
            for j in range(32):
                if boardgiven[j][i]:
                    number += 1
        assert number == 30*32

    def test_check_piecepos(self):
        """Method for testing the check piece position"""
        board = Board()
        boardin = [[' '] * 30 for _ in range(31)]
        boardin.extend([['X'] * 30])
        board.changeboard(boardin)
        block = BlockBlock()
        block.defineblock()
        block.setpos(29, 15)
        assert board.checkpiecepos(30, 15, block) == 0

    def test_check_piecepos1(self):
        """Method for testing the check piece position if partial block coincides"""
        board = Board()
        boardin = [[' '] * 30 for _ in range(32)]
        boardin[3][2] = boardin[4][2] = boardin[3][3] = boardin [5][3] = 'X'
        board.changeboard(boardin)
        block = BlockBlock()
        block.defineblock()
        assert board.checkpiecepos(2, 3, block) == 0

    def test_check_piecepos2(self):
        """Method for testing the check piece position if complete coincides"""
        board = Board()
        boardin = [[' '] * 30 for _ in range(32)]
        boardin[3][2] = boardin[4][2] = boardin[3][3] = boardin [4][3] = 'X'
        board.changeboard(boardin)
        block = BlockBlock()
        block.defineblock()
        assert board.checkpiecepos(2, 3, block) == 0

    def test_check_piecepos3(self):
        """Method for testing the check piece position if no coincides"""
        board = Board()
        boardin = [[' '] * 30 for _ in range(32)]
        board.changeboard(boardin)
        block = BlockBlock()
        block.defineblock()
        assert board.checkpiecepos(2, 3, block) == 1

    def test_check_piecepos4(self):
        """Method for testing the check piece position if no coincides for block but \
        present in 4*4 of block """
        board = Board()
        boardin = [[' '] * 30 for _ in range(32)]
        boardin[3][2] = 'X'
        board.changeboard(boardin)
        block = BlockBlock()
        block.defineblock()
        assert board.checkpiecepos(2, 3, block) == 1

    def test_fill_piecepos(self):
        """Method for testing the fill piece position"""
        board = Board()
        boardin = [[' '] * 31 for _ in range(31)]
        board.changeboard(boardin)
        block = BlockBlock()
        block.defineblock()
        board.fillpiecepos(1, 15, block)
        # print board.getboard()
        boardout = board.getboard()
        count = 0
        if boardout[1][15] == 'X':
            count += 1
        if boardout[1][16] == 'X':
            count += 1
        if boardout[2][15] == 'X':
            count += 1
        if boardout[2][15] == 'X':
            count += 1
        assert count == 4

    def test_fill_piecepos1(self):
        """Method for testing the fill piece position"""
        board = Board()
        boardin = [[' '] * 31 for _ in range(31)]
        board.changeboard(boardin)
        block = BlockBlock()
        block.defineblock()
        board.fillpiecepos(1, 15, block)
        # print board.getboard()
        boardout = board.getboard()
        count = 0
        if boardout[1][15] == 'X':
            count += 1
        if boardout[1][16] == 'X':
            count += 1
        if boardout[2][15] == 'X':
            count += 1
        if boardout[2][15] == 'X':
            count += 1
        assert count == 4

if __name__ == "__main__":
    T = Test_Board()
    T.test_board_empty_initially()
    T.test_check_piecepos()
    T.test_check_piecepos1()
    T.test_check_piecepos2()
    T.test_check_piecepos3()
    T.test_check_piecepos4()
    T.test_fill_piecepos()