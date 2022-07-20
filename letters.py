from pygame.sprite import Sprite
from pygame import Color
import pygame

class Letters(Sprite):
    def __init__(self,screen,character,col,row,origin_x, origin_y, color):
        self.color = color
        # basic font for user typed
        self.text_size = 80
        base_font = pygame.font.Font(None, self.text_size-10)
        self.text = base_font.render(character, True, (254,254,254))

        # create rectangle
        self.text_rect = self.text.get_rect(center=(origin_x + row*self.text_size,origin_y +col*self.text_size))
        # set the center of the rectangular object.
        pygame.draw.circle(screen, self.color, self.text_rect.center, self.text_size//2-5)
        # draw text
        screen.blit(self.text, self.text_rect)

        super(Letters,self).__init__()

    def select(self,screen):
        self.color = Color('DarkSlateGray')
        pygame.draw.circle(screen, self.color, self.text_rect.center, self.text_size//2-5)
        screen.blit(self.text, self.text_rect)
        super(Letters,self).__init__()

class Lists(Sprite):
    def __init__(self):
        super(Lists,self).__init__()
        self.all_letters = []

    def append_to_list(self, obj):
        self.all_letters.append(obj)
    
    def create_word(self,screen,origin_x,origin_y,word,bgcolor):
        for i in range(0,len(word)):    
            obj = Letters(screen, word[i], 0, i, origin_x, origin_y, bgcolor)
            self.append_to_list(obj)
    
    def update(self,screen,origin_x,origin_y,letter,index):
        obj = Letters(screen, letter, 0, index, origin_x, origin_y, Color('LimeGreen'))
        self.all_letters[index] = obj

class Textbox:
    def __init__(self, screen, originx, originy, strtext,fgcolor, bgcolor, text_size):
        self.strtext = strtext
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.originx = originx
        self.originy = originy
        # basic font for user typed
        self.text_size = text_size
        self.base_font = pygame.font.Font(None, self.text_size-10)
        self.text = self.base_font.render(strtext, True, self.fgcolor)

        # create rectangle
        self.text_rect = self.text.get_rect(center=(originx,originy))
        # set the center of the rectangular object.
        pygame.draw.rect(screen, self.bgcolor, self.text_rect)
        # draw text
        screen.blit(self.text, self.text_rect)
        super(Textbox,self).__init__()        
    
    def updateText(self, screen, user_text):
        self.strtext = user_text
        self.base_font = pygame.font.Font(None, self.text_size-10)
        self.text = self.base_font.render(user_text, True, self.fgcolor)
        # create rectangle
        self.text_rect = self.text.get_rect(center=(self.originx,self.originy))
        # set the center of the rectangular object.
        pygame.draw.rect(screen, self.bgcolor, self.text_rect)
        # draw text
        screen.blit(self.text, self.text_rect)
        
         