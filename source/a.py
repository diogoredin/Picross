import pygame

# Initialize the game engine
pygame.init()

# Configures the display
size = (800,600) # width & height
pygame.display.set_caption('Picross Game')# Title

# Open the display
screen = pygame.display.set_mode(size)


# Define some colors
black = (  0,   0,   0)
white = (255, 255, 255)
green = (  0, 225,   0)
red   = (255,   0,   0)
blue  = (  0,   0, 255)

pygame.display.update()

# Loop control
gameExit = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ----------- Main program loop ----------
while not gameExit:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user cicked close
            gameExit = True # Flag that the loop has to end
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT


    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT    


    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT    

    # ALL CODE TO DRAW SHOULD GO ABOOVE THIS COMMENT

    # Limit to 20  frames per second
    clock.tick(20)
    
pygame.quit()

