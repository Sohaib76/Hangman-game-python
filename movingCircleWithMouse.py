import pygame,sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((640,400),0,32)

radius = 25
circle = pygame.Surface([radius*2]*2,SRCALPHA,32)
circle = circle.convert_alpha()
pygame.draw.circle(circle,(25,46,100),[radius]*2,radius)




backgroundColor = (255,255,255)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill(backgroundColor)
    screen.blit(circle,(pygame.mouse.get_pos()[0],100))
    
    pygame.display.update()
    pygame.time.delay(10)

