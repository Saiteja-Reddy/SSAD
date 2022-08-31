    #!/usr/bin/python
# -*- coding: utf-8 -*-
"""This module builds Block Classes"""

from __future__ import print_function


class Block(object):
    """class for all blocks"""
    def __init__(self):
        """Here we are defining instance variables"""
        self._block = [['X'] * 4 for _ in range(4)]
        self._posx = -1
        self._posy = 15
        self._curr = []
        self.cords = []
        self._coori = []
        self._coorf = []

    def getblockshape(self):
        """Here we are getting protected variables block"""
        return self._block

    def getcoori(self, coord):
        """Here we are getting protected variables coori"""
        return self._coori[coord]

    def getcoorf(self, coord):
        """Here we are getting protected variables coorf"""
        return self._coorf[coord]

    def getcurr(self):
        """Here we are getting protected variables curr"""
        return self._curr

    def resetcurr(self):
        """Here we are resetting protected variables curr"""
        self._curr = []

    def appendtocurr(self, coords):
        """Here we are appending to protected variables curr"""
        self._curr.append(coords)

    def setpos(self, xin, yin):
        """set protected variables posx and posy"""
        self._posx = xin
        self._posy = yin

    def getpos(self):
        """return's protected variables"""
        return (self._posx, self._posy)

    def getblock(self, xcoord, ycoord):
        """return's protected variables block"""
        return self._block[xcoord][ycoord]

    def rotate(self, game):
        """for rotating the block"""
        preblock = self._block
        self._block = list(zip(*self._block[::-1]))
        self.cords = self._getcoords()
        self._coori = self.cords[0]
        self._coorf = self.cords[1]
        try:
            if game.checkpiecepos(self._posx, self._posy, self):
                game.fillpiecepos(self._posx, self._posy, self)
                return 1
            else:
                self._block = preblock
                self.cords = self._getcoords()
                self._coori = self.cords[0]
                self._coorf = self.cords[1]
                game.fillpiecepos(self._posx, self._posy, self)
                return 0
        except IndexError:
            self._block = preblock
            self.cords = self._getcoords()
            self._coori = self.cords[0]
            self._coorf = self.cords[1]
            game.fillpiecepos(self._posx, self._posy, self)
            return 0

    def fill(self, game):
        """for filling block at a position in board"""
        game.fillpiecepos(self._posx, self._posy, self)

    def moveleft(self, game):
        """move block left by one unit"""
        try:
            if game.checkpiecepos(self._posx, self._posy - 1, self) \
                    and self._posy > 0:
                game.fillpiecepos(self._posx, self._posy - 1, self)
                self._posy -= 1
            else:
                game.fillpiecepos(self._posx, self._posy, self)
        except IndexError:
            game.fillpiecepos(self._posx, self._posy, self)

    def moveright(self, game):
        """move block right by one unit"""
        try:
            if game.checkpiecepos(self._posx, self._posy + 1, self) \
                    and self._posy < 29:
                game.fillpiecepos(self._posx, self._posy + 1, self)
                self._posy += 1
        except IndexError:
            game.fillpiecepos(self._posx, self._posy, self)

    def draw(self, game):
        """move block down by one unit"""
        try:
            if game.checkpiecepos(self._posx + 1, self._posy, self):

                # print("Yes")

                game.fillpiecepos(self._posx + 1, self._posy, self)
                self._posx += 1
                return 1
            else:
                game.fillpiecepos(self._posx, self._posy, self)
                return 0
        except IndexError:
            game.fillpiecepos(self._posx, self._posy, self)
            return 0

    def goend(self, game):
        """go to the end of board for drop"""
        try:
            while self.draw(game):
                pass
        except IndexError:
            pass

    def newblock(self, num):
        """to select a random block"""

        # randnum = random.randrange(1,8)

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

        # return blocks[randnum]()

        selectedblock = blocks[num]()
        selectedblock.defineblock()
        return selectedblock

    def _getcoords(self):
        """protected functions which gets self._cords"""
        coor1 = [5, 5]
        coor2 = [-1, -1]
        for i in range(4):
            for j in range(4):
                if self._block[i][j] != ' ':
                    if coor1[0] > i:
                        coor1[0] = i
                    if coor1[1] > j:
                        coor1[1] = j
                    if coor2[0] < i:
                        coor2[0] = i
                    if coor2[1] < j:
                        coor2[1] = j
        return [coor1, coor2]

    def getcoords(self):
        """overloaded method which sends coordinates which are protected"""
        return [self._coori, self._coorf]

    def defineblock(self):
        """define block here , for polymorphism"""
        pass


class BlockLine(Block):
    """class for a particular Block"""
    def __init__(self):
        """Here we are defining instance variables"""
        Block.__init__(self)

    def defineblock(self):  # polymorphic method fo redefining block
        self._block = [[' ', ' ', ' ', ' '], ['X', 'X', 'X', 'X'], [' ', ' ', \
                       ' ', ' '], [' ', ' ', ' ', ' ']]
        self.cords = self._getcoords()
        self._coori = self.cords[0]
        self._coorf = self.cords[1]


class BlockBlock(Block):
    """class for a particular Block"""
    def __init__(self):
        """Here we are defining instance variables"""
        Block.__init__(self)

    def defineblock(self):
        """polymorphic method fo redefining block"""
        self._block = [[' ', ' ', ' ', ' '], [' ', 'X', 'X', ' '], [' ', 'X', \
                       'X', ' '], [' ', ' ', ' ', ' ']]
        self.cords = self._getcoords()
        self._coori = self.cords[0]
        self._coorf = self.cords[1]


class BlockZ(Block):
    """class for a particular Block"""
    def __init__(self):
        """Here we are defining instance variables"""
        Block.__init__(self)

    def defineblock(self):
        """polymorphic method fo redefining block"""
        self._block = [[' ', ' ', ' ', ' '], [' ', 'X', 'X', ' '], [' ', ' ', \
                       'X', 'X'], [' ', ' ', ' ', ' ']]
        self.cords = self._getcoords()
        self._coori = self.cords[0]
        self._coorf = self.cords[1]


class BlockS(Block):
    """class for a particular Block"""
    def __init__(self):
        """Here we are defining instance variables"""
        Block.__init__(self)

    def defineblock(self):
        """polymorphic method fo redefining block"""
        self._block = [[' ', ' ', ' ', ' '], [' ', ' ', 'X', 'X'], [' ', 'X', \
                       'X', ' '], [' ', ' ', ' ', ' ']]
        self.cords = self._getcoords()
        self._coori = self.cords[0]
        self._coorf = self.cords[1]


class BlockL(Block):
    """class for a particular Block"""
    def __init__(self):
        """Here we are defining instance variables"""
        Block.__init__(self)

    def defineblock(self):
        """polymorphic method fo redefining block"""
        self._block = [[' ', ' ', ' ', ' '], [' ', 'X', ' ', ' '], [' ', 'X', \
                       'X', 'X'], [' ', ' ', ' ', ' ']]
        self.cords = self._getcoords()
        self._coori = self.cords[0]
        self._coorf = self.cords[1]


class BlockJ(Block):
    """class for a particular Block"""
    def __init__(self):
        """Here we are defining instance variables"""
        Block.__init__(self)

    def defineblock(self):
        """polymorphic method fo redefining block"""
        self._block = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', 'X'], [' ', 'X', \
                       'X', 'X'], [' ', ' ', ' ', ' ']]
        self.cords = self._getcoords()
        self._coori = self.cords[0]
        self._coorf = self.cords[1]


class BlockT(Block):
    """class for a particular Block"""
    def __init__(self):
        """Here we are defining instance variables"""
        Block.__init__(self)

    def defineblock(self):
        """polymorphic method fo redefining block"""
        self._block = [[' ', ' ', ' ', ' '], [' ', 'X', 'X', 'X'], [' ', ' ', \
                       'X', ' '], [' ', ' ', ' ', ' ']]
        self.cords = self._getcoords()
        self._coori = self.cords[0]
        self._coorf = self.cords[1]


class BlockSpecial(Block):
    """class for a particular Block"""
    def __init__(self):
        """Here we are defining instance variables"""
        Block.__init__(self)

    def defineblock(self):
        """polymorphic method fo redefining block"""
        self._block = [[' ', ' ', ' ', ' '], [' ', '@', '@', ' '], [' ', '@', \
                       '@', ' '], [' ', ' ', ' ', ' ']]
        self.cords = self._getcoords()
        self._coori = self.cords[0]
        self._coorf = self.cords[1]
