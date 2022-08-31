#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This is used for testing Block class"""
from random import randrange
from ..mypkg.gameplayclass import Gameplay
from ..mypkg.blockclass import *

__author__ = 'Saiteja'

rotatedshapes = {
    BlockLine: [(' ', ' ', 'X', ' '), (' ', ' ', 'X', ' '), (' ', ' ', \
                'X', ' '), (' ', ' ', 'X', ' ')],
    BlockBlock: [(' ', ' ', ' ', ' '), (' ', 'X', 'X', ' '), (' ', 'X', \
                 'X', ' '), (' ', ' ', ' ', ' ')],
    BlockZ: [(' ', ' ', ' ', ' '), (' ', ' ', 'X', ' '), (' ', 'X', 'X' \
             , ' '), (' ', 'X', ' ', ' ')],
    BlockS: [(' ', ' ', ' ', ' '), (' ', 'X', ' ', ' '), (' ', 'X', 'X' \
             , ' '), (' ', ' ', 'X', ' ')],
    BlockL: [(' ', ' ', ' ', ' '), (' ', 'X', 'X', ' '), (' ', 'X', ' ' \
             , ' '), (' ', 'X', ' ', ' ')],
    BlockJ: [(' ', ' ', ' ', ' '), (' ', 'X', ' ', ' '), (' ', 'X', ' ' \
             , ' '), (' ', 'X', 'X', ' ')],
    BlockT: [(' ', ' ', ' ', ' '), (' ', ' ', 'X', ' '), (' ', 'X', 'X' \
             , ' '), (' ', ' ', 'X', ' ')],
    BlockSpecial: [(' ', ' ', ' ', ' '), (' ', '@', '@', ' '), (' ', '@' \
                   , '@', ' '), (' ', ' ', ' ', ' ')],
    }

class Test_Block(object):
    """Module for testing Block Class"""

    def test_block_initial_position(self):
        """Method for testing for initial position at top"""
        block = Block()
        assert block.getpos() == (-1, 15)

    def test_block_rotate(self):
        """Method for testing for correct rotation"""
        blocks = {
            1: BlockLine,
            2: BlockBlock,
            3: BlockZ,
            4: BlockS,
            5: BlockL,
            6: BlockJ,
            7: BlockT,
            8: BlockSpecial,
            }

        for i in range(1, 9):
            gameplay = Gameplay()
            block = blocks[i]()
            block.defineblock()

            block.rotate(gameplay)

            assert block.getblockshape() == rotatedshapes[blocks[i]]
            del block
            del gameplay

    def test_block_rotate1(self):
        """ Rotate left corners """
        gameplay = Gameplay()
        block = BlockLine()
        block.defineblock()
        block.draw(gameplay)
        block.rotate(gameplay)
        block.setpos(1,0)
        block.fill(gameplay)
        assert block.rotate(gameplay) == 1

    def test_block_rotate2(self):
        """ Rotate right corners """
        gameplay = Gameplay()
        block = BlockLine()
        block.defineblock()
        block.draw(gameplay)
        block.rotate(gameplay)
        block.setpos(1,29)
        block.fill(gameplay)
        assert block.rotate(gameplay) == 0

    def test_block_rotate3(self):
        """ Rotate if already present block to left"""
        gameplay = Gameplay()
        block = BlockLine()
        block.defineblock()
        boardin = [[' '] * 30 for _ in range(32)]
        for i in range(32):
            boardin[i][0] = 'X'
        block.draw(gameplay)
        block.rotate(gameplay)
        block.setpos(1,29)
        block.fill(gameplay)
        assert block.rotate(gameplay) == 0

    def test_block_rotate4(self):
        """ Rotate if already present block to right """
        gameplay = Gameplay()
        block = BlockLine()
        block.defineblock()
        boardin = [[' '] * 30 for _ in range(32)]
        for i in range(32):
            boardin[i][29] = 'X'
        block.draw(gameplay)
        block.rotate(gameplay)
        block.setpos(1,29)
        block.fill(gameplay)
        assert block.rotate(gameplay) == 0

    def test_block_movedown(self):
        """Method for testing for correct move down"""
        gameplay = Gameplay()
        block = BlockLine()
        block.defineblock()
        block.draw(gameplay)
        assert block.getpos() == (0, 15)
        block.draw(gameplay)
        inishape = block.getblockshape()
        assert inishape == block.getblockshape()
        assert block.getpos() == (1, 15)

    def test_block_movedown_belowblock(self):
        """Method for testing for move down if below there is a block"""
        gameplay = Gameplay()
        block = BlockLine()
        block.defineblock()
        boardin = [[' '] * 30 for _ in range(31)]
        boardin.extend([['X'] * 29 , [' ']])
        gameplay.changeboard(boardin)
        block.draw(gameplay)
        block.goend(gameplay)
        inishape = block.getblockshape()
        assert inishape == block.getblockshape()
        assert block.getpos() == (30, 15)

    def test_block_moveleft(self):
        """Method for testing for correct move left"""
        gameplay = Gameplay()
        block = BlockLine()
        block.defineblock()
        block.moveleft(gameplay)
        assert block.getpos() == (-1, 14)
        block.moveleft(gameplay)
        inishape = block.getblockshape()
        assert inishape == block.getblockshape()
        assert block.getpos() == (-1, 13)

    def test_block_moveleft_leftblock(self):
        """Method for testing for move left if left there is a block"""
        gameplay = Gameplay()
        block = BlockLine()
        block.defineblock()
        boardin = [[' '] * 30 for _ in range(32)]
        for i in range(32):
            boardin[i][14] = 'X'
        gameplay.changeboard(boardin)
        block.draw(gameplay)
        block.moveleft(gameplay)
        block.moveleft(gameplay)
        inishape = block.getblockshape()
        assert inishape == block.getblockshape()
        assert block.getpos() == (0, 15)

    def test_block_moveright(self):
        """Method for testing for correct move right"""
        gameplay = Gameplay()
        block = BlockLine()
        block.defineblock()
        block.moveright(gameplay)
        assert block.getpos() == (-1, 16)
        block.moveright(gameplay)
        inishape = block.getblockshape()
        assert inishape == block.getblockshape()
        assert block.getpos() == (-1, 17)

    def test_block_moveright_rightblock(self):
        """Method for testing for move down if below there is a block"""
        gameplay = Gameplay()
        block = BlockLine()
        block.defineblock()
        boardin = [[' '] * 30 for _ in range(32)]
        for i in range(32):
            boardin[i][16] = 'X'
        gameplay.changeboard(boardin)
        block.draw(gameplay)
        block.moveright(gameplay)
        block.moveright(gameplay)
        inishape = block.getblockshape()
        assert inishape == block.getblockshape()
        assert block.getpos() == (-1, 17)

    def test_block_drop(self):
        """Method for testing for correct move drop"""
        gameplay = Gameplay()
        block = BlockLine()
        block.defineblock()
        block.goend(gameplay)
        inishape = block.getblockshape()
        assert inishape == block.getblockshape()
        assert block.getpos() == (31, 15)

    def test_block_drop1(self):
        """Method for testing for correct move drop"""
        gameplay = Gameplay()
        block = BlockLine()
        block.defineblock()
        boardin = [[' '] * 30 for _ in range(32)]
        for i in range(30):
            boardin[31][i] = 'X'
        # print boardin
        gameplay.changeboard(boardin)
        block.goend(gameplay)
        inishape = block.getblockshape()
        assert inishape == block.getblockshape()
        assert block.getpos() == (30, 15)

    def test_movements(self):
        """Method for testing all the combined left-right-rotate movement of the block"""
        movement = ['a', 'd','s']
        moves = 0
        rotations = 0
        gameplay = Gameplay()
        block = BlockLine()
        block.defineblock()
        block.draw(gameplay)
        inishape = block.getblockshape()
        finalshape = inishape
        assert block.getpos() == (0,15)
        for _ in range(0,30000):
            move = movement[randrange(0, 2)]
            currpos = block.getpos()
            if move == 'a':
                try :
                    if gameplay.checkpiecepos(currpos[0],currpos[1]-1,block) and currpos[1] > 0:
                        gameplay.fillpiecepos(currpos[0],currpos[1]-1,block)
                        moves -=1
                        block.moveleft(gameplay)
                except IndexError:
                    pass
            elif move == 's':
                block.rotate(gameplay)
                rotations += 1
            else:
                try:
                    if gameplay.checkpiecepos(currpos[0],currpos[1]+1,block) and currpos[1] < 29:
                        gameplay.fillpiecepos(currpos[0],currpos[1]+1,block)
                        moves +=1
                        block.moveright(gameplay)
                except IndexError:
                    pass
        for _ in range(rotations):
            finalshape = list(zip(*inishape[::-1]))
        assert finalshape == block.getblockshape()
        assert block.getpos() == (0,15+moves)


if __name__ == '__main__':
    T = Test_Block()
    T.test_block_initial_position()
    T.test_block_rotate()
    T.test_block_movedown()
    T.test_block_moveleft()
    T.test_block_moveright()
    T.test_block_drop()
    T.test_movements()
    T.test_block_movedown_belowblock()
    T.test_block_moveleft_leftblock()
    T.test_block_moveright_rightblock()
    T.test_block_rotate1()
    T.test_block_rotate2()
    T.test_block_rotate2()
    T.test_block_rotate4()
    T.test_block_drop1()