import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 60
y = 50
blue = (0, 128, 255)
aliceBlue = (240,248,255)
gold = (255,215,0)
green = (0,128,0)

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
    
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        #screen.fill((0, 0, 0))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
       # pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

        if pressed[pygame.K_DOWN]:
                screen.fill((0, 0, 0))
                pygame.draw.rect(screen, color, pygame.Rect(x, y, 100, 80))
        elif pressed[pygame.K_UP]:
                screen.fill((0, 0, 0))
                pygame.draw.rect(screen, green, pygame.Rect(x, y, 60, 60))
        elif pressed[pygame.K_a]:
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, gold, (x,y), 40)
        elif pressed[pygame.K_s]:
                screen.fill((0, 0, 0))
                pygame.draw.polygon(screen, aliceBlue, ((30,80),(80,20),(150,80)))
        if pressed[pygame.K_RETURN]:
                screen.fill((0, 0, 0))
        
        
        
        pygame.display.flip()
        clock.tick(60)
