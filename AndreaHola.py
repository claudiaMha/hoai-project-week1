from support_functions import *
import pygame

rows, columns = 27, 19
TSP = TSPDecoder(rows=rows, columns=columns)

# Define constants
PIXEL_WIDTH = 20
PIXEL_HEIGHT = 10
PIXEL_MARGIN = 2
BLACK = (0, 0, 0)
color= BLACK
TRESHOLDDF = 200

# Initialise the PyGame screen according to resolution
pygame.init()
WINDOW_SIZE = [
    columns * PIXEL_WIDTH + columns * PIXEL_MARGIN + 2 * PIXEL_MARGIN,
    rows * PIXEL_HEIGHT + rows * PIXEL_MARGIN + 2 * PIXEL_MARGIN
]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Haptic Skin visualiser")

# Initialise the PyGame Clock for timing
clock = pygame.time.Clock()
grid = np.zeros((TSP.rows, TSP.columns))
while True:
    # Check if the screen is closed and quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Get the frame
    if TSP.frame_available:
        grid = TSP.readFrame()

    # Clear the screen by blacking it out
    screen.fill(BLACK)

    # Loop through all pixels in the frame
    for row in range(rows):
        for column in range(columns):
            # Get the pixel value and set the gray value accordingly
            pixel = grid[row][column]
            if pixel > TRESHOLDDF:
                color = (pixel, pixel, pixel)


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
