import pygame
import random

# initialize pygame
pygame.init()

# RGB colors
BLACK = (0, 0, 0)

GREY = (128, 128, 128)

PURPLE = (128, 0, 128)

# Window dimensions
WIDTH, HEIGHT = 800, 600

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


# generate random cells in the grid
def gen(num):

    # changing the seed each time for more variety of postions
    random.seed = num * random.randint(1, 1000)
    return set(
        [
            (random.randrange(0, GRID_WIDTH), random.randrange(0, GRID_HEIGHT))
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


def toggle_cell(col, row, current_cells):
    pos = (col, row)

    if pos in current_cells:
        current_cells.remove(pos)
    else:
        current_cells.add(pos)


# Update Grid
def update_grid(current_cells):
    all_neighbours = set()
    new_positions = set()

    for position in current_cells:

        neigbours = get_neigbours(pos=position)

        all_neighbours.update(neigbours)
        

        neigbours = list(filter(lambda x: x in current_cells, neigbours))


        if len(neigbours) in [2, 3]:
            new_positions.add(position)
    
    
    for position in all_neighbours:
        neigbours = get_neigbours(pos=position)
        neigbours = list(filter(lambda x: x in current_cells, neigbours))

        if len(neigbours) in [2, 3]:
            new_positions.add(position)
    return new_positions


# get state of neigbours
def get_neigbours(pos):
    x, y = pos

    neigbours = list()
    for dx in [-1, 0, 1]:
        if (x + dx) in [-1, GRID_WIDTH + 1]:
            continue
        for dy in [-1, 0, 1]:
            if (y + dy) in [-1, GRID_HEIGHT + 1]:
                continue
            if dx == dy == 0:
                continue

            neigbours.append((x + dx, y + dy))
    return neigbours


## MAIN LOOP


def main():
    running = True
    playing = False
    count = 0
    update_frequency = 120

    # postions of alive cells
    current_cells = set()

    while running:
        # this loop will run a max of fps per seconnd
        clock.tick(FPS)
        # print(f"count: {count}")
        if playing:
            count += 1

        if count >= update_frequency:
            count = 0
            current_cells = update_grid(current_cells=current_cells)
            
        
        # showing game current state
        pygame.display.set_caption("Playing" if playing else "Paused")

        for event in pygame.event.get():
            # check if event is quit
            if event.type == pygame.QUIT:
                running = False
                count = 0

            # check if any mouse button is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:

                x, y = pygame.mouse.get_pos()

                col = x // TILE_SIZE
                row = y // TILE_SIZE

                toggle_cell(col=col, row=row, current_cells=current_cells)
            
            # check if key button is pressed
            elif event.type == pygame.KEYDOWN:
                # curr_pressed_key
                curr_key = event.key

                # toggle playing
                if curr_key == pygame.K_SPACE:
                    playing = not playing

                # reset game
                if curr_key == pygame.K_r:
                    current_cells = set()
                    playing = False
                    count = 0

                # randomize cells' postions
                if curr_key == pygame.K_c:
                    current_cells = gen(random.randrange(1, 4) * GRID_WIDTH)

        # set screen background to grey
        screen.fill(GREY)

        # draw the grid
        draw_grid(current_cells=current_cells)

        # update the display (necessary to each game)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
