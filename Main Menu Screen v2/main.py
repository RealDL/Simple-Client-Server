import pygame, sys
from functions import *

class MainMenu:
    def __init__(self):
        # Setting up Game Menu
        pygame.init()
        info = pygame.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Setting up Objects
        self.image_button = self.start_button = Button((0,0,0), (0,0,0), self.screen_width-52,52, "Fonts/Orbitron-Regular.ttf", (0,0,0), (0,0,0), 64, 64,'','Image', None, 50, 10, 'Images/github.png')
        self.sunset_image = Images("Images/bg.png")
        self.custom_mouse = Mouse("Images/mouse.png", "Images/mouse2.png", "Images/mouse3.png")
        self.start_button = Button((255, 255, 255), (12, 182, 29), 960, 455, "Fonts/Orbitron-Regular.ttf", (12, 182, 29), (255, 255, 255), 250, 70,'Start','Rectangle', None, 50, 10)
        self.options_button = Button((255, 255, 255), (12, 182, 29), 960, 540, "Fonts/Orbitron-Regular.ttf", (12, 182, 29), (255, 255, 255), 250, 70,'Options','Rectangle', None, 50, 10)
        self.quit_button = Button((255, 255, 255), (12, 182, 29), 960, 625, "Fonts/Orbitron-Regular.ttf", (12, 182, 29), (255, 255, 255), 250, 70,'Quit','Rectangle', None, 50, 10)
        self.current_x = 0

        # Set the frame rate (frames per second)
        self.FPS = 60
        self.clock = pygame.time.Clock()

    def close(self):
        pygame.quit()
        sys.exit()

    def draw_moving_background(self):
        # Draw the mvoing image on the screen
        self.sunset_image.draw(self.current_x, 0)
        self.sunset_image.draw((self.current_x - self.sunset_image.rect.width), 0)
        self.current_x += 1

        # If the image has moved beyond its width, reset it to 0
        if self.current_x >= self.sunset_image.rect.width:
            self.current_x = 0

    def draw_objects(self):
        # Draw the buttons and check for hover
        self.image_button.draw((27,31,35),None,"https://github.com/TheRealDL1/Simple-Client-Server")
        self.start_button.draw((0,0,0))
        self.options_button.draw((0,0,0))
        self.quit_button.draw((0,0,0),self.close)
        start_button_hover = self.start_button.is_hovered()
        options_button_hover = self.options_button.is_hovered()
        quit_button_hover = self.quit_button.is_hovered()
        image_button_hover = self.image_button.is_hovered()

        start_button_click = self.start_button.is_clicking()
        options_button_click = self.options_button.is_clicking()
        quit_button_click  = self.quit_button.is_clicking()
        image_button_click = self.image_button.is_clicking()

        # Check if mouse is hovering over buttons
        if start_button_hover or options_button_hover or quit_button_hover or image_button_hover:
            if not start_button_click and not options_button_click and not quit_button_click and not image_button_click:
                self.custom_mouse.mode = 1
            else:
                self.custom_mouse.mode = 2
        else:
            self.custom_mouse.mode = 0

        # Draw the mouse
        self.custom_mouse.draw()

    def redraw_window(self):
        self.draw_moving_background()
        self.draw_objects()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.close()

            # Update the display and frame rate
            self.redraw_window()
            pygame.display.update()
            self.clock.tick(self.FPS)

if __name__ == "__main__":
    game = MainMenu()
    game.run()
