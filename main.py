import pygame
import random

# initialize pygame
pygame.init()

# RGB colors
BLACK = (0, 0, 0)

GREY = (128, 128, 128)

PURPLE = (128, 0, 128)

# Window dimensions
WIDTH, HEIGHT = 600, 600

# single cell size (20x20)
TILE_SIZE = 20

# Grid size
GRID_WIDTH = WIDTH // TILE_SIZE

GRID_HEIGHT = HEIGHT // TILE_SIZE

# Frames per second
FPS = 60

# set new game window object dimensions
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()


def gen(num):
    random.seed = num * random.randint(1 , 1000)
    return set(
        [
            (random.randrange(0, GRID_HEIGHT), random.randrange(0, GRID_WIDTH))
            for _ in range(num)
        ]
    )


def draw_cell(col, row):
    # determine top left pixel of a cell
    top_left = (col * TILE_SIZE, row * TILE_SIZE)
    # draw it
    # NOTE: rect object in pygame is (x , y , width , height)
    # NOTE: *top_left = top_left[0] , top_left[1] => Unpacking
    pygame.draw.rect(screen, PURPLE, (*top_left, TILE_SIZE, TILE_SIZE))


# A function to draw grid
def draw_grid(current_cells):

    # loop on current position cell
    # NOTE: positon = (col,row)
    for positon in current_cells:
        col, row = positon
        draw_cell(col, row)

    # draw grid horizontal lines
    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))

    # draw grid vertical lines
    for column in range(GRID_WIDTH):
        pygame.draw.line(
            screen, BLACK, (column * TILE_SIZE, 0), (column * TILE_SIZE, HEIGHT)
        )


## MAIN LOOP


def main():
    running = True
    playing = False

    # postions of alive cells
    current_cells = set()
    current_cells.add((10, 10))

    while running:
        # this loop will run a max of fps per seconnd
        clock.tick(FPS)

        for event in pygame.event.get():
            # check if event is quit
            if event.type == pygame.QUIT:
                running = False

            # check if any mouse button is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:

                x, y = pygame.mouse.get_pos()

                col = x // TILE_SIZE
                row = y // TILE_SIZE

                pos = (col, row)

                if pos in current_cells:
                    current_cells.remove(pos)
                else:
                    current_cells.add(pos)

            if event.type == pygame.KEYDOWN:

                # curr_pressed_key
                curr_key = event.key

                if curr_key == pygame.K_SPACE:
                    playing = not playing

                if curr_key == pygame.K_r:
                    current_cells = set()
                    playing = False

                if curr_key == pygame.K_c:
                    current_cells = gen(random.randrange(2, 10) * GRID_WIDTH)

        # set screen background to grey
        screen.fill(GREY)

        # draw the grid
        draw_grid(current_cells=current_cells)

        # update the display (necessary to each game)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
