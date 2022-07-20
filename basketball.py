import pygame
from pygame import Color, Vector2, Rect
from random import randint
class Ring():
    def __init__(self):
        super(Ring,self).__init__()
        self.speed = Vector2(1,0)
        self.size = Vector2(100,40)
        self.pos = Vector2(850, 330)
        self.color = Color('Black')
        nullRect = Rect(0,0,0,0)
        self.ellipserect, self.leftrect, self.rightrect, self.centerrect = nullRect,nullRect,nullRect,nullRect
    
    def update(self,screen,width,height,score):
        if self.ellipserect.right > width or self.ellipserect.left < 300:
            self.speed.x = -self.speed.x

        self.pos.x += self.speed.x

        self.ellipserect = pygame.Rect(self.pos.x,self.pos.y,self.size.x,self.size.y)
        self.leftrect = pygame.Rect(self.pos.x, self.pos.y+10, self.size.x*0.10, 30)
        self.rightrect = pygame.Rect(self.pos.x+self.size.x*0.90, self.pos.y+10, self.size.x*0.10, 30)
        self.centerrect = pygame.Rect(self.pos.x+self.size.x*0.25, self.pos.y+30, self.size.x*0.50, 10)

        pygame.draw.ellipse(screen, self.color, self.ellipserect, 10)
        
class Ball():
    def __init__(self,screen,mousepos,power, color):
        super(Ball,self).__init__()
        self.radius = randint(5,20)
        self.isShooted = False
        self.color = color
        self.pos = Vector2(120, 530)
        self.speed = (mousepos-self.pos).normalize()*power
        self.rect = Rect(self.pos.x,self.pos.y,self.radius*2,self.radius*2)
    
        pygame.draw.circle(screen, self.color, (self.pos.x,self.pos.y), self.radius)

    def update(self, screen, width, height, ring):
        #limit horizontally
        if self.pos.x < 0 or self.pos.x > width:
            self.speed.x = -self.speed.x
        
        #limit vertically
        if self.pos.y < 0:
            self.speed.y = -self.speed.y
        
        #bounce ring
        if self.rect.colliderect(ring.leftrect) or self.rect.colliderect(ring.rightrect):
            self.speed.x = - self.speed.x

        #gravity
        if self.pos.y < height:
            self.pos.x += self.speed.x
            self.speed.y += 1
        else:
        #bounce
            self.speed.y = -self.speed.y * 0.75
            
        self.pos.y += self.speed.y 

        #update rect and draw
        self.rect = Rect(self.pos.x,self.pos.y,self.radius*2,self.radius*2)
        pygame.draw.circle(screen, self.color, (self.pos.x,self.pos.y), self.radius)

        #shoots
        if (not self.isShooted) and self.rect.colliderect(ring.centerrect):
            #ring.speed += ring.speed.normalize()
            self.isShooted = True
            ring.color = self.color
            return 1
        return 0
        