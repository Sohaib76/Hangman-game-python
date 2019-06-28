import pygame, sys, random
from random import randint
from time import sleep
import time
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.


#screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 80
y = 40
blue = (0, 128, 255)
aliceBlue = (240,248,255)

gold = (255,215,0)
green = (0,128,0)
red = (255, 0, 0)
pink = (238, 130, 238)
purple = (106, 90, 205)
orange = (255, 165, 0)
color_disp = ['blue' ,'aliceBlue',"gold","green","red","pink","purple",'orange']
color_name = [blue ,aliceBlue,gold,green,red,pink,purple,orange]
font = pygame.font.SysFont("Arial", 66)
text1 = font.render("gold", True, (139,117,0))

#clock = pygame.time.Clock()

#--------------function------------For Circle And Square
def draw_circle_and_square(screen, delay, colorCr , txtCr, txtcolorCr, colorSq, txtSq, txtcolorSq ,x, y):
#def draw_rhombus_and_parallelogram(screen, delay, colorRb, txtRb,txtcolorRb ,colorPl, txtPl, txtcolorPl, x, y):

    

    circle = pygame.Surface((100, 100))                    #circle = pygame.Surface((2*50, 2*50))
    rect = circle.get_rect()
    rect.center = screen.get_rect().center
    pygame.draw.circle(circle, colorCr, (x,y), 40)


    
    square = pygame.Surface((200, 200))
    rect = square.get_rect()
    rect.center = screen.get_rect().center
    pygame.draw.rect(square, colorSq, pygame.Rect(x-40, y+80, 100, 100))          #pygame.draw.rect(square, color2, pygame.Rect(x+60, y+60, 100, 100))


    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurfaceCr = myfont.render(txtCr, False, txtcolorCr)
    
    
    textsurfaceSq = myfont.render(txtSq, False, txtcolorSq)
    
    
    screen.fill((0, 0, 0))
    screen.blit(textsurfaceSq,(x-20,y+300))
    screen.blit(textsurfaceCr,(x-20,y+200))
    screen.blit(square,rect)
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







#..................Function For Rhombus And Parallelogram........#
def draw_rhombus_and_parallelogram(screen, delay, colorRb, txtRb,txtcolorRb ,colorPl, txtPl, txtcolorPl, x, y):

    

    square = pygame.Surface((500, 500))
    rect = square.get_rect()
    rect.center = screen.get_rect().center


    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurfaceRb = myfont.render(txtRb, False, txtcolorRb)
    textsurfacePl = myfont.render(txtPl, False, txtcolorPl)
    
    pygame.draw.lines(square, colorRb, False, [(100+100,100), (150+100,0), (200+100,100)], 1)
    pygame.draw.lines(square, colorRb, False, [(100+100,100), (150+100,200), (200+100,100)], 1)

    #paralle = pygame.Surface((500, 500))
   # rect = paralle.get_rect()
    #rect.center = screen.get_rect().center

    pygame.draw.lines(square, colorPl, True, [(100+100,100+150), (400+100,100+150), (300+100,200+150),(0+100,200+150)], 1)
    
    screen.fill((0, 0, 0))

    #screen.blit(paralle, rect)
    screen.blit(textsurfaceRb,(x-20,y+100))
    screen.blit(textsurfacePl,(x-20,y+300))
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

















#............................








def draw_square(screen, delay, color , x, y):

    

    square = pygame.Surface((200, 200))
    rect = square.get_rect()
    rect.center = screen.get_rect().center
    pygame.draw.rect(square, color, pygame.Rect(x+60, y+60, 100, 100))
    
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
   
    
    
'''
for i in range(3):

    draw_rhombus_and_parallelogram(screen, 2000, blue, "blue" , blue, gold,  "gold", gold,x, y)
    draw_circle_and_square(screen, 3000, gold , "gold" , gold, green, "green",  green,  x, y)
    draw_circle_and_square(screen, 2000, green ,"green", green , gold, "gold", gold, x, y)
    draw_rhombus_and_parallelogram(screen, 2000, red, "red" , red, gold,  "gold", gold,x, y)
    draw_circle_and_square(screen, 2000, green ,"green", green , aliceBlue, "white", aliceBlue, x, y)
    draw_rhombus_and_parallelogram(screen, 2000, pink, "pink" , pink, purple,  "purple", purple
                                   ,x, y)
    # draw_square(screen, 2000, blue, x, y)
  #  draw_square(screen, 2000, aliceBlue,  x, y)
'''
score =  0
        
pressed = pygame.key.get_pressed()

for i in range(3):
    t1 = time.time()
    min_rand = randint(0,3)
    max_rand = randint(4,7)
    rd1_s_c  = randint(min_rand,max_rand)    #shape color
    rd1_s_t  = randint(min_rand,max_rand)    #shape text 
    rd1_s_tc = randint(min_rand,max_rand)    #shape text color
    rd2_s_c  = randint(min_rand,max_rand)    #shape color
    rd2_s_t  = randint(min_rand,max_rand)    #shape text 
    rd2_s_tc = randint(min_rand,max_rand)    #shape text color
    draw_rhombus_and_parallelogram  (screen, 100, color_name[rd1_s_c],color_disp[rd1_s_t], color_name[rd1_s_tc], color_name[rd2_s_c], color_disp[rd2_s_t], color_name[rd2_s_tc],x, y)
    print(rd1_s_c,rd1_s_t,rd1_s_tc)
    print(rd2_s_c,rd2_s_t,rd2_s_tc)
    a = input("Enter 1 (True) or 2(False)")
    if(a == '1'):
          if(rd1_s_c == rd1_s_t==rd1_s_tc or rd2_s_c == rd2_s_t==rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c != rd2_s_t==rd2_s_tc or rd2_s_c == rd1_s_t==rd1_s_tc):
                score = score + 1
                print(score)
    elif(a == '2'):
          if(rd1_s_c != rd1_s_t!=rd1_s_tc or rd2_s_c != rd2_s_t!=rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c != rd2_s_t!=rd2_s_tc or rd2_s_c != rd1_s_t!=rd1_s_tc):
                score = score + 1
                print(score)
    t2 = time.time()
    T = t2 - t1
    print("Time = ",T,'sec')
    min_rand = randint(0,3)

    max_rand = randint(4,7)
    rd1_s_c  = randint(min_rand,max_rand)    #shape color
    rd1_s_t  = randint(min_rand,max_rand)    #shape text 
    rd1_s_tc = randint(min_rand,max_rand)    #shape text color
    rd2_s_c  = randint(min_rand,max_rand)    #shape color
    rd2_s_t  = randint(min_rand,max_rand)    #shape text 
    rd2_s_tc = randint(min_rand,max_rand)    #shape text color
    draw_circle_and_square          (screen, 100, color_name[rd1_s_c],color_disp[rd1_s_t], color_name[rd1_s_tc], color_name[rd2_s_c], color_disp[rd2_s_t], color_name[rd2_s_tc],x, y)
    print(rd1_s_c,rd1_s_t,rd1_s_tc)
    print(rd2_s_c,rd2_s_t,rd2_s_tc)
    a = input("Enter 1 (True) or 2(False)")
    if(a == '1'):
          if(rd1_s_c == rd1_s_t==rd1_s_tc or rd2_s_c == rd2_s_t==rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c == rd2_s_t==rd2_s_tc or rd2_s_c == rd1_s_t==rd1_s_tc):
                score = score + 1
                print(score)
    elif(a == '2'):
          if(rd1_s_c != rd1_s_t!=rd1_s_tc or rd2_s_c != rd2_s_t!=rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c != rd2_s_t!=rd2_s_tc or rd2_s_c != rd1_s_t!=rd1_s_tc):
                score = score + 1
                print(score)
    t3 = time.time()
    T = t3 - t2
    print("Time = ",T,'sec')

    min_rand = randint(0,3)
    max_rand = randint(4,7)
    rd1_s_c  = randint(min_rand,max_rand)    #shape color
    rd1_s_t  = randint(min_rand,max_rand)    #shape text 
    rd1_s_tc = randint(min_rand,max_rand)    #shape text color
    rd2_s_c  = randint(min_rand,max_rand)    #shape color
    rd2_s_t  = randint(min_rand,max_rand)    #shape text 
    rd2_s_tc = randint(min_rand,max_rand)    #shape text color
    draw_circle_and_square          (screen, 100, color_name[rd1_s_c],color_disp[rd1_s_t], color_name[rd1_s_tc], color_name[rd2_s_c], color_disp[rd2_s_t], color_name[rd2_s_tc],x, y)
    print(rd1_s_c,rd1_s_t,rd1_s_tc)
    print(rd2_s_c,rd2_s_t,rd2_s_tc)
    a = input("Enter 1 (True) or 2(False)")
    if(a == '1'):
          if(rd1_s_c == rd1_s_t==rd1_s_tc or rd2_s_c == rd2_s_t==rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c == rd2_s_t==rd2_s_tc or rd2_s_c == rd1_s_t==rd1_s_tc):
                score = score + 1
                print(score)
    elif(a == '2'):
          if(rd1_s_c != rd1_s_t!=rd1_s_tc or rd2_s_c != rd2_s_t!=rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c != rd2_s_t!=rd2_s_tc or rd2_s_c != rd1_s_t!=rd1_s_tc):
                score = score + 1
                print(score)

    t4 = time.time()
    T = t4 - t3
    print("Time = ",T,'sec')
    min_rand = randint(0,3)
    max_rand = randint(4,7)
    rd1_s_c  = randint(min_rand,max_rand)    #shape color
    rd1_s_t  = randint(min_rand,max_rand)    #shape text 
    rd1_s_tc = randint(min_rand,max_rand)    #shape text color
    rd2_s_c  = randint(min_rand,max_rand)    #shape color
    rd2_s_t  = randint(min_rand,max_rand)    #shape text 
    rd2_s_tc = randint(min_rand,max_rand)    #shape text color
    draw_rhombus_and_parallelogram  (screen, 100, color_name[rd1_s_c],color_disp[rd1_s_t], color_name[rd1_s_tc], color_name[rd2_s_c], color_disp[rd2_s_t], color_name[rd2_s_tc],x, y)
    print(rd1_s_c,rd1_s_t,rd1_s_tc)
    print(rd2_s_c,rd2_s_t,rd2_s_tc)
    a = input("Enter 1 (True) or 2(False)")
    if(a == '1'):
          if(rd1_s_c == rd1_s_t==rd1_s_tc or rd2_s_c == rd2_s_t==rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c == rd2_s_t==rd2_s_tc or rd2_s_c == rd1_s_t==rd1_s_tc):
                score = score + 1
                print(score)

    elif(a == '2'):
          if(rd1_s_c != rd1_s_t!=rd1_s_tc or rd2_s_c != rd2_s_t!=rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c != rd2_s_t!=rd2_s_tc or rd2_s_c != rd1_s_t!=rd1_s_tc):
                score = score + 1
                print(score)
    t5 = time.time()
    T = t5 - t4
    print("Time = ",T,'sec')
    min_rand = randint(0,3)
    max_rand = randint(4,7)
    rd1_s_c  = randint(min_rand,max_rand)    #shape color
    rd1_s_t  = randint(min_rand,max_rand)    #shape text 
    rd1_s_tc = randint(min_rand,max_rand)    #shape text color
    rd2_s_c  = randint(min_rand,max_rand)    #shape color
    rd2_s_t  = randint(min_rand,max_rand)    #shape text 
    rd2_s_tc = randint(min_rand,max_rand)    #shape text color
    draw_circle_and_square          (screen, 100, color_name[rd1_s_c],color_disp[rd1_s_t], color_name[rd1_s_tc], color_name[rd2_s_c], color_disp[rd2_s_t], color_name[rd2_s_tc],x, y)
    print(rd1_s_c,rd1_s_t,rd1_s_tc)
    print(rd2_s_c,rd2_s_t,rd2_s_tc)
    a = input("Enter 1 (True) or 2(False)")
    if(a == '1'):
          if(rd1_s_c == rd1_s_t==rd1_s_tc or rd2_s_c == rd2_s_t==rd1_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c == rd2_s_t==rd1_s_tc or rd2_s_c == rd1_s_t==rd1_s_tc):
                score = score + 1
                print(score)
    elif(a == '2'):
          if(rd1_s_c != rd1_s_t!=rd1_s_tc or rd2_s_c != rd2_s_t!=rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c != rd2_s_t!=rd2_s_tc or rd2_s_c != rd1_s_t!=rd1_s_tc):
                score = score + 1
                print(score)
    t6 = time.time()
    T = t6 - t5
    print("Time = ",T,'sec')
    min_rand = randint(0,3)
    max_rand = randint(4,7)
    rd1_s_c  = randint(min_rand,max_rand)    #shape color
    rd1_s_t  = randint(min_rand,max_rand)    #shape text 
    rd1_s_tc = randint(min_rand,max_rand)    #shape text color
    rd2_s_c  = randint(min_rand,max_rand)    #shape color
    rd2_s_t  = randint(min_rand,max_rand)    #shape text 
    rd2_s_tc = randint(min_rand,max_rand)    #shape text color
    draw_rhombus_and_parallelogram  (screen, 100, color_name[rd1_s_c],color_disp[rd1_s_t], color_name[rd1_s_tc], color_name[rd2_s_c], color_disp[rd2_s_t], color_name[rd2_s_tc],x, y)                                  
    print(rd1_s_c,rd1_s_t,rd1_s_tc)
    print(rd2_s_c,rd2_s_t,rd2_s_tc)
    a = input("Enter 1 (True) or 2(False)")
    if(a == '1'):
          if(rd1_s_c == rd1_s_t==rd1_s_tc or rd2_s_c == rd2_s_t==rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c == rd2_s_t==rd2_s_tc or rd2_s_c == rd1_s_t==rd1_s_tc):
                score = score + 1
                print(score)
    elif(a == '2'):
          if(rd1_s_c != rd1_s_t!=rd1_s_tc or rd2_s_c != rd2_s_t!=rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c != rd2_s_t!=rd2_s_tc or rd2_s_c != rd1_s_t!=rd1_s_tc):
                score = score + 1
                print(score)
    t7 = time.time()
    T = t7 - t6
    print("Time = ",T,'sec')
#draw_circle(screen, 3000, gold, x, y)
#draw_square(screen, 2000, blue, x, y)
#draw_circle(screen, 2000, green, x, y)


print("Your score is = ",score)
pygame.quit()
    #pygame.time.wait(5000)
    #screen.fill((0, 0, 0))
    #pygame.display.flip()
   # clock.tick(60)

