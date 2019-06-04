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
Blue = (0, 128, 255)
Yellow= (255,255,0)

Brown = (139,69,0)
Green = (0,128,0)
Red = (255, 0, 0)
Pink = (238, 130, 238)
Purple = (106, 90, 205)
Orange = (255, 165, 0)
color_disp = ['Blue' ,'Yellow',"Brown","Green","Red","Pink","Purple",'Orange']
color_name = [Blue ,Yellow,Brown,Green,Red,Pink,Purple,Orange]
font = pygame.font.SysFont("ALGERIAN", 96)
text1 = font.render("Brown", True, (139,117,0))

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


    myfont = pygame.font.SysFont('ALGERIAN', 48)
    textsurfaceCr = myfont.render(txtCr, False, txtcolorCr)
    
    
    textsurfaceSq = myfont.render(txtSq, False, txtcolorSq)
    
    
    screen.fill((0, 0, 0))
    screen.blit(textsurfaceSq,(10,y+300))
    screen.blit(textsurfaceCr,(10,y+200))
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


    myfont = pygame.font.SysFont('ALGERIAN', 48)
    textsurfaceRb = myfont.render(txtRb, False, txtcolorRb)
    textsurfacePl = myfont.render(txtPl, False, txtcolorPl)
    
    pygame.draw.lines(square, colorRb, False, [(100+100,100), (150+100,0), (200+100,100)], 7)
    pygame.draw.lines(square, colorRb, False, [(100+100,100), (150+100,200), (200+100,100)], 7)

    #paralle = pygame.Surface((500, 500))
   # rect = paralle.get_rect()
    #rect.center = screen.get_rect().center

    pygame.draw.lines(square, colorPl, True, [(100+100,100+150), (400+100,100+150), (300+100,200+150),(0+100,200+150)], 7)
    
    screen.fill((0, 0, 0))

    #screen.blit(paralle, rect)
    screen.blit(textsurfaceRb,(10,y+300))
    screen.blit(textsurfacePl,(10,y+200))
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

font = pygame.font.Font('freesansbold.ttf', 32)
text_true = font.render('True', True, (0,0,0))
text_false = font.render('False', True, (0,0,0))
textRectt = text_true.get_rect()
textRectt.center = ((150+(100/2)), (450+(50/2)))

textRectf = text_false.get_rect()
textRectf.center = ((550+(100/2)), (450+(50/2)))


score = 0
count_true = 0
count_false = 0

for i in range(3):


    t1 = time.time()
    min_rand = randint(0,3)
    max_rand = randint(4,7)
    rd1_s_c  = randint(min_rand,max_rand)    #shape color
    rd1_s_t  = randint(min_rand,max_rand)    #shape text
    rd1_s_tc = rd1_s_t
    #rd1_s_tc = randint(min_rand,max_rand)    #shape text color
    rd2_s_c  = randint(min_rand,max_rand)    #shape color
    rd2_s_t  = randint(min_rand,max_rand)    #shape text 
    rd2_s_tc = rd2_s_t    #shape text color
    draw_rhombus_and_parallelogram  (screen, 100, color_name[rd1_s_c],color_disp[rd1_s_t], color_name[rd1_s_tc], color_name[rd2_s_c], color_disp[rd2_s_t], color_name[rd2_s_tc],x, y)
    #print(rd1_s_c,rd1_s_t,rd1_s_tc)
    #print(rd2_s_c,rd2_s_t,rd2_s_tc)


    pygame.draw.rect(screen, (0,255,0), (150,450,100,50))
    pygame.draw.rect(screen, (255,0,0), (550,450,100,50))
    screen.blit(text_true, textRectt)
    screen.blit(text_false, textRectf)
    text_score = font.render(str(score), 1, (255,255,0))
    textRects = text_true.get_rect()
    textRects.center = ((700+(100/2)), (50+(50/2)))
    screen.blit(text_score, textRects) 
    pygame.display.update()
    a = 0
   # score = 0
    #count_true = 0
    #count_false = 0
    '''smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects("GO!", smallText)
    textRect.center = ( (150+(100/2)), (450+(50/2)) )
    gameDisplay.blit(textSurf, textRect)'''

    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
                        a = '1'
                        #print("1")
                        break
                    elif 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
                        a = '2'
                        #print("2")
                        break
        if ( a=='1' or a == '2'):
            break
    
    #a = input("Enter 1 (True) or 2(False)")
        '''
    if(a == '1'):
          if(rd1_s_c == rd1_s_t==rd1_s_tc or rd2_s_c == rd2_s_t==rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c == rd2_s_t==rd2_s_tc or rd2_s_c == rd1_s_t==rd1_s_tc):
                score = score + 1
                print(score)

          count_true = count_true+1
          print('count:',count_true)
    elif(a == '2'):
          if(rd1_s_c != rd1_s_t!=rd1_s_tc or rd2_s_c != rd2_s_t!=rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c != rd2_s_t!=rd2_s_tc or rd2_s_c != rd1_s_t!=rd1_s_tc):
                score = score + 1
                print(score)

          count_false = count_false+1
          print('count:',count_false)'''
    
    if(a == '1'):
          if(rd1_s_c == rd1_s_t==rd1_s_tc or rd2_s_c == rd2_s_t==rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c == rd2_s_t==rd2_s_tc or rd2_s_c == rd1_s_t==rd1_s_tc):
                score = score + 1
                print(score)
          count_true = count_true+1
          print('count:',count_true)

    elif(a == '2'):
          if(rd1_s_c != rd1_s_t!=rd1_s_tc or rd2_s_c != rd2_s_t!=rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c != rd2_s_t!=rd2_s_tc or rd2_s_c != rd1_s_t!=rd1_s_tc):
                score = score + 1
                print(score)
          count_false = count_false+1
          print('count:',count_false)

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

    pygame.draw.rect(screen, (0,255,0), (150,450,100,50))
    pygame.draw.rect(screen, (255,0,0), (550,450,100,50))
    screen.blit(text_true, textRectt)
    screen.blit(text_false, textRectf)
    text_score = font.render(str(score), 1, (255,255,0))
    textRects = text_true.get_rect()
    textRects.center = ((700+(100/2)), (50+(50/2)))
    screen.blit(text_score, textRects) 
    pygame.display.update()
    a = 0
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
                        a = '1'
                        #print("1")
                        break
                    elif 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
                        a = '2'
                        #print("2")
                        break
        if ( a=='1' or a == '2'):
            break
    if(a == '1'):
          if(rd1_s_c == rd1_s_t==rd1_s_tc or rd2_s_c == rd2_s_t==rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c == rd2_s_t==rd2_s_tc or rd2_s_c == rd1_s_t==rd1_s_tc):
                score = score + 1
                print(score)
          count_true = count_true+1
          print('count:',count_true)

    elif(a == '2'):
          if(rd1_s_c != rd1_s_t!=rd1_s_tc or rd2_s_c != rd2_s_t!=rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c != rd2_s_t!=rd2_s_tc or rd2_s_c != rd1_s_t!=rd1_s_tc):
                score = score + 1
                print(score)
          count_false = count_false+1
          print('count:',count_false)

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
    #print(rd1_s_c,rd1_s_t,rd1_s_tc)
    #print(rd2_s_c,rd2_s_t,rd2_s_tc)
    pygame.draw.rect(screen, (0,255,0), (150,450,100,50))
    pygame.draw.rect(screen, (255,0,0), (550,450,100,50))
    screen.blit(text_true, textRectt)
    screen.blit(text_false, textRectf)
    text_score = font.render(str(score), 1, (255,255,0))
    textRects = text_true.get_rect()
    textRects.center = ((700+(100/2)), (50+(50/2)))
    screen.blit(text_score, textRects) 
    pygame.display.update()
    a = 0
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
                        a = '1'
                        #print("1")
                        break
                    elif 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
                        a = '2'
                        #print("2")
                        break
        if ( a=='1' or a == '2'):
            break
    if(a == '1'):
          if(rd1_s_c == rd1_s_t==rd1_s_tc or rd2_s_c == rd2_s_t==rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c == rd2_s_t==rd2_s_tc or rd2_s_c == rd1_s_t==rd1_s_tc):
                score = score + 1
                print(score)
          count_true = count_true+1
          print('count:',count_true)

    elif(a == '2'):
          if(rd1_s_c != rd1_s_t!=rd1_s_tc or rd2_s_c != rd2_s_t!=rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c != rd2_s_t!=rd2_s_tc or rd2_s_c != rd1_s_t!=rd1_s_tc):
                score = score + 1
                print(score)
          count_false = count_false+1
          print('count:',count_false)


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
    #print(rd1_s_c,rd1_s_t,rd1_s_tc)
    #print(rd2_s_c,rd2_s_t,rd2_s_tc)
    pygame.draw.rect(screen, (0,255,0), (150,450,100,50))
    pygame.draw.rect(screen, (255,0,0), (550,450,100,50))
    screen.blit(text_true, textRectt)
    screen.blit(text_false, textRectf)
    text_score = font.render(str(score), 1, (255,255,0))
    textRects = text_true.get_rect()
    textRects.center = ((700+(100/2)), (50+(50/2)))
    screen.blit(text_score, textRects) 
    pygame.display.update()
    a = 0
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
                        a = '1'
                        #print("1")
                        break
                    elif 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
                        a = '2'
                        #print("2")
                        break
        if ( a=='1' or a == '2'):
            break
    if(a == '1'):
          if(rd1_s_c == rd1_s_t==rd1_s_tc or rd2_s_c == rd2_s_t==rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c == rd2_s_t==rd2_s_tc or rd2_s_c == rd1_s_t==rd1_s_tc):
                score = score + 1
                print(score)
          count_true = count_true+1
          print('count:',count_true)


    elif(a == '2'):
          if(rd1_s_c != rd1_s_t!=rd1_s_tc or rd2_s_c != rd2_s_t!=rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c != rd2_s_t!=rd2_s_tc or rd2_s_c != rd1_s_t!=rd1_s_tc):
                score = score + 1
                print(score)
          count_false = count_false+1
          print('count:',count_false)

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
    #print(rd1_s_c,rd1_s_t,rd1_s_tc)
    #print(rd2_s_c,rd2_s_t,rd2_s_tc)
    pygame.draw.rect(screen, (0,255,0), (150,450,100,50))
    pygame.draw.rect(screen, (255,0,0), (550,450,100,50))
    screen.blit(text_true, textRectt)
    screen.blit(text_false, textRectf)
    text_score = font.render(str(score), 1, (255,255,0))
    textRects = text_true.get_rect()
    textRects.center = ((700+(100/2)), (50+(50/2)))
    screen.blit(text_score, textRects) 
    pygame.display.update()
    a = 0
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
                        a = '1'
                        #print("1")
                        break
                    elif 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
                        a = '2'
                        #print("2")
                        break
        if ( a=='1' or a == '2'):
            break
    if(a == '1'):
          if(rd1_s_c == rd1_s_t==rd1_s_tc or rd2_s_c == rd2_s_t==rd1_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c == rd2_s_t==rd1_s_tc or rd2_s_c == rd1_s_t==rd1_s_tc):
                score = score + 1
                print(score)
          count_true = count_true+1
          print('count:',count_true)

    elif(a == '2'):
          if(rd1_s_c != rd1_s_t!=rd1_s_tc or rd2_s_c != rd2_s_t!=rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c != rd2_s_t!=rd2_s_tc or rd2_s_c != rd1_s_t!=rd1_s_tc):
                score = score + 1
                print(score)
          count_false = count_false+1
          print('count:',count_false)

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
    #print(rd1_s_c,rd1_s_t,rd1_s_tc)
    #print(rd2_s_c,rd2_s_t,rd2_s_tc)
    pygame.draw.rect(screen, (0,255,0), (150,450,100,50))
    pygame.draw.rect(screen, (255,0,0), (550,450,100,50))
    screen.blit(text_true, textRectt)
    screen.blit(text_false, textRectf)
    text_score = font.render(str(score), 1, (255,255,0))
    textRects = text_true.get_rect()
    textRects.center = ((700+(100/2)), (50+(50/2)))
    screen.blit(text_score, textRects) 
    pygame.display.update()
    a = 0
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
                        a = '1'
                        #print("1")
                        break
                    elif 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
                        a = '2'
                        #print("2")
                        break
        if ( a=='1' or a == '2'):
            break
    if(a == '1'):
          if(rd1_s_c == rd1_s_t==rd1_s_tc or rd2_s_c == rd2_s_t==rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c == rd2_s_t==rd2_s_tc or rd2_s_c == rd1_s_t==rd1_s_tc):
                score = score + 1
                print(score)
          count_true = count_true+1
          print('count:',count_true)

    elif(a == '2'):
          if(rd1_s_c != rd1_s_t!=rd1_s_tc or rd2_s_c != rd2_s_t!=rd2_s_tc):
                score = score + 1
                print(score)
          elif(rd1_s_c != rd2_s_t!=rd2_s_tc or rd2_s_c != rd1_s_t!=rd1_s_tc):
                score = score + 1
                print(score)
          count_false = count_false+1
          print('count:',count_false)

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

