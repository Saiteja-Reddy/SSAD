#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This is used for testing Gameplay class"""
from random import randrange
from ..mypkg.gameplayclass import Gameplay
__author__ = 'Saiteja'


class Test_Gameplay(object):
    """Module for testing Gameplay Class"""

    def test_score_initially(self):
        """Method for testing if score is initially zero"""
        gameplay = Gameplay()
        assert gameplay.getscore() == 0

    def test_board_empty_initially(self):
        """Method for testing if board is initially empty"""
        gameplay = Gameplay()
        number = 0
        boardgiven = gameplay.getboard()
        for i in range(30):
            for j in range(32):
                if boardgiven[j][i]:
                    number += 1
        assert number == 30 * 32

    def test_row_full(self):
        """Method for testing if full rows are removed and score is updated"""
        gameplay = Gameplay()
        boardin = [[' '] * 30 for _ in range(31)]
        boardin.extend([['X'] * 30])
        gameplay.changeboard(boardin)
        gameplay.updatescore()

        # print gameplay.getscore()

        assert gameplay.getscore() == 110

    def test_row_full1(self):
        """Method for testing if multiple full rows are removed and score is updated"""
        gameplay = Gameplay()
        boardin = [[' '] * 30 for _ in range(32)]
        for i in range(30):
            boardin[1][i] = 'X'
            boardin[2][i] = 'X'
        gameplay.changeboard(boardin)
        gameplay.updatescore()

        # print gameplay.getscore()
        assert gameplay.getscore() == 210

    def test_addsemifilled(self):
        """Method for testing if add-semifilledrow at bottom is working"""
        gameplay = Gameplay()
        boardin = [[' '] * 30 for _ in range(32)]
        gameplay.changeboard(boardin)
        gameplay.addsemifilled()
        count = 0
        for i in range(30):
            if boardin[29][i] == ' ':
                count += 1
        assert count != 0

    def test_checkrowempty(self):
        """Method for testing if add-walls at is working"""
        gameplay = Gameplay()
        boardin = [[' '] * 30 for _ in range(32)]
        gameplay.changeboard(boardin)
        assert gameplay.checkrowempty() == 1

    def test_change_board(self):
        """Method for testing if change board function is working"""
        gameplay = Gameplay()
        boardin = [[' '] * 30 for _ in range(31)]
        boardin.extend([['X'] * 30])
        gameplay.changeboard(boardin)
        assert gameplay.getboard() == boardin

    def test_game(self):
        """Method for testing a game run"""
        movement = ['a', 'd', 's', ' ']
        moves = 0
        gameplay = Gameplay()
        blockno = randrange(1, 8)
        block = gameplay.newblock(blockno)
        gameover = False

        while not gameover and moves < 1000:
            go_down = block.draw(gameplay)
            gameplay.printboard()
            if go_down == 0:
                if block.getpos()[0] == -1:
                    gameover = True
                    break
                gameplay.updatescore()
                blockno = randrange(1, 8)
                block = gameplay.newblock(blockno)
                block.draw(gameplay)
            takeinput = randrange(0, 2)
            if takeinput == 1:
                move = movement[randrange(0, 4)]
                moves += 1
                if move == 'a':
                    block.moveleft(gameplay)
                elif move == 'd':
                    block.moveright(gameplay)
                elif move == 's':
                    block.rotate(gameplay)
                elif move == ' ':
                    block.goend(gameplay)
                print(move)
        print(gameplay.getscore())
        assert gameplay.getscore() != 0


if __name__ == '__main__':
    T = Test_Gameplay()
    T.test_score_initially()
    T.test_board_empty_initially()
    T.test_change_board()
    T.test_game()
    T.test_row_full()
    T.test_row_full1()
    T.test_score_initially()
    T.test_checkrowempty()
    T.test_addsemifilled()