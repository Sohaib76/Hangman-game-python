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
font1 = pygame.font.SysFont("Arial", 30)
clock = pygame.time.Clock()
fps=60
timer=3600
#--------------function------------For Circle And Square
def draw_circle_and_square(counter, delay, colorCr , txtCr, txtcolorCr, colorSq, txtSq, txtcolorSq ,x, y):
#def draw_rhombus_and_parallelogram(screen, delay, colorRb, txtRb,txtcolorRb ,colorPl, txtPl, txtcolorPl, x, y):

    

    circle = pygame.Surface((100, 100))                    #circle = pygame.Surface((2*50, 2*50))
    rect = circle.get_rect()
    rect.center = screen.get_rect().center
    pygame.draw.circle(circle, colorCr, (x,y), 40)


    
    square = pygame.Surface((200, 200))
    rect = square.get_rect()
    rect.center = screen.get_rect().center
    pygame.draw.rect(square, colorSq, pygame.Rect(x-40, y+80, 100, 100))          #pygame.draw.rect(square, color2, pygame.Rect(x+60, y+60, 100, 100))

    #bg=pygame.image.load('flippyboard.png')  
    clock = pygame.time.Clock()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
 #   timer = "Time : {}".format(counter)
  #  text_counter = font1.render(timer, True, (255,255,255))
    #text_timer=font.render(timer/60,True,(255,255,255))
    textsurfaceCr = myfont.render(txtCr, False, txtcolorCr)
    
    
    textsurfaceSq = myfont.render(txtSq, False, txtcolorSq)
    
    
    screen.fill((0,0,0))
    screen.blit(textsurfaceSq,(x-20,y+300))
    screen.blit(textsurfaceCr,(x-20,y+200))
    screen.blit(square,rect)
    screen.blit(circle,rect)
    #screen.blit(text_counter,(650,550))

    pygame.display.flip()
    
    
    
    
    #blit wlit
    
    current_time = pygame.time.get_ticks()
    exit_time = current_time + delay
    clock = pygame.time.Clock()
    frame_count = 0
    frame_rate = 60
    start_time = 90

    done = False

    while not done:
    


    
    #Quit event etc
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                done= True
        # --- Timer going up ---
        # Calculate total seconds
        total_seconds = frame_count // frame_rate
             
                # Divide by 60 to get total minutes
        minutes = total_seconds // 60
             
                # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60
             
                # Use python string formatting to format in leading zeros
        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
             
                # Blit to the screen
        text = font.render(output_string, True, orange)
        #screen.blit(text, [600,500 ])
                # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        frame_count += 1
             
                # Limit frames per second
        clock.tick(frame_rate)
             
                # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

                
        current_time = pygame.time.get_ticks()

        if current_time >= exit_time:
            done = True

        clock.tick(5)

pygame.init()

screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()


#score =  0
        
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
counter=0
frame_count = 0
frame_rate = 60
start_time = 90

total_seconds = frame_count // frame_rate
             
                # Divide by 60 to get total minutes
minutes = total_seconds // 60
             
                # Use modulus (remainder) to get seconds
seconds = total_seconds % 60
        


for i in range(20):
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

    counter=draw_circle_and_square(counter, 100, color_name[rd1_s_c],color_disp[rd1_s_t], color_name[rd1_s_tc], color_name[rd2_s_c], color_disp[rd2_s_t], color_name[rd2_s_tc],x, y)

    pygame.draw.rect(screen, (0,255,0), (150,450,100,50))
    pygame.draw.rect(screen, (255,0,0), (550,450,100,50))
    screen.blit(text_true, textRectt)
    screen.blit(text_false, textRectf)
    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
    text = font.render(output_string, True, orange)
    screen.blit(text, [600,500 ])
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 1
 
    # Limit frames per second
    clock.tick(frame_rate)

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
                        #return counter
                        break
                    elif 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
                        a = '2'
                        #print("2")
                        break
            #counter += 1
            clock.tick(frame_rate)
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

    #t3 = time.time()
    #T = t3 - t2
    #print("Time = ",T,'sec')
