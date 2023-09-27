import pygame, sys
from logger import *
from functions import *

logger.info("RealDL - Main Code")

class MainMenu:
    def __init__(self):
        # Setting up Game Menu
        pygame.init()
        info = pygame.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.icon = Images("Images/General/icon.png")
        self.sunset_image = Images("Images/General/bg.png")
        self.icon.display_icon()
        pygame.display.set_caption('Bullet Assault')
        self.image_width = 64
        self.image_height = 64
        self.image_padding = 20
        self.button_padding = 85
        self.main_menu_pages = "home"

        # Setting up Objects for home
        self.youtube_name = Text(20, "Fonts/Orbitron-Medium.ttf",(27,31,35), None, None, None, 15)
        self.github_name = Text(20, "Fonts/Orbitron-Medium.ttf",(27,31,35), None, None, None, 15)
        self.github_button = Button((0,0,0), (0,0,0), self.screen_width-(self.image_width/2)-self.image_padding,(self.image_width/2)+self.image_padding, "Fonts/Orbitron-Regular.ttf", (0,0,0), (0,0,0), 64, 64,'','Image', None, 50, 10, 'Images/Buttons/github.png')
        self.youtube_button = Button((0,0,0), (0,0,0), self.screen_width-(self.image_width*2)-(self.image_padding/4),(self.image_width/2)+self.image_padding, "Fonts/Orbitron-Regular.ttf", (0,0,0), (0,0,0), 64, 64,'','Image', None, 50, 10, 'Images/Buttons/youtube.png')
        self.custom_mouse = Mouse("Images/Mouse/mouse1.png", "Images/Mouse/mouse2.png", "Images/Mouse/mouse3.png")
        self.start_button = Button((39, 174, 96), (240,240,240), self.screen_width/2, (self.screen_height/2)-self.button_padding, "Fonts/Orbitron-Regular.ttf", (240,240,240), (39, 174, 96), 250, 70,'Start','Rectangle', None, 50, 10)
        self.options_button = Button((39, 96, 174), (240,240,240), self.screen_width/2, self.screen_height/2, "Fonts/Orbitron-Regular.ttf", (240,240,240), (39, 96, 174), 250, 70,'Options','Rectangle', None, 50, 10)
        self.quit_button = Button((174, 39, 96), (240,240,240), self.screen_width/2, (self.screen_height/2)+self.button_padding, "Fonts/Orbitron-Regular.ttf", (240,240,240), (174, 39, 96), 250, 70,'Quit','Rectangle', None, 50, 10)
        self.current_x = 0

        # Options buttons
        self.options_board = Button((15,15,15), (15,15,15), self.screen_width/2, self.screen_height/2, "Fonts/Orbitron-Regular.ttf", (15,15,15), (15,15,15), self.screen_width*0.7, self.screen_height*0.7,'','Rectangle', None, 50, 15)
        self.back = Button((174, 39, 96), (15,15,15), self.screen_width/2, self.screen_height*0.78, "Fonts/Orbitron-Regular.ttf", (15,15,15), (174, 39, 96), 250, 70,'Back','Rectangle', None, 50, 10)
        
        # We need buttons for Audio settings: volume, sound mode, mute all.
        #                     Control settings: key binds. 
        #                     Game play settings: change character.

        # Set the frame rate (frames per second)
        self.FPS = 60
        self.clock = pygame.time.Clock()

    def close(self):
        pygame.quit()
        sys.exit()

    def options(self):
        self.main_menu_pages = "settings"

    def home(self):
        self.main_menu_pages = "home"

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
        if self.main_menu_pages == "home":
            self.github_button.draw((27,31,35),None,"https://github.com/TheRealDL1/Simple-Client-Server")
            self.youtube_button.draw((27,31,35),None,"https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            self.start_button.draw((0,0,0))
            self.options_button.draw((0,0,0),self.options)
            self.quit_button.draw((0,0,0),self.close)
            start_button_hover = self.start_button.is_hovered()
            options_button_hover = self.options_button.is_hovered()
            quit_button_hover = self.quit_button.is_hovered()
            github_button_hover = self.github_button.is_hovered()
            youtube_button_hover = self.youtube_button.is_hovered()

            start_button_click = self.start_button.is_clicking()
            options_button_click = self.options_button.is_clicking()
            quit_button_click  = self.quit_button.is_clicking()
            github_button_click = self.github_button.is_clicking()
            youtube_button_click = self.youtube_button.is_clicking()

            # Check if mouse is hovering over buttons
            if start_button_hover or options_button_hover or quit_button_hover or github_button_hover or youtube_button_hover:
                # Draw hover text.
                if github_button_hover: self.github_name.draw("draw","Github", self.screen_width-(self.image_width/2)-self.image_padding, (self.image_width/2)+self.image_padding*3.1)
                else: self.github_name.draw("undraw","Github", self.screen_width-(self.image_width/2)-self.image_padding, (self.image_width/2)+self.image_padding*3.1)
                
                if youtube_button_hover: self.youtube_name.draw("draw","Youtube", self.screen_width-(self.image_width*2)-(self.image_padding/4), (self.image_width/2)+self.image_padding*3.1) 
                else: self.youtube_name.draw("undraw","Youtube", self.screen_width-(self.image_width*2)-(self.image_padding/4), (self.image_width/2)+self.image_padding*3.1) 

                if not start_button_click and not options_button_click and not quit_button_click and not github_button_click and not youtube_button_click:
                    self.custom_mouse.mode = 1
                else:
                    self.custom_mouse.mode = 2
            else:
                self.custom_mouse.mode = 0
                self.github_name.draw("undraw","Github", self.screen_width-(self.image_width/2)-self.image_padding, (self.image_width/2)+self.image_padding*3.1)
                self.youtube_name.draw("undraw","Youtube", self.screen_width-(self.image_width*2)-(self.image_padding/4), (self.image_width/2)+self.image_padding*3.1) 

        if self.main_menu_pages == "settings":
            self.options_board.draw((27,31,35),None, None, False)
            self.back.draw((240,240,240),self.home)
            self.github_button.draw((27,31,35),None,"https://github.com/TheRealDL1/Simple-Client-Server")
            self.youtube_button.draw((27,31,35),None,"https://www.youtube.com/watch?v=dQw4w9WgXcQ")

            back_hover = self.back.is_hovered()
            github_button_hover = self.github_button.is_hovered()
            youtube_button_hover = self.youtube_button.is_hovered()

            back_click = self.back.is_clicking()
            github_button_click = self.github_button.is_clicking()
            youtube_button_click = self.youtube_button.is_clicking()
    
            if back_hover or github_button_hover or youtube_button_hover:
                if github_button_hover: self.github_name.draw("draw","Github", self.screen_width-(self.image_width/2)-self.image_padding, (self.image_width/2)+self.image_padding*3.1)
                else: self.github_name.draw("undraw","Github", self.screen_width-(self.image_width/2)-self.image_padding, (self.image_width/2)+self.image_padding*3.1)
                
                if youtube_button_hover: self.youtube_name.draw("draw","Youtube", self.screen_width-(self.image_width*2)-(self.image_padding/4), (self.image_width/2)+self.image_padding*3.1) 
                else: self.youtube_name.draw("undraw","Youtube", self.screen_width-(self.image_width*2)-(self.image_padding/4), (self.image_width/2)+self.image_padding*3.1) 

                if not back_click and not github_button_click and not youtube_button_click:
                    self.custom_mouse.mode = 1
                else:
                    self.custom_mouse.mode = 2
            else:
                self.custom_mouse.mode = 0
                self.github_name.draw("undraw","Github", self.screen_width-(self.image_width/2)-self.image_padding, (self.image_width/2)+self.image_padding*3.1)
                self.youtube_name.draw("undraw","Youtube", self.screen_width-(self.image_width*2)-(self.image_padding/4), (self.image_width/2)+self.image_padding*3.1) 

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
