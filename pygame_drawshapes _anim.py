import pygame, sys, random


#screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 60
y = 50
blue = (0, 128, 255)
aliceBlue = (240,248,255)
gold = (255,215,0)
green = (0,128,0)

#clock = pygame.time.Clock()

#--------------function------------
def draw_circle(screen, delay, color , x, y):

    

    circle = pygame.Surface((2*50, 2*50))
    rect = circle.get_rect()
    rect.center = screen.get_rect().center
    pygame.draw.circle(circle, color, (x,y), 40)
    
    screen.fill((0, 0, 0))
    screen.blit(circle,rect)
    pygame.display.flip()
    
    
    
    
    #blit wlit
    
    current_time = pygame.time.get_ticks()
    exit_time = current_time + delay
    clock = pygame.time.Clock()

    done = False

    while not done:
    


    
    #Quit event etc
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                done= True
                
        current_time = pygame.time.get_ticks()

        if current_time >= exit_time:
            done = True

        clock.tick(5)




def draw_square(screen, delay, color , x, y):

    

    square = pygame.Surface((200, 200))
    rect = square.get_rect()
    rect.center = screen.get_rect().center
    pygame.draw.rect(square, color, pygame.Rect(x, y, 100, 100))
    
    screen.fill((0, 0, 0))
    screen.blit(square,rect)
    pygame.display.flip()
    
    
    
    
    #blit wlit
    
    current_time = pygame.time.get_ticks()
    exit_time = current_time + delay
    clock = pygame.time.Clock()

    done = False

    while not done:
    


    
    #Quit event etc
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                done= True
                
        current_time = pygame.time.get_ticks()

        if current_time >= exit_time:
            done = True

        clock.tick(5)












#----------program----------







   # pygame.draw.circle(screen, gold, (x,y), 40)
     
   # pygame.draw.rect(screen, aliceBlue, pygame.Rect(x, y, 100, 80))
pygame.init()

screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()

for i in range(3):
    draw_circle(screen, 3000, gold, x, y)
    draw_square(screen, 2000, blue, x, y)
    draw_circle(screen, 2000, green, x, y)
    draw_square(screen, 2000, aliceBlue, x, y)


#draw_circle(screen, 3000, gold, x, y)
#draw_square(screen, 2000, blue, x, y)

#draw_circle(screen, 2000, green, x, y)




pygame.quit()
    #pygame.time.wait(5000)
    #screen.fill((0, 0, 0))
    #pygame.display.flip()
   # clock.tick(60)

