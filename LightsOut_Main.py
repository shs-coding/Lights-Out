''' This is a project I have worked on for about two weeks.
    It is not perfect, but I'm happy with it. If you have
    suggestions or input, email me at shs.python@gmail.com.
    Thanks for playing! '''

import getpass
import pygame
import random
import sys
import time
from copy import deepcopy

pygame.init()

pygame.time.wait(5)

red = (255, 0, 0)
white = (255, 255, 255)
blue = (66, 134, 244)

clicks = 0

# GETS THE USER’S PROFILE NAME TO ACCESS THE SOUND FILES NEEDED #

username = (getpass.getuser())


# SETS DELAY FOR EXIT FUNCTION #


def delay():
    time.sleep(0.5)


# EXITS CHALLENGE AFTER PLAYER WINS #


def exit_challenge():
    global clicks
    if not pygame.mixer.music.get_busy():
        sys.exit("Congrats -- you won in " + str(clicks) + " moves! "
                                                           "\nSound icons created by Bhima from The Noun Project.")
    else:
        delay()
        exit_challenge()


# INITIALLY, NO ONE NEEDS HELP SOLVING #

request_solve = False

# ---------- INTRO ---------- #

print()
print("Welcome to Lights Out.")
print()
mode = input("Which gamemode would you like to play -- Sandbox or Challenge?"
             " Type \'s\' for Sandbox or \'c\' for Challenge. ")

# SIZE OF GRID - ZERO INDEXED #

if mode == "s":
    size = 4
elif mode == "c":
    size = 5

grid = []
for x in range(size + 1):
    column = []
    for y in range(size + 1):
        column.append(white)
    grid.append(column)


# ---------- LOADS IMAGES FOR SOUND ---------- #


sound_on_img = pygame.image.load("C:/Users/" + username + "/Downloads/LightsOut/SoundOn.png")
sound_off_img = pygame.image.load("C:/Users/" + username + "/Downloads/LightsOut/SoundOff.png")
sound_reset_img = pygame.image.load("C:/Users/" + username + "/Downloads/LightsOut/SoundReset.png")

sound_on_img = pygame.transform.scale(sound_on_img, (80, 80))
sound_off_img = pygame.transform.scale(sound_off_img, (80, 80))
sound_reset_img = pygame.transform.scale(sound_reset_img, (80, 80))

sound_on = True


# ---------- DRAWING FUNCTION ---------- #


def draw():
    global size
    global mode
    global clicks
    global sound_on
    global request_solve

    pygame.mixer.pre_init(frequency=64000, size=-16, channels=2)
    pygame.mixer.init()

    drawing = True

    while drawing:

        # MAKES THE GRID #

        if mode == "s":
            pygame.draw.rect(w, (0, 0, 0), (500, 0, 100, 500), 5)
        elif mode == "c":
            pygame.draw.rect(w, (0, 0, 0), (600, 0, 100, 700), 5)

        for a in range(size + 1):
            for b in range(size + 1):
                r = pygame.Rect(a * 100, b * 100, 100, 100)
                border = 0
                if grid[a][b] == (0, 0, 0):
                    border = 5
                pygame.draw.rect(w, grid[a][b], r, border)

        for grid_x in range(size + 1):
            for grid_y in range(size + 1):
                rect = pygame.Rect(grid_x * 100, grid_y * 100, 100, 100)
                pygame.draw.rect(w, (0, 0, 0), rect, 5)

                # ---------- REPLACES SOUND ON IMAGE WITH SOUND OFF IMAGE ---------- #

                if sound_on:
                    w.blit(sound_on_img, ((size + 1) * 100 + 10, 10))
                elif not sound_on:
                    w.blit(sound_off_img, ((size + 1) * 100 + 10, 10))

                # ---------- SOLVES PUZZLE USING "CHASE-THE-LIGHTS" METHOD ---------- #

                if request_solve:

                    press_0_0 = False
                    press_0_1 = False
                    press_0_2 = False
                    press_0_3 = False
                    press_0_4 = False
                    press_0_5 = False
                    press_1_0 = False
                    press_1_1 = False
                    press_1_2 = False
                    press_1_3 = False
                    press_1_4 = False
                    press_1_5 = False
                    press_2_0 = False
                    press_2_1 = False
                    press_2_2 = False
                    press_2_3 = False
                    press_2_4 = False
                    press_2_5 = False
                    press_3_0 = False
                    press_3_1 = False
                    press_3_2 = False
                    press_3_3 = False
                    press_3_4 = False
                    press_3_5 = False
                    press_4_0 = False
                    press_4_1 = False
                    press_4_2 = False
                    press_4_3 = False
                    press_4_4 = False
                    press_4_5 = False
                    press_5_0 = False
                    press_5_1 = False
                    press_5_2 = False
                    press_5_3 = False
                    press_5_4 = False
                    press_5_5 = False

                    solve_grid = deepcopy(grid)

                    # ---------- INITIAL CHASE THE LIGHTS RUN ---------- #

                    if solve_grid[0][0] == red:
                        invert(solve_grid, (0, 1))
                        press_0_1 = not press_0_1

                    if solve_grid[1][0] == red:
                        invert(solve_grid, (1, 1))
                        press_1_1 = not press_1_1

                    if solve_grid[2][0] == red:
                        invert(solve_grid, (2, 1))
                        press_2_1 = not press_2_1

                    if solve_grid[3][0] == red:
                        invert(solve_grid, (3, 1))
                        press_3_1 = not press_3_1

                    if solve_grid[4][0] == red:
                        invert(solve_grid, (4, 1))
                        press_4_1 = not press_4_1

                    if solve_grid[5][0] == red:
                        invert(solve_grid, (5, 1))
                        press_5_1 = not press_5_1

                    ##########

                    if solve_grid[0][1] == red:
                        invert(solve_grid, (0, 2))
                        press_0_2 = not press_0_2

                    if solve_grid[1][1] == red:
                        invert(solve_grid, (1, 2))
                        press_1_2 = not press_1_2

                    if solve_grid[2][1] == red:
                        invert(solve_grid, (2, 2))
                        press_2_2 = not press_2_2

                    if solve_grid[3][1] == red:
                        invert(solve_grid, (3, 2))
                        press_3_2 = not press_3_2

                    if solve_grid[4][1] == red:
                        invert(solve_grid, (4, 2))
                        press_4_2 = not press_4_2

                    if solve_grid[5][1] == red:
                        invert(solve_grid, (5, 2))
                        press_5_2 = not press_5_2

                    ##########

                    if solve_grid[0][2] == red:
                        invert(solve_grid, (0, 3))
                        press_0_3 = not press_0_3

                    if solve_grid[1][2] == red:
                        invert(solve_grid, (1, 3))
                        press_1_3 = not press_1_3

                    if solve_grid[2][2] == red:
                        invert(solve_grid, (2, 3))
                        press_2_3 = not press_2_3

                    if solve_grid[3][2] == red:
                        invert(solve_grid, (3, 3))
                        press_3_3 = not press_3_3

                    if solve_grid[4][2] == red:
                        invert(solve_grid, (4, 3))
                        press_4_3 = not press_4_3

                    if solve_grid[5][2] == red:
                        invert(solve_grid, (5, 3))
                        press_5_3 = not press_5_3

                    ##########

                    if solve_grid[0][3] == red:
                        invert(solve_grid, (0, 4))
                        press_0_4 = not press_0_4

                    if solve_grid[1][3] == red:
                        invert(solve_grid, (1, 4))
                        press_1_4 = not press_1_4

                    if solve_grid[2][3] == red:
                        invert(solve_grid, (2, 4))
                        press_2_4 = not press_2_4

                    if solve_grid[3][3] == red:
                        invert(solve_grid, (3, 4))
                        press_3_4 = not press_3_4

                    if solve_grid[4][3] == red:
                        invert(solve_grid, (4, 4))
                        press_4_4 = not press_4_4

                    if solve_grid[5][3] == red:
                        invert(solve_grid, (5, 4))
                        press_5_4 = not press_5_4

                    ##########

                    if solve_grid[0][4] == red:
                        invert(solve_grid, (0, 5))
                        press_0_5 = not press_0_5

                    if solve_grid[1][4] == red:
                        invert(solve_grid, (1, 5))
                        press_1_5 = not press_1_5

                    if solve_grid[2][4] == red:
                        invert(solve_grid, (2, 5))
                        press_2_5 = not press_2_5

                    if solve_grid[3][4] == red:
                        invert(solve_grid, (3, 5))
                        press_3_5 = not press_3_5

                    if solve_grid[4][4] == red:
                        invert(solve_grid, (4, 5))
                        press_4_5 = not press_4_5

                    if solve_grid[5][4] == red:
                        invert(solve_grid, (5, 5))
                        press_5_5 = not press_5_5

                    # ---------- APPLIES RULES ---------- #

                    if solve_grid[0][5] == red:
                        invert(solve_grid, (0, 0))
                        press_0_0 = not press_0_0
                        invert(solve_grid, (2, 0))
                        press_2_0 = not press_2_0

                    if solve_grid[1][5] == red:
                        invert(solve_grid, (3, 0))
                        press_3_0 = not press_3_0

                    if solve_grid[2][5] == red:
                        invert(solve_grid, (0, 0))
                        press_0_0 = not press_0_0
                        invert(solve_grid, (4, 0))
                        press_4_0 = not press_4_0

                    if solve_grid[3][5] == red:
                        invert(solve_grid, (1, 0))
                        press_1_0 = not press_1_0
                        invert(solve_grid, (5, 0))
                        press_5_0 = not press_5_0

                    if solve_grid[4][5] == red:
                        invert(solve_grid, (2, 0))
                        press_2_0 = not press_2_0

                    if solve_grid[5][5] == red:
                        invert(solve_grid, (3, 0))
                        press_3_0 = not press_3_0
                        invert(solve_grid, (5, 0))
                        press_5_0 = not press_5_0

                    # SECOND RUN #

                    if solve_grid[0][0] == red:
                        invert(solve_grid, (0, 1))
                        press_0_1 = not press_0_1

                    if solve_grid[1][0] == red:
                        invert(solve_grid, (1, 1))
                        press_1_1 = not press_1_1

                    if solve_grid[2][0] == red:
                        invert(solve_grid, (2, 1))
                        press_2_1 = not press_2_1

                    if solve_grid[3][0] == red:
                        invert(solve_grid, (3, 1))
                        press_3_1 = not press_3_1

                    if solve_grid[4][0] == red:
                        invert(solve_grid, (4, 1))
                        press_4_1 = not press_4_1

                    if solve_grid[5][0] == red:
                        invert(solve_grid, (5, 1))
                        press_5_1 = not press_5_1

                    ##########

                    if solve_grid[0][1] == red:
                        invert(solve_grid, (0, 2))
                        press_0_2 = not press_0_2

                    if solve_grid[1][1] == red:
                        invert(solve_grid, (1, 2))
                        press_1_2 = not press_1_2

                    if solve_grid[2][1] == red:
                        invert(solve_grid, (2, 2))
                        press_2_2 = not press_2_2

                    if solve_grid[3][1] == red:
                        invert(solve_grid, (3, 2))
                        press_3_2 = not press_3_2

                    if solve_grid[4][1] == red:
                        invert(solve_grid, (4, 2))
                        press_4_2 = not press_4_2

                    if solve_grid[5][1] == red:
                        invert(solve_grid, (5, 2))
                        press_5_2 = not press_5_2

                    ##########

                    if solve_grid[0][2] == red:
                        invert(solve_grid, (0, 3))
                        press_0_3 = not press_0_3

                    if solve_grid[1][2] == red:
                        invert(solve_grid, (1, 3))
                        press_1_3 = not press_1_3

                    if solve_grid[2][2] == red:
                        invert(solve_grid, (2, 3))
                        press_2_3 = not press_2_3

                    if solve_grid[3][2] == red:
                        invert(solve_grid, (3, 3))
                        press_3_3 = not press_3_3

                    if solve_grid[4][2] == red:
                        invert(solve_grid, (4, 3))
                        press_4_3 = not press_4_3

                    if solve_grid[5][2] == red:
                        invert(solve_grid, (5, 3))
                        press_5_3 = not press_5_3

                    ##########

                    if solve_grid[0][3] == red:
                        invert(solve_grid, (0, 4))
                        press_0_4 = not press_0_4

                    if solve_grid[1][3] == red:
                        invert(solve_grid, (1, 4))
                        press_1_4 = not press_1_4

                    if solve_grid[2][3] == red:
                        invert(solve_grid, (2, 4))
                        press_2_4 = not press_2_4

                    if solve_grid[3][3] == red:
                        invert(solve_grid, (3, 4))
                        press_3_4 = not press_3_4

                    if solve_grid[4][3] == red:
                        invert(solve_grid, (4, 4))
                        press_4_4 = not press_4_4

                    if solve_grid[5][3] == red:
                        invert(solve_grid, (5, 4))
                        press_5_4 = not press_5_4

                    ##########

                    if solve_grid[0][4] == red:
                        invert(solve_grid, (0, 5))
                        press_0_5 = not press_0_5

                    if solve_grid[1][4] == red:
                        invert(solve_grid, (1, 5))
                        press_1_5 = not press_1_5

                    if solve_grid[2][4] == red:
                        invert(solve_grid, (2, 5))
                        press_2_5 = not press_2_5

                    if solve_grid[3][4] == red:
                        invert(solve_grid, (3, 5))
                        press_3_5 = not press_3_5

                    if solve_grid[4][4] == red:
                        invert(solve_grid, (4, 5))
                        press_4_5 = not press_4_5

                    if solve_grid[5][4] == red:
                        invert(solve_grid, (5, 5))
                        press_5_5 = not press_5_5

                    # SHOWS WHERE TO CLICK #

                    if press_0_0:
                        pygame.draw.circle(w, blue, (50, 50), 35)
                    if press_0_1:
                        pygame.draw.circle(w, blue, (50, 150), 35)
                    if press_0_2:
                        pygame.draw.circle(w, blue, (50, 250), 35)
                    if press_0_3:
                        pygame.draw.circle(w, blue, (50, 350), 35)
                    if press_0_4:
                        pygame.draw.circle(w, blue, (50, 450), 35)
                    if press_0_5:
                        pygame.draw.circle(w, blue, (50, 550), 35)
                    if press_1_0:
                        pygame.draw.circle(w, blue, (150, 50), 35)
                    if press_1_1:
                        pygame.draw.circle(w, blue, (150, 150), 35)
                    if press_1_2:
                        pygame.draw.circle(w, blue, (150, 250), 35)
                    if press_1_3:
                        pygame.draw.circle(w, blue, (150, 350), 35)
                    if press_1_4:
                        pygame.draw.circle(w, blue, (150, 450), 35)
                    if press_1_5:
                        pygame.draw.circle(w, blue, (150, 550), 35)
                    if press_2_0:
                        pygame.draw.circle(w, blue, (250, 50), 35)
                    if press_2_1:
                        pygame.draw.circle(w, blue, (250, 150), 35)
                    if press_2_2:
                        pygame.draw.circle(w, blue, (250, 250), 35)
                    if press_2_3:
                        pygame.draw.circle(w, blue, (250, 350), 35)
                    if press_2_4:
                        pygame.draw.circle(w, blue, (250, 450), 35)
                    if press_2_5:
                        pygame.draw.circle(w, blue, (250, 550), 35)
                    if press_3_0:
                        pygame.draw.circle(w, blue, (350, 50), 35)
                    if press_3_1:
                        pygame.draw.circle(w, blue, (350, 150), 35)
                    if press_3_2:
                        pygame.draw.circle(w, blue, (350, 250), 35)
                    if press_3_3:
                        pygame.draw.circle(w, blue, (350, 350), 35)
                    if press_3_4:
                        pygame.draw.circle(w, blue, (350, 450), 35)
                    if press_3_5:
                        pygame.draw.circle(w, blue, (350, 550), 35)
                    if press_4_0:
                        pygame.draw.circle(w, blue, (450, 50), 35)
                    if press_4_1:
                        pygame.draw.circle(w, blue, (450, 150), 35)
                    if press_4_2:
                        pygame.draw.circle(w, blue, (450, 250), 35)
                    if press_4_3:
                        pygame.draw.circle(w, blue, (450, 350), 35)
                    if press_4_4:
                        pygame.draw.circle(w, blue, (450, 450), 35)
                    if press_4_5:
                        pygame.draw.circle(w, blue, (450, 550), 35)
                    if press_5_0:
                        pygame.draw.circle(w, blue, (550, 50), 35)
                    if press_5_1:
                        pygame.draw.circle(w, blue, (550, 150), 35)
                    if press_5_2:
                        pygame.draw.circle(w, blue, (550, 250), 35)
                    if press_5_3:
                        pygame.draw.circle(w, blue, (550, 350), 35)
                    if press_5_4:
                        pygame.draw.circle(w, blue, (550, 450), 35)
                    if press_5_5:
                        pygame.draw.circle(w, blue, (550, 550), 35)

        # MANAGES EVENTS #

        for event in pygame.event.get():

            # CHECKS IF PLAYER HAS EXITED #

            if event.type == pygame.QUIT:
                sys.exit("Thanks for playing! \nSound icons created by Bhima from The Noun Project.")

            if event.type == pygame.MOUSEBUTTONDOWN:

                # PLAYS CLICK SOUND #

                pygame.mixer.music.stop()
                if sound_on:
                    pygame.mixer.music.load('C:/Users/' + username + '/Downloads/LightsOut/Switch.wav')
                    pygame.mixer.music.play(1)

                # INVERTS BOXES #

                (x_pos, y_pos) = pygame.mouse.get_pos()

                if x_pos < 500 and mode == "s":
                    grid_x = int(x_pos / 100)
                    grid_y = int(y_pos / 100)
                    invert(grid, (grid_x, grid_y))

                elif x_pos < 600 and y_pos < 600 and mode == "c":
                    grid_x = int(x_pos / 100)
                    grid_y = int(y_pos / 100)
                    invert(grid, (grid_x, grid_y))

                elif x_pos > 500 and mode == "s":
                    sound_on = not sound_on
                    w.blit(sound_reset_img, (510, 10))

                elif x_pos > 600 and mode == "c":
                    sound_on = not sound_on
                    w.blit(sound_reset_img, (610, 10))

                # CHECKS IF PLAYER HAS CLICKED "SOLVE" #

                elif y_pos >= 600:
                    request_solve = not request_solve

                # CHECKS IF PLAYER HAS WON CHALLENGE MODE #

                if mode == "c":
                    clicks += 1
                    if grid[0][0] == white and grid[0][1] == white and grid[0][2] == white and grid[0][3] == white and \
                                    grid[0][4] == white and grid[0][5] == white \
                            and grid[1][0] == white and grid[1][1] == white and grid[1][2] == white and grid[1][
                        3] == white and grid[1][4] == white and grid[1][5] == white \
                            and grid[2][0] == white and grid[2][1] == white and grid[2][2] == white and grid[2][
                        3] == white and grid[2][4] == white and grid[2][5] == white \
                            and grid[2][0] == white and grid[3][1] == white and grid[3][2] == white and grid[3][
                        3] == white and grid[3][4] == white and grid[3][5] == white \
                            and grid[4][0] == white and grid[4][1] == white and grid[4][2] == white and grid[4][
                        3] == white and grid[4][4] == white and grid[4][5] == white \
                            and grid[5][0] == white and grid[5][1] == white and grid[5][2] == white and grid[5][
                        3] == white and grid[5][4] == white and grid[5][5] == white:
                        if sound_on:
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('C:/Users/' + username + '/Downloads/LightsOut/Cheering.wav')
                            pygame.mixer.music.play(1)
                        exit_challenge()

            pygame.display.flip()


# ---------- INVERT FUNCTION ---------- #


def invert(grid, grid_position):
    global size

    (x, y) = grid_position

    # TOP LEFT SQUARE #

    if x == y == 0:
        if grid[x][y] == red:
            grid[x][y] = white
        elif grid[x][y] == white:
            grid[x][y] = red

        if grid[x + 1][y] == red:
            grid[x + 1][y] = white
        elif grid[x + 1][y] == white:
            grid[x + 1][y] = red
        if grid[x][y + 1] == red:
            grid[x][y + 1] = white

        elif grid[x][y + 1] == white:
            grid[x][y + 1] = red

    # BOTTOM LEFT SQUARE #

    elif x == 0 and y == size:
        if grid[x][y] == red:
            grid[x][y] = white
        elif grid[x][y] == white:
            grid[x][y] = red

        if grid[x + 1][y] == red:
            grid[x + 1][y] = white
        elif grid[x + 1][y] == white:
            grid[x + 1][y] = red

        if grid[x][y - 1] == red:
            grid[x][y - 1] = white
        elif grid[x][y - 1] == white:
            grid[x][y - 1] = red

    # TOP RIGHT SQUARE #

    elif x == size and y == 0:
        if grid[x][y] == red:
            grid[x][y] = white
        elif grid[x][y] == white:
            grid[x][y] = red

        if grid[x - 1][y] == red:
            grid[x - 1][y] = white
        elif grid[x - 1][y] == white:
            grid[x - 1][y] = red

        if grid[x][y + 1] == red:
            grid[x][y + 1] = white
        elif grid[x][y + 1] == white:
            grid[x][y + 1] = red

    # BOTTOM RIGHT SQUARE #

    elif x == y == size:
        if grid[x][y] == red:
            grid[x][y] = white
        elif grid[x][y] == white:
            grid[x][y] = red

        if grid[x - 1][y] == red:
            grid[x - 1][y] = white
        elif grid[x - 1][y] == white:
            grid[x - 1][y] = red

        if grid[x][y - 1] == red:
            grid[x][y - 1] = white
        elif grid[x][y - 1] == white:
            grid[x][y - 1] = red

    # LEFTMOST COLUMN #

    elif x == 0 and 1 <= y <= (size - 1):
        if grid[x][y] == red:
            grid[x][y] = white
        elif grid[x][y] == white:
            grid[x][y] = red

        if grid[x + 1][y] == red:
            grid[x + 1][y] = white
        elif grid[x + 1][y] == white:
            grid[x + 1][y] = red

        if grid[x][y - 1] == red:
            grid[x][y - 1] = white
        elif grid[x][y - 1] == white:
            grid[x][y - 1] = red

        if grid[x][y + 1] == red:
            grid[x][y + 1] = white
        elif grid[x][y + 1] == white:
            grid[x][y + 1] = red

    # RIGHTMOST COLUMN #

    elif x == size and 1 <= y <= (size - 1):
        if grid[x][y] == red:
            grid[x][y] = white
        elif grid[x][y] == white:
            grid[x][y] = red

        if grid[x - 1][y] == red:
            grid[x - 1][y] = white
        elif grid[x - 1][y] == white:
            grid[x - 1][y] = red

        if grid[x][y - 1] == red:
            grid[x][y - 1] = white
        elif grid[x][y - 1] == white:
            grid[x][y - 1] = red

        if grid[x][y + 1] == red:
            grid[x][y + 1] = white
        elif grid[x][y + 1] == white:
            grid[x][y + 1] = red

    # TOP ROW #

    elif y == 0 and 1 <= x <= (size - 1):
        if grid[x][y] == red:
            grid[x][y] = white
        elif grid[x][y] == white:
            grid[x][y] = red

        if grid[x - 1][y] == red:
            grid[x - 1][y] = white
        elif grid[x - 1][y] == white:
            grid[x - 1][y] = red

        if grid[x + 1][y] == red:
            grid[x + 1][y] = white
        elif grid[x + 1][y] == white:
            grid[x + 1][y] = red

        if grid[x][y + 1] == red:
            grid[x][y + 1] = white
        elif grid[x][y + 1] == white:
            grid[x][y + 1] = red

    # BOTTOM ROW #

    elif y == size and 1 <= x <= (size - 1):
        if grid[x][y] == red:
            grid[x][y] = white
        elif grid[x][y] == white:
            grid[x][y] = red

        if grid[x - 1][y] == red:
            grid[x - 1][y] = white
        elif grid[x - 1][y] == white:
            grid[x - 1][y] = red

        if grid[x + 1][y] == red:
            grid[x + 1][y] = white
        elif grid[x + 1][y] == white:
            grid[x + 1][y] = red

        if grid[x][y - 1] == red:
            grid[x][y - 1] = white
        elif grid[x][y - 1] == white:
            grid[x][y - 1] = red

    # EVERYTHING ELSE #

    else:
        if grid[x][y] == red:
            grid[x][y] = white
        elif grid[x][y] == white:
            grid[x][y] = red

        if grid[x - 1][y] == red:
            grid[x - 1][y] = white
        elif grid[x - 1][y] == white:
            grid[x - 1][y] = red

        if grid[x + 1][y] == red:
            grid[x + 1][y] = white
        elif grid[x + 1][y] == white:
            grid[x + 1][y] = red

        if grid[x][y - 1] == red:
            grid[x][y - 1] = white
        elif grid[x][y - 1] == white:
            grid[x][y - 1] = red

        if grid[x][y + 1] == red:
            grid[x][y + 1] = white
        elif grid[x][y + 1] == white:
            grid[x][y + 1] = red

    return


# ---------- SANDBOX MODE ---------- #


if mode == "s":
    print()
    print("-")
    print()
    rules = input("Do you need an explanation of the rules? y/n: ")
    if rules == "y":
        print("In sandbox mode, you start off with a blank 5 by 5 grid.")
        print("You can do whatever you please. Have fun!")

    # CREATES SCREEN #

    w = pygame.display.set_mode([600, 500])
    caption = "Lights Out - Sandbox"
    pygame.display.set_caption(caption)
    w.fill(white)

    # PLAYS GAME #

    draw()


# ---------- CHALLENGE MODE ---------- #


elif mode == "c":
    print()
    print("-")
    print()

    rules = input("Do you need an explanation of the rules? y/n: ")
    if rules == "y":
        print()
        print("In challenge mode, you are given a randomly generated 6 by 6 board.")
        pygame.time.wait(1000)
        print()
        print("The object of this gamemode is to turn every square white.")
        pygame.time.wait(1000)
        print()
        print("All boards can be solved, but because of the random nature "
              "of the generation process some will be much harder than others.")
        pygame.time.wait(1000)
        print()
        print("If you are stuck on a puzzle, click \"Solve\", and the solution will be shown.")
        print()

        input("When you are done reading, press Enter.")

    # DOESN'T ACTUALLY DO ANYTHING, JUST ADDS TO AESTHETIC #

    print()
    print("Board created. Good luck!")

    # CREATES SCREEN #

    w = pygame.display.set_mode([700, 700])
    w.fill(white)
    caption = "Lights Out - Challenge"
    pygame.display.set_caption(caption)

    # CONTROLS SOUND OUTPUT #

    solve_font = pygame.font.SysFont("cambria", 48)
    solve_rect = pygame.draw.rect(w, (0, 0, 0), (0, 600, 602.5, 100), 0)
    solve_text = solve_font.render("SOLVE", True, (255, 255, 255))
    w.blit(solve_text, (240, 620))

    # GENERATES BOARD #

    num_1 = random.randint(1, 2)
    num_2 = random.randint(1, 2)
    num_3 = random.randint(1, 2)
    num_4 = random.randint(1, 2)
    num_5 = random.randint(1, 2)
    num_6 = random.randint(1, 2)
    num_7 = random.randint(1, 2)
    num_8 = random.randint(1, 2)
    num_9 = random.randint(1, 2)
    num_10 = random.randint(1, 2)
    num_11 = random.randint(1, 2)
    num_12 = random.randint(1, 2)
    num_13 = random.randint(1, 2)
    num_14 = random.randint(1, 2)
    num_15 = random.randint(1, 2)
    num_16 = random.randint(1, 2)
    num_17 = random.randint(1, 2)
    num_18 = random.randint(1, 2)
    num_19 = random.randint(1, 2)
    num_20 = random.randint(1, 2)
    num_21 = random.randint(1, 2)
    num_22 = random.randint(1, 2)
    num_23 = random.randint(1, 2)
    num_24 = random.randint(1, 2)
    num_25 = random.randint(1, 2)
    num_26 = random.randint(1, 2)
    num_27 = random.randint(1, 2)
    num_28 = random.randint(1, 2)
    num_29 = random.randint(1, 2)
    num_30 = random.randint(1, 2)
    num_31 = random.randint(1, 2)
    num_32 = random.randint(1, 2)
    num_33 = random.randint(1, 2)
    num_34 = random.randint(1, 2)
    num_35 = random.randint(1, 2)
    num_36 = random.randint(1, 2)
    if num_1 == 2:
        grid[0][0] = red
    if num_2 == 2:
        grid[0][1] = red
    if num_3 == 3:
        grid[0][2] = red
    if num_4 == 2:
        grid[0][3] = red
    if num_5 == 2:
        grid[0][4] = red
    if num_6 == 2:
        grid[0][5] = red
    if num_7 == 2:
        grid[1][0] = red
    if num_8 == 2:
        grid[1][1] = red
    if num_9 == 2:
        grid[1][2] = red
    if num_10 == 2:
        grid[1][3] = red
    if num_11 == 2:
        grid[1][4] = red
    if num_12 == 2:
        grid[1][5] = red
    if num_13 == 2:
        grid[2][0] = red
    if num_14 == 2:
        grid[2][1] = red
    if num_15 == 2:
        grid[2][2] = red
    if num_16 == 2:
        grid[2][3] = red
    if num_17 == 2:
        grid[2][4] = red
    if num_18 == 2:
        grid[2][5] = red
    if num_19 == 2:
        grid[3][0] = red
    if num_20 == 2:
        grid[3][1] = red
    if num_21 == 2:
        grid[3][2] = red
    if num_22 == 2:
        grid[3][3] = red
    if num_23 == 2:
        grid[3][4] = red
    if num_24 == 2:
        grid[3][5] = red
    if num_25 == 2:
        grid[4][0] = red
    if num_26 == 2:
        grid[4][1] = red
    if num_27 == 2:
        grid[4][2] = red
    if num_28 == 2:
        grid[4][3] = red
    if num_29 == 2:
        grid[4][4] = red
    if num_30 == 2:
        grid[4][5] = red
    if num_31 == 2:
        grid[5][0] = red
    if num_32 == 2:
        grid[5][1] = red
    if num_33 == 2:
        grid[5][2] = red
    if num_34 == 2:
        grid[5][3] = red
    if num_35 == 2:
        grid[5][4] = red
    if num_36 == 2:
        grid[5][5] = red

    # PLAYS GAME #

    draw()
