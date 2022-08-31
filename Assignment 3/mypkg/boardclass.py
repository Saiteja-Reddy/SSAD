#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This module builds Board Class"""


class Board(object):
    """Here we are writing the Board Class"""
    def __init__(self):
        """Here we are defining instance variables"""
        self._board = [[' '] * 30 for _ in range(32)]

    def getboard(self):
        """Here we are passing private variables board"""
        return self._board

    def changeboard(self, inputboard):
        """Method to change board"""
        self._board = inputboard

    def checkpiecepos(self, row, col, piece):
        """Method for checking piece position if valid or not"""
        for (xcoord, ycoord) in piece.getcurr():
            self._board[xcoord][ycoord] = ' '
        for i in range(piece.getcoori(0), piece.getcoorf(0) + 1):
            for j in range(piece.getcoori(1), piece.getcoorf(1) + 1):
                xpos = i + row - piece.getcoori(0)
                ypos = j + col - piece.getcoori(1)
                if self._board[xpos][ypos] in ['X', 'W'] \
                        and piece.getblock(i, j) in ['X', '@']:
                    return 0
        return 1

    def fillpiecepos(self, row, col, piece):
        """Method for copying piece contents to board"""
        for (xcoord, ycoord) in piece.getcurr():
            self._board[xcoord][ycoord] = ' '
        piece.resetcurr()
        for i in range(piece.getcoori(0), piece.getcoorf(0) + 1):
            for j in range(piece.getcoori(1), piece.getcoorf(1) + 1):
                xpos = i + row - piece.getcoori(0)
                ypos = j + col - piece.getcoori(1)
                if piece.getblock(i, j) is 'X':
                    self._board[xpos][ypos] = 'X'

                    piece.appendtocurr((xpos, ypos))
                if piece.getblock(i, j) is '@':
                    self._board[xpos][ypos] = '@'

                    piece.appendtocurr((xpos, ypos))

    def clearcolumn(self, number):
        """Method to clear a cloumn by column number for special block"""
        for i in range(32):
            self._board[i][number[1]] = ' '
            self._board[i][number[1] + 1] = ' '
