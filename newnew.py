from support_functions import *
import pygame
import numpy as np
import random
import time

#rows, columns = 27, 19
ROWS = 27
COLUMNS = 19

# Define constants
PIXEL_WIDTH = 20
PIXEL_HEIGHT = 10
PIXEL_MARGIN = 2
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TRESHOLDDF = 100


TSP = TSPDecoder(rows=ROWS, columns=COLUMNS)

pygame.init()
WINDOW_SIZE = [
    COLUMNS*PIXEL_WIDTH+COLUMNS*PIXEL_MARGIN+2*PIXEL_MARGIN,
    ROWS*PIXEL_HEIGHT+ROWS*PIXEL_MARGIN+2*PIXEL_MARGIN
]

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Gamegame")

clock = pygame.time.Clock()
grid = np.zeros((TSP.rows, TSP.columns))



# wack-a-mole added stuff
# selected_row = -1
# selected_column = -1
# last_time = time.time()
# interval = 10


beats = []

def generateBeats():
    global beats
    beats.clear()

    is_long_b = random.choice([True, False])

    if is_long_b:
        row, column = random.randint(0, ROWS - 1), random.randint(0, COLUMNS - 1)
        direction = random.choice(['horizontal', 'vertical'])
        length = random.randint(3, 7)

        if direction == 'horizontal':
            for i in range(length):
                if column + i < COLUMNS:
                    beats.append((row, column + i))
        else:  # vertical
            for i in range(length):
                if row + i < ROWS:
                    beats.append((row + i, column))


    # Select a random cell and make it alive
    else:
        row, column = random.randint(0, ROWS-1), random.randint(0, COLUMNS-1)
        beats.append((row,column))


def match_position(pos):
    x, y = pos
    column = (x - PIXEL_MARGIN) // (PIXEL_WIDTH + PIXEL_MARGIN)
    row = (y - PIXEL_MARGIN) // (PIXEL_HEIGHT + PIXEL_MARGIN)

    if row < 0 or row >= ROWS or column < 0 or column >= COLUMNS:
        return None

    # Check if the clicked position has a '1'
    if (row, column) in beats:
        beats.remove((row, column))
        if not beats:
            generateBeats()

generateBeats() #first b shown



while True:
    # Check if the screen is closed and quit
    for event in pygame.event.get():
        if TSP.frame_available:
            grid = TSP.readFrame()

        if event.type == pygame.QUIT:
            pygame.quit()



    screen.fill(BLACK)

    # current_time = time.time()
    # if current_time - last_time > interval:
    #     selected_row = random.randint(0, rows - 1)
    #     selected_column = random.randint(0, columns - 1)
    #     last_time = current_time

    for row in range(ROWS):
        for column in range(COLUMNS):
             #pixel = grid[row][column]
             #color = BLACK
            for beat in beats:
                pixel = beats.index(row, column)    #ayuda

                if pixel > TRESHOLDDF:
                    match_position(pygame.mouse.get_pos())
                elif pixel > TRESHOLDDF:
                    match_position(pygame.mouse.get_pos())

                if (row, column) in beats:
                    color = WHITE
                else:
                    color = BLACK


            # if row == selected_row and column == selected_column:
            #     color = WHITE
            #
            # if pixel > TRESHOLDDF and row == selected_row and column == selected_column:
            #     color = BLACK
            # else:
            #     if row == selected_row and column == selected_column:
            #         color = WHITE
            #     else:
            #         color = BLACK

            # Draw the pixel on the screen
            pygame.draw.rect(
                screen,
                color,
                [
                    PIXEL_MARGIN + ((PIXEL_MARGIN + PIXEL_WIDTH) * column),
                    PIXEL_MARGIN + ((PIXEL_MARGIN + PIXEL_HEIGHT) * row),
                    PIXEL_WIDTH,
                    PIXEL_HEIGHT
                ]
            )

    # Limit the framerate to 60FPS
    clock.tick(60)

    # Draw to the display
    pygame.display.flip()