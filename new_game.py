import pygame
import numpy as np
import random

from support_functions import TSPDecoder

# Define constants
ROWS = 2
COLUMNS = 2
THRESHOLD = 75
PIXEL_WIDTH = 10
PIXEL_HEIGHT = 10
PIXEL_MARGIN = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
Counter = 0


pygame.init()
WINDOW_SIZE = [
    COLUMNS*PIXEL_WIDTH+COLUMNS*PIXEL_MARGIN+2*PIXEL_MARGIN,
    ROWS*PIXEL_HEIGHT+ROWS*PIXEL_MARGIN+2*PIXEL_MARGIN
]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("A")

# Initialise the PyGame Clock for timing
clock = pygame.time.Clock()

# Initialise the Haptic Skin
TSP = TSPDecoder(rows=ROWS, columns=COLUMNS)

# Create the game grid and fill it randomly at the start
grid = np.zeros((ROWS, COLUMNS, 3), dtype=int)
grid2 = np.zeros((ROWS, COLUMNS, 3), dtype=int)


