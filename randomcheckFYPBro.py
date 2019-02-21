import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False


font = pygame.font.SysFont("Arial", 66)
c=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#start_angle=0
#stop_angle=math.pi
#width=1

text = font.render("gold", True, (139,117,0))
text1 = font.render("yellow", True, (255,255,0))
text2 = font.render("blue", True, (0,128,255))
text3 = font.render("aliceBlue", True, (240, 248, 255))
text4 = font.render("orange", True, (255, 69, 0))
text5 = font.render("firebricks", True, (238, 44, 44))
text6 = font.render("white", True, (255, 255, 255))
text7 = font.render("skyblue", True, (135, 206, 235))
text8 = font.render("brown", True, (165, 42, 42))
text9 = font.render("green", True, (0, 128, 0))

is_blue = True
a=350
b=350
m=450
n=150
x =350
y =350
b1=450
n1=100
blue = (0, 128, 255)
aliceBlue = (240,248,255)
gold = (139,117,0)
green = (0,128,0)
firebricks=(238,44,44)
yellow=(255,255,0)
orange=(255,69,0)
white=(255,255,255)
brown=(165, 42, 42)
skyblue=(135,206,235)
c1=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
c=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

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

                pygame.draw.circle(screen,c1 , (m,b1), 120)
                screen.blit(text6,
        (100- text6.get_width() // 2, 150 - text6.get_height() // 2))

                pygame.draw.rect(screen,c, pygame.Rect(a, n1, 200, 200))
                screen.blit(text5,
        (170- text5.get_width() // 2, 450 - text5.get_height() // 2))
               
        
                
                #pygame.draw.ellipse(screen, red, (225, 10, 50, 20), 10) 

        elif pressed[pygame.K_UP]:
                screen.fill((0, 0, 0))
                #pygame.draw.ellipse(screen, orange, [350, 100, 700, 50])
                pygame.draw.polygon(screen, c1, [[350, 100], [350, 300],[550, 200]])
                #pygame.draw.polygon(screen, gold
                #pygame.draw.circle(screen, gold, (m,n), 105)
                screen.blit(text,
        (100- text.get_width() // 2, 150 - text.get_height() // 2))

                pygame.draw.rect(screen, c, pygame.Rect(x, y, 200, 200))
                screen.blit(text1,
        (170- text1.get_width() // 2, 450 - text1.get_height() // 2))

        elif pressed[pygame.K_a]:
                screen.fill((0, 0, 0))

                #pygame.draw.circle(screen, blue, (m,n), 105)
                pygame.draw.ellipse(screen, blue, [300, 100, 300, 150])
                #pygame.draw.arc(screen, orange, (450,150,300,150), 50, 50)
                screen.blit(text2,
        (100- text2.get_width() // 2, 150 - text2.get_height() // 2))

                pygame.draw.rect(screen, aliceBlue, pygame.Rect(x, y, 200, 200))
                screen.blit(text3,
        (170- text3.get_width() // 2, 450 - text3.get_height() // 2))

                     
        elif pressed[pygame.K_b]:
                screen.fill((0, 0, 0))
                #pygame.draw.polygon(screen, orange,True, [(350,150),(550,150),(250,250)])
                pygame.draw.circle(screen, orange, (m,n), 105)
                #pygame.draw.ellipse(screen, orange, [350, 100, 700, 50])
                screen.blit(text4,
        (100- text4.get_width() // 2, 150 - text4.get_height() // 2))

                pygame.draw.rect(screen, firebricks, pygame.Rect(x, y, 200, 200))
                screen.blit(text5,
        (170- text5.get_width() // 2, 450 - text5.get_height() // 2))


        elif pressed[pygame.K_c]:
                screen.fill((0, 0, 0))

                #pygame.draw.circle(screen, white,[[350, 400], [350, 300],[550, 400],[350,500]])
                #pygame.draw.arc(screen, white, (50,50,200,300), 20, 20)
                pygame.draw.circle(screen, blue, (m,n), 105)
                screen.blit(text6,
        (100- text6.get_width() // 2, 150 - text6.get_height() // 2))

                pygame.draw.polygon(screen, skyblue, [[450,350],[250,350],[550,550],[450,550]])
                screen.blit(text7,
        (170- text7.get_width() // 2, 450 - text7.get_height() // 2))

                
        elif pressed[pygame.K_d]:
                screen.fill((0, 0, 0))
                #pygame.draw.ellipse(screen, blue, [300, 100, 300, 150])
                pygame.draw.circle(screen, brown, (m,n), 105)
                screen.blit(text8,
        (100- text8.get_width() // 2, 150 - text8.get_height() // 2))

                #pygame.draw.rect(screen, orange, 400,600,300,500)
                pygame.draw.ellipse(screen, blue, [300, 100, 300, 150])
                screen.blit(text4,
        (170- text4.get_width() // 2, 450 - text4.get_height() // 2))

     
        #elif pressed[pygame.K_e]:
                screen.fill((0, 0, 0))

                pygame.draw.circle(screen, orange, (m,n), 105)
                screen.blit(text4,
        (100- text4.get_width() // 2, 150 - text4.get_height() // 2))

                pygame.draw.rect(screen, white, pygame.Rect(x, y, 200, 200))
                screen.blit(text6,
        (170- text6.get_width() // 2, 450 - text6.get_height() // 2))

                
        #elif pressed[pygame.K_f]:
                screen.fill((0, 0, 0))

                pygame.draw.circle(screen, white, (m,n), 105)
                screen.blit(text6,
        (100- text6.get_width() // 2, 150 - text6.get_height() // 2))

                pygame.draw.rect(screen, green, pygame.Rect(x, y, 200, 200))
                screen.blit(text9,
        (170- text9.get_width() // 2, 450 - text9.get_height() // 2))

                
     
        #elif pressed[pygame.K_g]:
                screen.fill((0, 0, 0))

                pygame.draw.circle(screen, blue, (m,n), 105)
                screen.blit(text2,
        (100- text2.get_width() // 2, 150 - text2.get_height() // 2))
        
                pygame.draw.rect(screen, green, pygame.Rect(x, y, 200, 200))
                screen.blit(text9,
        (170- text9.get_width() // 2, 450 - text9.get_height() // 2))

                
        if pressed[pygame.K_o]:
                screen.fill((0, 0, 0))
        
        
        
        pygame.display.flip()
        clock.tick(60)
