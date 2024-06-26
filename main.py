import pygame

#initialize pygame
pygame.init()

#RGB colors
BLACK = (0, 0, 0)

GREY = (128, 128, 128)

PURPLE = (128, 0, 128)

# Window dimensions
WIDTH, HEIGHT = 600, 600

# single cell size (20x20)
TILE_SIZE = 20

# Grid size 
GRID_WIDTH = WIDTH//TILE_SIZE

GRID_HEIGHT = HEIGHT//TILE_SIZE

# Frames per second
FPS = 60

# set new game window object dimensions
screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()


# A function to draw grid
def draw_grid(current_cells):
    
    # draw grid horizontal lines
    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen , BLACK,(0,row*TILE_SIZE),(WIDTH,row * TILE_SIZE))
    
    # draw grid vertical lines
    for column in range(GRID_WIDTH):
        pygame.draw.line(screen , BLACK,(column*TILE_SIZE,0),(column*TILE_SIZE,HEIGHT))
    
    
        
    

## MAIN LOOP

def main():
    running = True
    
    # postions of alive cells 
    current_cells=set()
    
    while running:
        # this loop will run a max of fps per seconnd
        clock.tick(FPS)
        
        for event in pygame.event.get():
            # check if event is quit
            if event.type == pygame.QUIT:
                running = False
            
        # set screen background to grey
        screen.fill(GREY)
        
        # draw the grid
        draw_grid(current_cells=current_cells)
        
        # update the display (necessary to each game)
        pygame.display.update()
    
    pygame.quit()
    
    

if __name__=="__main__":
    main()
                
        


