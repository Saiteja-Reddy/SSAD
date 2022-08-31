#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Final Run Script for the game"""
import curses
import time
import random
import sys
from ..mypkg.gameplayclass import Gameplay

sys.stdout.write('\x1b[8;{rows};{cols}t'.format(rows=50, cols=60))
# resizing terminal for proper view

curses.initscr()  # create win
WIN = curses.newwin(38, 60, 1, 1)
WINS = WIN.subwin(36, 32, 1, 1)
WINS1 = WIN.subwin(34, 32, 3, 1)
WINS2 = WIN.subwin(34, 55, 3, 1)
WIN.keypad(1)
WIN.nodelay(1)
curses.noecho()
curses.curs_set(0)
# level = 1  # global variable for menu window
LEVELARRAY = {  # ranges of global variable level
    0: 1,
    1: 2,
    2: 3,
    3: 4,
    4: 5,
    5: 6,
    6: 7,
    7: 8,
    }


def game(input_level):  # main game window
    """Here we are defining main game window"""

    WIN.clear()
    WIN.nodelay(1)
    WIN.border(
        '|',
        ' ',
        ' ',
        ' ',
        ' ',
        ' ',
        ' ',
        ' ',
        )
    WINS.border('|', '|', ' ', '^')
    WINS1.border('|', '|', '_', '^')
    WIN.addstr(1, 9, 'TETRIS - By Teja', curses.A_BOLD)
    newgame = Gameplay()
    nextblock = random.randrange(1, 8)
    currblock = newgame.newblock(nextblock)
    speeds = {
        1: 500,
        2: 400,
        3: 300,
        4: 250,
        5: 200,
        6: 150,
        7: 100,
        8: 50,
        }
    level = input_level
    speed = speeds[level]
    gameover = False
    addedwall = False
    superblock = False
    start = time.time()
    while not gameover:  # main game loop

        speed = speeds[level]
        go_down = currblock.draw(newgame)

        # WIN.refresh()

        kcoord = 1
        lcoord = 1
        for i in newgame.getboard():
            kcoord += 1
            lcoord = 0
            for j in i:
                lcoord += 1
                if j == '@':
                    WIN.addstr(1 + kcoord, 1 + lcoord - 1, j, curses.A_BOLD)
                else:
                    WIN.addstr(1 + kcoord, 1 + lcoord - 1, j)

        if go_down == 0:
            if currblock.getpos()[0] == -1:
                gameover = True
                break

            # * Semi Filled Row
            # if newgame.getscore() % 100 is 0 and newgame.getscore()!= 0 :
            # ....newgame.addsemifilled()

            if superblock is True:
                newgame.clearcolumn(currblock.getpos())
                curses.flash()
            if superblock is False:
                currblock.fill(newgame)
            if superblock is True:
                superblock = False
            newgame.updatescore()

            if newgame.getscore() % 200 is 0 and newgame.getscore() \
                    != 0:
                if level is 7:
                    level = 8
                elif level is not 8:
                    level += 1
                if level in [6, 7, 8]:
                    if addedwall is False:
                        isadded = newgame.checkrowempty()  # add wall
                        if isadded:
                            addedwall = True
                            curses.flash()

            currblock = newgame.newblock(nextblock)
            if nextblock == 8:
                superblock = True
            nextblock = random.randrange(1, 8)

            #  * Special Block
            # if level in [6,7,'MAX'] and newgame.getscore() % 100 \
            #         is 0 and newgame.getscore()!= 0 :
            # ....nextblock = 8

            currblock.draw(newgame)

        # WIN.refresh()

        action = WIN.getch()
        if action == curses.KEY_UP or action == 115:
            currblock.rotate(newgame)
        elif action == curses.KEY_DOWN:
            pass
        elif action == curses.KEY_RIGHT or action == 100:
            currblock.moveright(newgame)
        elif action == curses.KEY_LEFT or action == 97:
            currblock.moveleft(newgame)
        elif action == 32:
            currblock.goend(newgame)
        elif action == 113:
            break

        WIN.addstr(36, 9, '  SCORE  : ' + str(newgame.getscore()),
                   curses.A_BOLD)
        mystyle = curses.A_BOLD | curses.A_UNDERLINE
        WIN.addstr(5, 39, 'Next Block', mystyle)
        kcoord = 4
        lcoord = 37
        nextup = newgame.newblock(nextblock)
        for i in nextup.getblockshape():
            kcoord += 1
            lcoord = 40
            for j in i:
                lcoord += 1
                WIN.addstr(1 + kcoord, 1 + lcoord - 1, j)
        del nextup
        end = time.time()
        (minutes, seconds) = divmod(end - start, 60)
        (hours, minutes) = divmod(minutes, 60)
        timeelapsed = '%d:%02d:%02d' % (hours, minutes, seconds)
        mymessage = 'Time Elapsed : ' + timeelapsed
        WIN.addstr(10, 34, mymessage, curses.A_BOLD)
        if level is not 8:
            WIN.addstr(12, 38, 'Level  : ' + str(level), curses.A_BOLD)
        else:
            WIN.addstr(12, 38, 'Level  : ' + str('MAX'), curses.A_BOLD)
        mystyle = curses.A_BOLD | curses.A_UNDERLINE
        WIN.addstr(15, 42, 'Controls', mystyle)
        WIN.addstr(17, 37, '    A/<- : Left ')
        WIN.addstr(18, 37, '    D/-> : Right ')
        WIN.addstr(19, 37, '    S/Up : Rotate ')
        WIN.addstr(20, 37, '    Down : Speed Up ')
        WIN.addstr(21, 37, '   Space : Drop ')
        WIN.addstr(22, 37, '     Q   : Quit ')
        WIN.refresh()  # to see value

        # WIN.getch()#get command from keyboard

        WIN.timeout(speed)

    WIN.clear()
    WINS2.border('|')
    WIN.nodelay(0)

    # defining game over screen

    message1 = 'Game Over!'
    message2 = 'Your Score was ' + str(newgame.getscore())
    message3 = 'Press Space to play again!'
    message4 = 'Press Enter to quit!'
    message5 = 'Press M for Main Menu'
    WIN.addstr(10, 18, message1, curses.A_STANDOUT)
    WIN.addstr(12, 16, message2, curses.A_BOLD | curses.A_UNDERLINE)
    WIN.addstr(14, 13, message3)
    WIN.addstr(16, 14, message5)
    WIN.addstr(18, 14, message4)

    counter = 0
    while counter not in [32, 10, 109]:
        counter = WIN.getch()
    if counter == 32:
        WIN.clear()
        level = 1
        game(level)
    if counter == 109:
        menu()


def menu():
    """Here we are defining the home menu screen"""
    WIN.nodelay(0)
    WIN.clear()
    WINS.border()
    selection = -1
    option = 0
    levoption = 0

    while selection < 0:
        graphics = [0] * 4
        graphics[option] = curses.A_REVERSE
        WIN.addstr(6, 13, 'XXX', curses.A_BOLD)
        WIN.addstr(7, 13, 'X', curses.A_BOLD)
        WIN.addstr(10, 12, 'Tetris', curses.A_BOLD | curses.A_UNDERLINE)
        WIN.addstr(14, 13, 'Play', graphics[0])
        WIN.addstr(15, 9, 'Instructions', graphics[1])
        if levoption != 7:
            WIN.addstr(16, 8, '  Level : ' + str(levoption + 1) + '  ',
                       graphics[2])
        else:
            WIN.addstr(16, 8, '  Level : MAX', graphics[2])
        WIN.addstr(17, 13, 'Exit', graphics[3])
        WIN.addstr(34, 20, '--By Teja')
        WIN.refresh()

        action = WIN.getch()
        if action == curses.KEY_UP:
            option = (option - 1) % 4
        elif action == curses.KEY_DOWN:
            option = (option + 1) % 4
        elif action == ord('\n'):
            selection = option
        elif graphics[2] == curses.A_REVERSE:
            if action == curses.KEY_RIGHT:
                levoption = (levoption + 1) % 8
            elif action == curses.KEY_LEFT:
                levoption = (levoption - 1) % 8

    if selection == 3:
        curses.endwin()
    elif selection == 1:
        instructions()
    elif selection == 0 or 2:
        WIN.clear()
        game(LEVELARRAY[levoption])


def instructions():
    """Here we are defining the instructions menu"""
    WIN.nodelay(0)
    WIN.clear()
    WINS.border()
    mystyle = curses.A_BOLD | curses.A_UNDERLINE
    WIN.addstr(9, 10, 'Instructions', mystyle)
    WIN.addstr(11, 6, 'Use the following keys')
    WIN.addstr(13, 6, '    A/<- : Left ')
    WIN.addstr(14, 6, '    D/-> : Right ')
    WIN.addstr(15, 6, '    S/Up : Rotate ')
    WIN.addstr(16, 6, '    Down : Speed Up ')
    WIN.addstr(17, 6, '   Space : Drop ')
    WIN.addstr(18, 6, '     Q   : Quit ')
    WIN.addstr(20, 4, 'Press any key to continue', curses.A_BOLD)
    inchar = WIN.getch()
    if inchar:
        menu()


menu()  # calling menu window

curses.endwin()  # close window

sys.stdout.write('\x1b[8;{rows};{cols}t'.format(rows=30, cols=100))
# resizing terminal to default size
