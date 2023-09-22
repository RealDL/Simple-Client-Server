import pygame, webbrowser, time
print("Pygame Functions 0.0.1 (Python 3.11.0)\nI am not affliated with pygame. https://github.com/TheRealDL1/pygame_functions")

class Images(object):
    def __init__(self, image):
        self.image = image
        try:
            self.load_image = pygame.image.load(self.image).convert()
        except:
            self.load_image = pygame.image.load(f"../{self.image}").convert()
        self.rect = self.load_image.get_rect()
    def display_icon(self):
        pygame.display.set_icon(self.load_image)
    def draw(self, win, x=0, y=0):
        win.blit(self.load_image, (x,y))

class WordButton(object):
    def __init__(self, x, y, text, color1, color2,  basefont, largefont, textSize=30,):
        """Sets the values for button"""
        self.color = color1
        self.color2 = color2
        self.x = x
        self.y = y
        self.text = text
        self.textSize = textSize
        self.largeSize = round(self.textSize * 1.25)
        self.basefont = basefont
        self.largefont = largefont
        try:
            self.base_font = pygame.font.Font(self.basefont, self.textSize)
            self.large_font = pygame.font.Font(self.largefont, self.largeSize)
        except:
            self.base_font = pygame.font.Font(f"../{self.basefont}", self.textSize)
            self.large_font = pygame.font.Font(f"../{self.largefont}", self.largeSize)
        self.hover = False
        self.click = False
        self.release = False

    def displayText(self, win, newText=None, action=None, link=None):
        if newText != None:
            self.text = newText
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Render text with both fonts
        text = self.large_font.render(self.text, 1, self.color2)
        text2 = self.base_font.render(self.text, 1, self.color)

        # Check if mouse is over the text
        if self.x + text.get_width()/2> mouse[0] > self.x - text.get_width()/2 and self.y + text.get_height()/2  > mouse[1] > self.y - text.get_height()/2:
            self.hover = True
            # Render text with larger font and lighter color
            text = self.large_font.render(self.text, 1, self.color2)

            # Center text vertically as well as horizontally
            win.blit(text, (self.x - text.get_width() / 2, self.y - text.get_height() / 2))

            # Check for mouse click and run action if specified
            if click[0] == 1:
                self.click = True
            
            if self.click == True and not click[0]:
                self.release = True
            
            if self.release:
                if action != None:
                    action()
                if link != None:
                    webbrowser.open(link)
                self.release = False
                self.click = False
        else:
            self.hover = False
            self.click = False
            self.release = False
            # Render text with base font and color
            text2 = self.base_font.render(self.text, 1, self.color)

            # Center text vertically as well as horizontally
            win.blit(text2, (self.x - text2.get_width() / 2, self.y - text2.get_height() / 2))



class Animation(object):
    def __init__(self, image, scale, scale_direction, scale_min, scale_max, scale_speed, screen_y, screen_x):
        self.scale = scale #1.0
        self.image = image
        self.scale_direction = scale_direction #-1.35  # Start by zooming out
        self.scale_min = scale_min #0.9
        self.scale_max = scale_max #1.2
        self.scale_speed = scale_speed #0.01  # The rate at which the scale changes
        self.screen_center_x = screen_x
        self.screen_center_y = screen_y #324#win.get_height() // 2
        self.monopoly_rect = self.image.get_rect(center=(self.screen_center_x, self.screen_center_y))

    def animation(self, win):
        self.scale += self.scale_direction * self.scale_speed
        if self.scale <= self.scale_min:
            if self.scale_direction < 0:
                self.scale_direction = self.scale_direction * -1
            else:
                self.scale_direction = self.scale_direction * 1# Start zooming in
        elif self.scale >= self.scale_max:
            if self.scale_direction > 0:
                self.scale_direction = self.scale_direction * -1
            else:
                self.scale_direction = self.scale_direction * 1  # Start zooming out

        # Scale the image and get its rect
        scaled_monopoly = pygame.transform.rotozoom(self.image, 0, self.scale)
        scaled_monopoly_rect = scaled_monopoly.get_rect(center=(self.screen_center_x, self.screen_center_y))

        # Blit the scaled image to the screen and update the display
        win.blit(scaled_monopoly, scaled_monopoly_rect)

class TextBox(object):
    def __init__(self, width, height, x, y, color1, color2, textfont, curve, thickness, maxTextWidth):
        self.text = ''
        self.textSize = 60
        self.textfont = textfont
        self.base_font = pygame.font.Font(self.textfont, self.textSize)
        self.active = False
        self.width = width
        self.height = height
        self.x = x - self.width / 2
        self.ogWidth = width
        self.y = y
        self.color_active = pygame.Color(color1)
        self.color_passive = pygame.Color(color2)
        self.color = self.color_passive
        self.last_update = 0 # time of last update
        self.show_cursor = False # whether to show cursor or not
        self.cursor = 0
        self.maxTextWidth = maxTextWidth
        self.curve = curve
        self.thickness = thickness
    def draw(self, win):
        area = [self.x,self.y,self.width,self.height]
        pygame.draw.rect(win, self.color, area, self.thickness, self.curve)
        
    def checkTextBox(self):
        mouse = pygame.mouse.get_pos()
        
        if self.x+self.width > mouse[0] > self.x and self.y+self.height > mouse[1] > self.y:
            self.active = True
        else:
            self.active = False

        if self.active:
            self.color = self.color_active
        else:
            self.color = self.color_passive
            
    def update(self, win, x_pos=None, y_pos=None):
        middleOfX = win.get_width() // 2
        if x_pos is None:
            x_pos = self.x
        if y_pos is None:
            y_pos = self.y
        if self.text:
            surface_area = self.base_font.render(self.text, True, (0, 0, 0))
            text_width = surface_area.get_width() + 20
            if self.ogWidth > self.width:
                self.width = self.ogWidth
                self.x = middleOfX - self.width // 2
            if text_width > self.width:
                self.width = text_width
                self.x = middleOfX - self.width // 2
            elif self.width > text_width:
                if self.ogWidth < self.width:
                    self.width = text_width
                    self.x = middleOfX - self.width // 2
            win.blit(surface_area, (x_pos + 5, y_pos + (self.height // 2 - surface_area.get_height() // 2)))
        else:
            self.width = self.ogWidth
            self.x = middleOfX - self.width // 2
            surface_area = self.base_font.render(self.text, True, (0, 0, 0))
            win.blit(surface_area, (x_pos + 5, y_pos + (self.height // 2 - surface_area.get_height() // 2)))

        time_since_last_update = pygame.time.get_ticks() - self.last_update
        if self.active and time_since_last_update > 500:
            self.show_cursor = not self.show_cursor
            self.last_update = pygame.time.get_ticks()

        if self.show_cursor and self.active == True:
            cursor_width = 2
            cursor_pos = self.base_font.size(self.text[:self.cursor])[0] - 5
            text_to_show = self.text[:self.cursor] + '|' + self.text[self.cursor:]
            cursor_pos += self.base_font.size(' ')[0] * 0.8
            surface_area = self.base_font.render(text_to_show, True, (0, 0, 0))
            cursor_area = pygame.Surface((cursor_width, surface_area.get_height()))
            cursor_area.fill((0, 0, 0))
            win.blit(cursor_area, (x_pos + cursor_pos, y_pos + (self.height // 2 - cursor_area.get_height() // 2)), (0, 0, cursor_width, cursor_area.get_height()))
        else:
            surface_area = self.base_font.render(self.text, True, (0, 0, 0))
            win.blit(surface_area, (x_pos + 5, y_pos + (self.height // 2 - surface_area.get_height() // 2)))

    def updateText(self, events, function):
        surface_area = self.base_font.render(self.text, True, (0, 0, 0))
        text_width = surface_area.get_width() + 20
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.checkTextBox()
            if event.type == pygame.KEYDOWN:
                if self.active == True:
                    if event.key == pygame.K_BACKSPACE:
                        if self.cursor > 0:
                            self.text = self.text[:self.cursor-1] + self.text[self.cursor:]
                            self.cursor -= 1
                    elif event.key == pygame.K_DELETE:
                        self.text = self.text[:self.cursor] + self.text[self.cursor+1:]
                    elif event.key == pygame.K_RETURN:
                        if function != None:
                            function()
                    elif event.key == pygame.K_LEFT:
                        if self.cursor > 0:
                            self.cursor -= 1
                    elif event.key == pygame.K_RIGHT:
                        if self.cursor < len(self.text):
                            self.cursor += 1
                    else:
                        if text_width < self.maxTextWidth:
                            self.text = self.text[:self.cursor] + event.unicode + self.text[self.cursor:]
                            self.cursor += 1
        

class Text(object):
    def __init__(self, text, x, y, height, baseFont, textSize=32):
        self.text = text
        self.x = x
        self.y = y
        self.baseFont = baseFont
        self.height = height
        self.textSize = textSize
        self.base_font = pygame.font.Font(self.baseFont, self.textSize)
    def draw(self, win):
        surface_area = self.base_font.render(self.text, 1, (0,0,0))
        win.blit(surface_area, (self.x - surface_area.get_width() / 2, self.y - surface_area.get_height() / 2))
    def update(self, win, newtext, color):
        self.text = newtext
        surface_area = self.base_font.render(self.text, 1, color)
        win.blit(surface_area, (self.x - surface_area.get_width() / 2, self.y - surface_area.get_height() / 2))

class Button():
    """A class for all buttons"""
    def __init__(self, color, color2, x, y, basefont, text_color=(0,0,0), text_color2=(0,0,0), width=None, height=None, text='',buttonType='Rectangle', radius=None, textSize=30, curve=20):
        """Sets the values for buttton"""
        self.color = color
        self.color2 = color2
        self.x = x - width/2
        self.y = y - height/2
        self.width = width
        self.height = height
        self.text = text
        self.buttonType = buttonType
        self.radius = radius
        self.textSize = textSize
        self.hover = False
        self.click = False
        self.curve = curve
        self.text_color = text_color
        self.text_color2 = text_color2
        self.basefont = basefont
        self.base_font = pygame.font.SysFont(self.basefont, self.textSize)
    def draw(self,win,outline=None,action=None, colorChange=True):
        """Draws the button. Variable for mouse detection"""
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.buttonType == "Rectangle":
            """If it is a rectangle it will draw it here"""
            if outline:
                """draws an outline"""
                pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0,self.curve)
            if self.x+self.width > mouse[0] > self.x and self.y+self.height > mouse[1] > self.y and colorChange:
                """Draws a lighter version of the image"""
                pygame.draw.rect(win, self.color2, (self.x,self.y,self.width,self.height),0,self.curve)

                if self.text != '':
                    """Text is blit here"""
                    text = self.base_font.render(self.text, 1, self.text_color2)
                    win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

                self.hover = True
                
                if click[0] == 1:
                    self.click = True
                    if action != None:
                        """If there is an action it is run"""
                        action()
                else:
                    """When mouse is not clicking"""
                    self.click = False
            else:
                self.hover = False
                """A darker version of image when the player isn't hovering over"""
                pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0, self.curve)
                if self.text != '':
                    """Text is blit here"""
                    text = self.base_font.render(self.text, 1, self.text_color)
                    win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))           

        if self.buttonType == "Circle":
            """If it is a circle it will draw it here"""
            if outline:
                """draws an outline"""
                pygame.draw.circle(win, outline, (self.x, self.y),self.radius+4,0)
            """Trig for area"""
            differenceInX = mouse[0] - self.x
            differenceInY = mouse[1] - self.y
            difference = ( differenceInX**2 + differenceInY**2 )**0.5
            """Print info on the circle"""
            ## print("\n" + "Circle X: " + str(self.x) + "\nCircle Y: " + str(self.y) + "\nMy X: " + str(mouse[0]) + "\nMy Y: " + str(mouse[1]) + "\nDifference in X: " + str(differenceInX)+ "\nDifference in Y: " + str(differenceInY) + "\nDifference: " + str(difference) + "\nRadius: " + str(self.radius) + "\n")
            if difference <= self.radius:
                """Draws a lighter version of the image"""
                pygame.draw.circle(win, self.color2, (self.x,self.y),self.radius,0)
      
                if click[0] == 1 and action != None:
                    """If there is an action it is run"""
                    action()
            else:
                """A darker version of image when the player isn't hovering over"""
                pygame.draw.circle(win, self.color, (self.x,self.y),self.radius,0)
             
            
            if self.text != '':
                """Text is blit here"""
                text = self.base_font.render(self.text, 1, (0,0,0))
                win.blit(text, (self.x - (text.get_width()/2), self.y - (text.get_height()/2)))
                
    def update(self, win ,newText,x_pos=None,y_pos=None):
        if x_pos == None:
            """If an x pos is given"""
            x_pos = self.x
        if y_pos == None:
            """If a y pos is given"""
            y_pos = self.y
        if newText != '':
            """Updates the text with the newText, the font and x and y. the old text is removed"""
            self.text = None
            text = self.base_font.render(newText, 1, (0,0,0))
            win.blit(text, (x_pos + (self.width/2 - text.get_width()/2), y_pos + (self.height/2 - text.get_height()/2)))
