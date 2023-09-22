import pygame, sys
from functions import *

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 1920
screen_height = 1080

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Load your wide sunset background image
sunset_image = Images("bg.png")

# Initialize variables
current_x = 0  # Current position of the image

# Set the frame rate (frames per second)
FPS = 60
clock = pygame.time.Clock()

# Create the button
boarder1 = Button((150, 150, 150), (12, 182, 29), 960, 455, "Orbitron-Regular.ttf", (12, 182, 29), (150, 150, 150), 250, 70,'Start','Rectangle', None, 50, 10)
boarder2 = Button((150, 150, 150), (12, 182, 29), 960, 540, "Orbitron-Regular.ttf", (12, 182, 29), (150, 150, 150), 250, 70,'Options','Rectangle', None, 50, 10)
boarder3 = Button((150, 150, 150), (12, 182, 29), 960, 625, "Orbitron-Regular.ttf", (12, 182, 29), (150, 150, 150), 250, 70,'Quit','Rectangle', None, 50, 10)
#startButton = WordButton(960, 455, "Start", (12, 182, 29), (40, 220, 58), "Orbitron-Regular.ttf", "Orbitron-Medium.ttf", 40)
#optionsButton = WordButton(960, 540, "Options", (12, 182, 29), (40, 220, 58), "Orbitron-Regular.ttf", "Orbitron-Medium.ttf", 40)
#quitButton = WordButton(960, 625, "Quit", (12, 182, 29), (40, 220, 58), "Orbitron-Regular.ttf", "Orbitron-Medium.ttf", 40)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Draw the image on the screen
    sunset_image.draw(screen, current_x, 0)

    # Copy a portion of the image to the left to create a seamless loop
    sunset_image.draw(screen,(current_x - sunset_image.rect.width), 0)

    # Draw the button
    boarder1.draw(screen, (0,0,0))
    boarder2.draw(screen, (0,0,0))
    boarder3.draw(screen, (0,0,0))
    #startButton.displayText(screen)
    #optionsButton.displayText(screen)
    #quitButton.displayText(screen)


    # Update the display
    pygame.display.flip()

    # Move the image to the right by one pixel
    current_x += 1

    # If the image has moved beyond its width, reset it to 0
    if current_x >= sunset_image.rect.width:
        current_x = 0

    # Limit the frame rate
    clock.tick(FPS)
