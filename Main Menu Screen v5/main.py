import pygame, sys
from logger import *
from functions import *

logger.info("RealDL - Main Menu Code")

class MainMenu:
    def __init__(self):
        # Pygame setup
        pygame.init()
        info = pygame.display.Info()
        pygame.display.set_caption('Bullet Assault')
        self.clock = pygame.time.Clock()
        self.FPS = 60

        # Window setup
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.DEFAULT_WIDTH = 1920
        self.DEFAULT_HEIGHT = 1080
        self.width_ratio = self.screen_width / self.DEFAULT_WIDTH
        self.height_ratio = self.screen_height / self.DEFAULT_HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Constants setup
        self.BIG_TEXT_SIZE = 50
        self.BASE_TEXT_SIZE = 15
        self.TEXT_HEIGHT = 20
        self.IMAGE_WIDTH = 64
        self.IMAGE_HEIGHT = 64
        self.IMAGE_PADDING = 20
        self.BUTTON_PADDING = 85
        self.CURVE = 10
        self.THICKNESS = 2
        self.BASE_BUTTON_WIDTH = 250
        self.BASE_BUTTON_HEIGHT = 70

        # Variable setup
        self.image_width = int(self.IMAGE_WIDTH*self.width_ratio)
        self.image_height = int(self.IMAGE_HEIGHT*self.height_ratio)
        self.image_padding = int(self.IMAGE_PADDING*self.width_ratio)
        self.button_padding = int(self.BUTTON_PADDING*self.height_ratio)
        self.text_height = int(self.TEXT_HEIGHT*self.height_ratio)
        self.base_text_size = int(self.BASE_TEXT_SIZE*self.height_ratio)
        self.big_text_size = int(self.BIG_TEXT_SIZE*self.height_ratio)
        self.curve = int(self.CURVE*self.height_ratio)
        self.thickness = int(self.THICKNESS*self.height_ratio)
        self.base_button_width = int(self.BASE_BUTTON_WIDTH*self.width_ratio)
        self.base_button_height = int(self.BASE_BUTTON_HEIGHT*self.height_ratio)

        # Images
        self.icon = Images("Images/General/icon.png")
        self.sunset_image = Images("Images/General/bg.png")
        self.icon.display_icon()

        # Setting up Objects for home
        self.youtube_name = Text(self.text_height, "Fonts/Orbitron-Medium.ttf",(27,31,35), None, None, None, self.base_text_size)
        self.github_name = Text(self.text_height, "Fonts/Orbitron-Medium.ttf",(27,31,35), None, None, None, self.base_text_size)
        self.github_button = Button((27,31,35), (27,31,35), self.screen_width-(self.image_width/2)-self.image_padding,(self.image_width/2)+self.image_padding, "Fonts/Orbitron-Regular.ttf", (27,31,35), (27,31,35), self.image_width, self.image_height,'','Image', None, self.big_text_size, self.curve, 'Images/Buttons/github.png')
        self.youtube_button = Button((27,31,35), (27,31,35), self.screen_width-(self.image_width*2)-(self.image_padding/4),(self.image_width/2)+self.image_padding, "Fonts/Orbitron-Regular.ttf", (27,31,35), (27,31,35), self.image_width, self.image_height,'','Image', None, self.big_text_size, self.curve, 'Images/Buttons/youtube.png')
        self.custom_mouse = Mouse("Images/Mouse/mouse1.png", "Images/Mouse/mouse2.png", "Images/Mouse/mouse3.png")
        self.start_button = Button((39, 174, 96), (240,240,240), self.screen_width/2, (self.screen_height/2)-self.button_padding, "Fonts/Orbitron-Medium.ttf", (240,240,240), (39, 174, 96), self.base_button_width, self.base_button_height,'Start','Rectangle', None, int(self.big_text_size/1.3), self.curve)
        self.options_button = Button((39, 96, 174), (240,240,240), self.screen_width/2, self.screen_height/2, "Fonts/Orbitron-Medium.ttf", (240,240,240), (39, 96, 174), self.base_button_width, self.base_button_height,'Options','Rectangle', None, int(self.big_text_size/1.3), self.curve)
        self.quit_button = Button((174, 39, 96), (240,240,240), self.screen_width/2, (self.screen_height/2)+self.button_padding, "Fonts/Orbitron-Medium.ttf", (240,240,240), (174, 39, 96), self.base_button_width, self.base_button_height,'Quit','Rectangle', None, int(self.big_text_size/1.3), self.curve)
        self.current_x = 0

        # Options buttons
        self.options_board = Button((27,31,35), (27,31,35), self.screen_width/2, self.screen_height/2, "Fonts/Orbitron-Regular.ttf", (27,31,35), (27,31,35), self.screen_width*0.7, self.screen_height*0.7,'','Rectangle', None, self.big_text_size, int(self.curve*1.5))
        self.back = Button((174, 39, 96), (27,31,35), self.screen_width/2, self.screen_height*0.78, "Fonts/Orbitron-Medium.ttf", (27,31,35), (174, 39, 96), self.base_button_width, self.base_button_height,'Back','Rectangle', None, int(self.big_text_size/1.3), self.curve)
        self.control_settings = Text(self.text_height, "Fonts/Orbitron-Bold.ttf",(240,240,240), None, None, None, int(self.base_text_size*2))
        self.audio_settings = Text(self.text_height, "Fonts/Orbitron-Bold.ttf",(240,240,240), None, None, None, int(self.base_text_size*2))
        self.underline = Button((27,31,35), (240,240,240), (self.screen_width/2)*0.70, (self.screen_height/2)*0.46,"Fonts/Orbitron-Regular.ttf", (240,240,240), (240,240,240), 275*self.width_ratio, 3.5*self.height_ratio,'','Rectangle', None, self.big_text_size, self.curve)
        self.underline2 = Button((27,31,35), (240,240,240), (self.screen_width/2)*1.3, (self.screen_height/2)*0.46,"Fonts/Orbitron-Regular.ttf", (240,240,240), (240,240,240), 245*self.width_ratio, 3.5*self.height_ratio,'','Rectangle', None, self.big_text_size, self.curve)
        # Control Settings
        self.box_control = Button((27,31,35), (27,31,35), (self.screen_width/2)*0.70, (self.screen_height/2)*0.96, "Fonts/Orbitron-Regular.ttf", (240,240,240), (136,173,227), self.base_button_width*2, self.base_button_height*7,'','Rectangle', None, self.big_text_size, self.curve)
        self.key_binds = Button((27,31,35), (27,31,35), (self.screen_width/2)*0.70, (self.screen_height/2)*0.685, "Fonts/Orbitron-Regular.ttf", (240,240,240), (136,173,227), self.base_button_width, self.base_button_height,'WASD','Rectangle', None, int(self.big_text_size/1.5), self.curve)
        self.movement = Text(self.text_height, "Fonts/Orbitron-Medium.ttf",(240,240,240), None, None, None, int(self.base_text_size*2))
        self.attack_text = Text(self.text_height, "Fonts/Orbitron-Medium.ttf",(240,240,240), None, None, None, int(self.base_text_size*2))
        self.attack_btn = Button((27,31,35), (27,31,35), (self.screen_width/2)*0.70, (self.screen_height/2)*0.935, "Fonts/Orbitron-Regular.ttf", (240,240,240), (136,173,227), self.base_button_width, self.base_button_height,'Space','Rectangle', None, int(self.big_text_size/1.5), self.curve)
        # Audio Settings
        self.box_audio = Button((27,31,35), (27,31,35), (self.screen_width/2)*1.3, (self.screen_height/2)*0.96, "Fonts/Orbitron-Regular.ttf", (240,240,240), (136,173,227), self.base_button_width*2, self.base_button_height*7,'','Rectangle', None, self.big_text_size, self.curve)
        self.volume_text = Text(self.text_height, "Fonts/Orbitron-Medium.ttf",(240,240,240), None, None, None, int(self.base_text_size*2))
        self.volume_bar = Button((27,31,35), (27,31,35), (self.screen_width/2)*1.3, (self.screen_height/2)*0.685, "Fonts/Orbitron-Regular.ttf", (240,240,240), (136,173,227), self.base_button_width*1.5, self.base_button_height*1,'','Rectangle', None, self.big_text_size, self.curve)
        self.volume_line = Button((27,31,35), (27,31,35), (self.screen_width/2)*1.25, (self.screen_height/2)*0.685, "Fonts/Orbitron-Regular.ttf", (240,240,240), (136,173,227), self.base_button_width, self.base_button_height*0.36,'','Rectangle', None, self.big_text_size, self.curve)
        self.volume_button = Button((27,31,35), (51,96,158), (self.screen_width/2)*1.3, (self.screen_height/2)*0.685, "Fonts/Orbitron-Regular.ttf", (240,240,240), (136,173,227), self.base_button_height*0.3, self.base_button_height*0.3,'','Rectangle', None, self.big_text_size, int(self.curve/2))
        self.volume_indicator = Text(self.text_height, "Fonts/Orbitron-Regular.ttf",(240,240,240), None, None, None, int(self.base_text_size*2))
        self.audio_text = Text(self.text_height, "Fonts/Orbitron-Medium.ttf",(240,240,240), None, None, None, int(self.base_text_size*2))
        self.sound_text = Text(self.text_height, "Fonts/Orbitron-Medium.ttf",(240,240,240), None, None, None, int(self.base_text_size*2))
        self.music_text = Text(self.text_height, "Fonts/Orbitron-Medium.ttf",(240,240,240), None, None, None, int(self.base_text_size*2))
        self.sound_box = Button((27,31,35), (39,174,96), (self.screen_width/2)*1.45, (self.screen_height/2)*0.97, "Fonts/Orbitron-Regular.ttf", (240,240,240), (136,173,227), self.base_button_height*0.4, self.base_button_height*0.4,'','Rectangle', None, self.big_text_size, self.curve)
        self.music_box = Button((27,31,35), (39,174,96), (self.screen_width/2)*1.45, (self.screen_height/2)*1.08, "Fonts/Orbitron-Regular.ttf", (240,240,240), (136,173,227), self.base_button_height*0.4, self.base_button_height*0.4,'','Rectangle', None, self.big_text_size, self.curve)
        self.audio_box = Button((27,31,35), (27,31,35), (self.screen_width/2)*1.3, (self.screen_height/2)*1.03, "Fonts/Orbitron-Regular.ttf", (240,240,240), (136,173,227), self.base_button_width*1.5, self.base_button_height*2.5,'','Rectangle', None, self.big_text_size, self.curve)

        # Start
        self.start_board = Button((27,31,35), (27,31,35), self.screen_width/2, self.screen_height/2, "Fonts/Orbitron-Regular.ttf", (27,31,35), (27,31,35), self.screen_width*0.7, self.screen_height*0.7,'','Rectangle', None, self.big_text_size, int(self.curve*1.5))
        self.start_back = Button((174, 39, 96), (27,31,35), self.screen_width/2, self.screen_height*0.78, "Fonts/Orbitron-Medium.ttf", (27,31,35), (174, 39, 96), self.base_button_width, self.base_button_height,'Back','Rectangle', None, int(self.big_text_size/1.3), self.curve)
        self.bullet_assault = Text(self.text_height, "Fonts/Orbitron-Bold.ttf",(240,240,240), None, None, None, int(self.base_text_size*3.5))
        self.join_message = Text(self.text_height, "Fonts/Orbitron-Regular.ttf",(240,240,240), None, None, None, int(self.base_text_size*1.7))
        self.ip_text_box = TextBox(self.base_button_width*2.5, self.base_button_height*1.5, (self.screen_width/2), (self.screen_height/2)*0.99, (240,240,240), (200,200,200),"Fonts/Orbitron-Regular.ttf",self.curve,self.thickness,self.base_button_width*2.5)
        self.join_boarder = Button((27,31,35), (27,31,35), (self.screen_width/2), (self.screen_height/2), "Fonts/Orbitron-Regular.ttf", (240,240,240), (136,173,227), self.base_button_width*3, self.base_button_height*6,'','Rectangle', None, self.big_text_size, self.curve)
        self.join_btn = Button((39, 174, 96), (27,31,35), (self.screen_width/2), (self.screen_height/2)*1.445-self.button_padding, "Fonts/Orbitron-Medium.ttf", (27,31,35), (39, 174, 96), self.base_button_width, self.base_button_height,'Connect','Rectangle', None, int(self.big_text_size/1.3), self.curve)
        self.server_ip_text = Text(self.text_height, "Fonts/Orbitron-Regular.ttf",(240,240,240), None, None, None, int(self.base_text_size*1.7))
        self.name_text_box = TextBox(self.base_button_width*2.5, self.base_button_height*1.5, (self.screen_width/2), (self.screen_height/2)*0.70, (240,240,240), (200,200,200),"Fonts/Orbitron-Regular.ttf",self.curve,self.thickness,self.base_button_width*2.5)
        self.name_box_text = Text(self.text_height, "Fonts/Orbitron-Regular.ttf",(240,240,240), None, None, None, int(self.base_text_size*1.7))

        # Settings
        self.main_menu_pages = "home"
        self.settings_screen = "control"
        self.attack_keys = "Space"
        self.keys = "WASD"
        # Volume
        self.min_vol_x = self.volume_line.x + self.volume_button.width/3 + 1 
        self.max_vol_x = self.volume_line.x + self.volume_line.width - (self.volume_button.width*2)/3 - 1
        self.volume_ratio = 100 / (self.max_vol_x - self.min_vol_x)
        self.volume = int(self.volume_ratio * ((self.volume_button.x + self.volume_button.width/4) - self.min_vol_x))
        self.sound_change = 0
        self.music_change = 0

    def close(self):
        pygame.quit()
        sys.exit()

    def options(self):
        self.main_menu_pages = "settings"

    def home(self):
        self.main_menu_pages = "home"

    def start_option(self):
        self.main_menu_pages = "start"

    def draw_moving_background(self):
        # Draw the mvoing image on the screen
        self.sunset_image.draw(self.current_x, 0)
        self.sunset_image.draw((self.current_x - self.sunset_image.rect.width), 0)
        self.current_x += 1

        # If the image has moved beyond its width, reset it to 0
        if self.current_x >= self.sunset_image.rect.width:
            self.current_x = 0

    def change_keys(self):
        if self.keys == 'WASD':
            self.keys = 'Arrow Keys'
        else:
            self.keys = 'WASD'

    def control_settings_change(self):
        self.settings_screen = "control"

    def audio_settings_change(self):
        self.settings_screen = "audio"

    def change_attack(self):
        # Changes the key binds.
        if self.attack_keys == "Space":
            self.attack_keys = "L-Ctrl"
        elif self.attack_keys == "L-Ctrl":
            self.attack_keys = "R-Ctrl"
        else:
             self.attack_keys = "Space"

    def sound_box_color(self):
        # Changes the sound box color
        self.sound_change += 1
        if self.sound_change == 1:
            self.sound_box.color = (39,174,96)
        else:
            self.sound_change = 0
            self.sound_box.color = (27,31,35)       

    def music_box_color(self):
        # Changes the music box check color.
        self.music_change += 1
        if self.music_change == 1:
            self.music_box.color = (39,174,96)
        else:
            self.music_change = 0
            self.music_box.color = (27,31,35)
        
    def volume_settings(self):
        # Get the mouse and sets the volume to where the mosue is.
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] - self.volume_button.width/3 > self.volume_line.x:
            if mouse_pos[0] + (self.volume_button.width/3)*2 < self.volume_line.x + self.volume_line.width:
                self.volume_button.x = mouse_pos[0] - self.volume_button.width/3
                self.volume = int(self.volume_ratio * (mouse_pos[0] - self.min_vol_x))

    def start_game(self):
        self.starting_dict = {
            "settings": {
                "control": {
                    "movement": self.keys,
                    "offense": self.attack_keys
                },
                "audio": {
                    "volume": self.volume,
                    "sound": True if self.sound_change == 1 else False,
                    "music": True if self.music_change == 1 else False
                }
            },
            "start": {
                "username": self.name_text_box.return_text() or "Player",
                "server_ip": self.ip_text_box.return_text() or "Server IP"
            }
        }
        
        # Check the values
        """
        for category, subcategories in self.starting_dict.items():
            print(f"{category}:")
            for subcategory, values in subcategories.items():
                print(f"  {subcategory}:")
                if isinstance(values, dict):
                    for key, value in values.items():
                        print(f"    {key}: {value}")
                else:
                    print(f"    {values}")

        """

    def draw_objects(self, events):
        # Draw the buttons and check for hover
        if self.main_menu_pages == "home":
            self.github_button.draw((27,31,35),None,"https://github.com/TheRealDL1/Simple-Client-Server")
            self.youtube_button.draw((27,31,35),None,"https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            self.start_button.draw((27,31,35),self.start_option)
            self.options_button.draw((27,31,35),self.options)
            self.quit_button.draw((27,31,35),self.close,None,True)
            
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
            self.control_settings.draw("draw","Control Settings", (self.screen_width/2)*0.70, (self.screen_height/2)*0.42,self.control_settings_change)
            self.audio_settings.draw("draw","Audio Settings", (self.screen_width/2)*1.3, (self.screen_height/2)*0.42,self.audio_settings_change)
            self.github_button.draw((27,31,35),None,"https://github.com/TheRealDL1/Simple-Client-Server")
            self.youtube_button.draw((27,31,35),None,"https://www.youtube.com/@dominicpike")

            back_hover = self.back.is_hovered()
            github_button_hover = self.github_button.is_hovered()
            youtube_button_hover = self.youtube_button.is_hovered()
            key_binds_hover = self.control_settings.is_hovered()
            audio_hover = self.audio_settings.is_hovered()
            key_hover = self.key_binds.is_hovered()
            attack_hover = self.attack_btn.is_hovered()
            volume_btn_hover = self.volume_button.is_hovered()
            sound_box_hover = self.sound_box.is_hovered()
            music_box_hover = self.music_box.is_hovered()

            back_click = self.back.is_clicking()
            github_button_click = self.github_button.is_clicking()
            youtube_button_click = self.youtube_button.is_clicking()
            key_binds_click = self.control_settings.is_clicking()
            audio_click = self.audio_settings.is_clicking()
            key_click = self.key_binds.is_clicking()
            attack_click = self.attack_btn.is_clicking()
            volume_btn_click = self.volume_button.is_clicking()
            sound_box_click = self.sound_box.is_clicking()
            music_box_click = self.music_box.is_clicking()

            if back_hover or github_button_hover or youtube_button_hover or key_binds_hover or audio_hover or key_hover or attack_hover or volume_btn_hover or sound_box_hover or music_box_hover:
                if github_button_hover: self.github_name.draw("draw","Github", self.screen_width-(self.image_width/2)-self.image_padding, (self.image_width/2)+self.image_padding*3.1)
                else: self.github_name.draw("undraw","Github", self.screen_width-(self.image_width/2)-self.image_padding, (self.image_width/2)+self.image_padding*3.1)
                
                if youtube_button_hover: self.youtube_name.draw("draw","Youtube", self.screen_width-(self.image_width*2)-(self.image_padding/4), (self.image_width/2)+self.image_padding*3.1) 
                else: self.youtube_name.draw("undraw","Youtube", self.screen_width-(self.image_width*2)-(self.image_padding/4), (self.image_width/2)+self.image_padding*3.1) 

                if not back_click and not github_button_click and not youtube_button_click and not key_binds_click and not audio_click and not key_click and not attack_click and not volume_btn_click and not sound_box_click and not music_box_click:
                    self.custom_mouse.mode = 1
                else:
                    if volume_btn_click:
                        self.volume_settings()
                    self.custom_mouse.mode = 2
            else:
                self.custom_mouse.mode = 0
                self.github_name.draw("undraw","Github", self.screen_width-(self.image_width/2)-self.image_padding, (self.image_width/2)+self.image_padding*3.1)
                self.youtube_name.draw("undraw","Youtube", self.screen_width-(self.image_width*2)-(self.image_padding/4), (self.image_width/2)+self.image_padding*3.1) 

            if self.settings_screen == "control":
                if audio_hover: self.underline2.draw(None,None,None,True,None,None,None,"draw")
                else: self.underline2.draw(None,None,None,True,None,None,None,"undraw")
                self.underline.draw(None,None,None,True,None,None,None,"draw")
                self.box_control.draw((240,240,240))
                self.movement.draw("draw","Movement", (self.screen_width/2)*0.70, (self.screen_height/2)*0.57)
                self.key_binds.draw((240,240,240),self.change_keys, None, True, self.keys)
                self.attack_text.draw("draw","Offense", (self.screen_width/2)*0.70, (self.screen_height/2)*0.82)
                self.attack_btn.draw((240,240,240),self.change_attack, None, True, self.attack_keys)
                
            elif self.settings_screen == "audio":
                if key_binds_hover: self.underline.draw(None,None,None,True,None,None,None,"draw")
                else: self.underline.draw(None,None,None,True,None,None,None,"undraw")
                self.underline2.draw(None,None,None,True,None,None,None,"draw")
                self.box_audio.draw((240,240,240))
                self.volume_text.draw("draw","Volume", (self.screen_width/2)*1.3, (self.screen_height/2)*0.57)
                self.volume_bar.draw((240,240,240))
                self.volume_line.draw((240,240,240))
                self.volume_button.draw((240,240,240))
                self.volume_indicator.draw("draw",str(self.volume), (self.screen_width/2)*1.435, (self.screen_height/2)*0.685)
                self.audio_text.draw("draw","Audio",(self.screen_width/2)*1.3, (self.screen_height/2)*0.82)
                self.audio_box.draw((240,240,240))
                self.sound_text.draw("draw","Sound",(self.screen_width/2)*1.185, (self.screen_height/2)*0.97)
                self.music_text.draw("draw","Music",(self.screen_width/2)*1.18, (self.screen_height/2)*1.08)
                self.sound_box.draw((240,240,240),self.sound_box_color)
                self.music_box.draw((240,240,240),self.music_box_color)

        if self.main_menu_pages == "start":
            self.options_board.draw((27,31,35),None, None, False)
            self.start_back.draw((240,240,240),self.home)
            self.github_button.draw((27,31,35),None,"https://github.com/TheRealDL1/Simple-Client-Server")
            self.youtube_button.draw((27,31,35),None,"https://www.youtube.com/@dominicpike")
            self.join_boarder.draw((240,240,240))
            self.bullet_assault.draw("draw","Bullet Assault", (self.screen_width/2), (self.screen_height/2)*0.43)
            self.server_ip_text.draw("draw","Server IP Address", (self.screen_width/2), (self.screen_height/2)*0.955)
            message = "Enter the Server's IP Address that you want to join!"
            self.join_message.draw("draw",message, (self.screen_width/2), (self.screen_height/2)*0.52)
            self.ip_text_box.draw()
            self.ip_text_box.updateText(events)
            self.ip_text_box.update()
            self.join_btn.draw((240,240,240),self.start_game)

            # Name Text Box
            self.name_box_text.draw("draw","Username",(self.screen_width/2), (self.screen_height/2)*0.665)
            self.name_text_box.draw()
            self.name_text_box.updateText(events)
            self.name_text_box.update()

            github_button_hover = self.github_button.is_hovered()
            youtube_button_hover = self.youtube_button.is_hovered()
            start_back_hover = self.start_back.is_hovered()
            join_hover = self.join_btn.is_hovered()
            text_box_hover = self.ip_text_box.is_hovered()
            name_hover = self.name_text_box.is_hovered()

            github_button_click = self.github_button.is_clicking()
            youtube_button_click = self.youtube_button.is_clicking()
            start_back_click = self.start_back.is_clicking()
            join_click = self.join_btn.is_clicking()
            text_box_click = self.ip_text_box.is_clicking()
            name_click = self.name_text_box.is_clicking()

            if start_back_hover or github_button_hover or youtube_button_hover or join_hover or text_box_hover or name_hover:
                # Draw hover text.
                if github_button_hover: self.github_name.draw("draw","Github", self.screen_width-(self.image_width/2)-self.image_padding, (self.image_width/2)+self.image_padding*3.1)
                else: self.github_name.draw("undraw","Github", self.screen_width-(self.image_width/2)-self.image_padding, (self.image_width/2)+self.image_padding*3.1)
                
                if youtube_button_hover: self.youtube_name.draw("draw","Youtube", self.screen_width-(self.image_width*2)-(self.image_padding/4), (self.image_width/2)+self.image_padding*3.1) 
                else: self.youtube_name.draw("undraw","Youtube", self.screen_width-(self.image_width*2)-(self.image_padding/4), (self.image_width/2)+self.image_padding*3.1) 

                if not start_back_click and not github_button_click and not youtube_button_click and not join_click and not text_box_click and not name_click:
                    self.custom_mouse.mode = 1
                else:
                    self.custom_mouse.mode = 2
            else:
                self.custom_mouse.mode = 0
                self.github_name.draw("undraw","Github", self.screen_width-(self.image_width/2)-self.image_padding, (self.image_width/2)+self.image_padding*3.1)
                self.youtube_name.draw("undraw","Youtube", self.screen_width-(self.image_width*2)-(self.image_padding/4), (self.image_width/2)+self.image_padding*3.1) 

        # Draw the mouse
        self.custom_mouse.draw()

    def redraw_window(self, events):
        self.draw_moving_background()
        self.draw_objects(events)

    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.close()

            # Update the display and frame rate
            self.redraw_window(events)
            pygame.display.update()
            self.clock.tick(self.FPS)

if __name__ == "__main__":
    game = MainMenu()
    game.run()
