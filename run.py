import pygame
from pygame import Color, Vector2
import pygame
from basketball import Ball, Ring
from letters import Textbox
from random import randint
import sys
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN
)

class Canvas():
    width = 1050
    height = 650
    score = 0

    def __init__(self):
        super(Canvas,self).__init__()

        pygame.init()
        screen = pygame.display.set_mode((Canvas.width, Canvas.height))
        pygame.display.set_caption('Shoot Ball')
        pygame.display.flip()

        clock = pygame.time.Clock()
        isRunning = True
        balls = []
        mousepos2 = Vector2()
        power = 30
        colorReps=0
        ring = Ring()
        
        def randomizeColor():
            return pygame.Color(randint(0,254),randint(0,254),randint(0,254),randint(100,200))
        
        randomColor = randomizeColor()

        while isRunning:
            screen.fill(Color('White'))
            Textbox(screen,Canvas.width//2,Canvas.height//3,str(Canvas.score),ring.color,Color('White'),150)
            Textbox(screen,Canvas.width//5,Canvas.height//15,'Press (w) to adjust shooting power',ring.color,Color('White'),40)
            Textbox(screen,Canvas.width//3.25,2*Canvas.height//15,'Mouse click to single attack OR Press (e) to splash attack',ring.color,Color('White'),40)
            Textbox(screen,Canvas.width//12.5,3*Canvas.height//15,'Power: '+str(int(power/30*10-1)),ring.color,Color('White'),40)
            
            ring.update(screen,Canvas.width, Canvas.height, Canvas.score)
            origin = pygame.draw.circle(screen, randomColor,(120,530),25,10)
            mousepos1 = pygame.mouse.get_pos()
            pygame.draw.line(screen, Color('Gray'),origin.center,mousepos1)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    
                elif event.type == MOUSEBUTTONDOWN:
                    mousepos2[:] = pygame.mouse.get_pos()            
                    ball = Ball(screen, mousepos2, power,randomColor)
                    balls.append(ball)
                    randomColor = randomizeColor()
                    
            key_pressed = pygame.key.get_pressed()

            #add power
            if key_pressed[pygame.K_w] and power<35:
                power += 1.25
            
            if key_pressed[pygame.K_e]:
                ball = Ball(screen, mousepos1, power,randomColor)
                colorReps +=1
                if colorReps>10:
                    colorReps=0
                    randomColor = randomizeColor()
                balls.append(ball)

            if power>5:
                power -= 1

            for i in balls:
                Canvas.score += i.update(screen, Canvas.width, Canvas.height-10, ring)

            pygame.display.flip()
            clock.tick(60)
canvas = Canvas() 
