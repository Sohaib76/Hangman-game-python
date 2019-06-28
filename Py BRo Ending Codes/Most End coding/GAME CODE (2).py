import pygame
import sys
import random
from random import randint
from time import sleep
import time
from constants import *


#start_screen function
textcolor = Green
textshadowcolor = Red 
def showtextscreen(font):
    # This function displays large text in the
    # center of the screen until a key is pressed.
    # Draw the text drop shadowu
    titlesurf,titlerect=maketextobjects(text,font,textshadowcolor)
    titlerect.centre =(int(DISPLAY_SIZE/2)-3)
    surf.blit(titlesurf,titlerect)

    # Draw the text
    titlesurf,titlerect=maketextobjects(text,font,textcolor)
    titlerect.centre =(int(DISPLAY_SIZE/2))
    surf.blit(titlesurf,titlerect)

    # Draw the additional "Press a key to play." text.
    presskeysurf,presskeyrect=maketextobjects('Press a key to play.', basicfont, textcolor)
    presskeyrect.centre =(int(DISPLAY_SIZE/2))
    surf.blit(presskeysurf,presskeyrect)

    while checkForKeyPress() == None:
        pygame.display.update()
        clock.tick(5)

def checkForKeyPress():
    # Go through event queue looking for a KEYUP event.
    # Grab KEYDOWN events to remove them from the event queue.
    checkForQuit()

    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None        

 
#Timer function
total_time =30
def create_timer_box(font):
    text = font.render("TIME LEFT: ", True, (255, 255, 255))
    return text, text.get_rect()

def update_timer(font, time):
    text = font.render('         %i:%.4f' %(time//60,time%60), True, (255, 255, 255))
    rect = text.get_rect()
    rect.topleft = (105, 0)
    return text, rect

def draw_timer(box_surf, box_rect, timer_surf, timer_rect):
    surf = pygame.surface.Surface((250, 50))
    surf.fill((0, 0, 0))
    surf.blit(box_surf, box_rect)
    surf.blit(timer_surf, timer_rect)
    return surf
    

# --------------function------------For Circle And Square

def initialize():
    screen = pygame.display.set_mode(DISPLAY_SIZE)
    pygame.font.init()
    font_algerian = pygame.font.SysFont("ALGERIAN", 96)
    pygame.init()
    text1 = font_algerian.render("Brown", True, (139, 117, 0))
    screen_rect = screen.get_rect()
    pressed = pygame.key.get_pressed()
    font_freesans = pygame.font.Font('freesansbold.ttf', 32)
    text_true = font_freesans.render('True', True, (0, 0, 0))
    text_false = font_freesans.render('False', True, (0, 0, 0))
    textRectt = text_true.get_rect()
    textRectt.center = ((50+(100/2)), (700+(50/2)))
    textRectf = text_false.get_rect()
    textRectf.center = ((400+(100/2)), (700+(50/2)))
    score = 0
    count_true = 0
    count_false = 0
    count = 0
    return [screen,
            font_algerian,
            text1,
            screen_rect,
            pressed,
            font_freesans,
            text_true,
            text_false,
            textRectt,
            textRectf,
            score,
            count_true,
            count_false,
            count]


def draw_circle_and_square(screen, delay, colorCr, txtCr, txtcolorCr,
                           colorSq, txtSq, txtcolorSq, x, y):
    # def draw_rhombus_and_parallelogram(screen, delay, colorRb, txtRb,
    # txtcolorRb ,colorPl, txtPl, txtcolorPl, x, y):

    # circle = pygame.Surface((2*50, 2*50))
    circle = pygame.Surface((400, 200)).convert_alpha()
    circle.fill((0,0,0,0))
    rect = circle.get_rect()
    rect.center = screen.get_rect().center
    pygame.draw.circle(circle, colorCr, (x+200, y+60), 100)

    bg=pygame.image.load('flippy2.png')
    bg=pygame.transform.scale(bg,(800,800))

    square = pygame.Surface((400, 400)).convert_alpha()
    square.fill((0,0,0,0))
    rect = square.get_rect()
    rect.center = screen.get_rect().center
    # pygame.draw.rect(square, color2, pygame.Rect(x+60, y+60, 100, 100))
    pygame.draw.rect(square, colorSq, pygame.Rect(x+100, y+200, 200, 300))

    myfont = pygame.font.SysFont('ALGERIAN', 48)
    textsurfaceCr = myfont.render(txtCr, False, txtcolorCr)

    textsurfaceSq = myfont.render(txtSq, False, txtcolorSq)

    screen.blit(bg,( 0, 0))
    screen.blit(textsurfaceSq, (10, y+250))
    screen.blit(textsurfaceCr, (10, y+500))
    screen.blit(square, rect)
    screen.blit(circle, rect)
    pygame.display.flip()

    # blit wlit

    current_time = pygame.time.get_ticks()
    exit_time = current_time + delay
    clock = pygame.time.Clock()

    done = False

    while not done:

        # Quit event etc
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                done = True

        current_time = pygame.time.get_ticks()

        if current_time >= exit_time:
            done = True

        clock.tick(5)

# ..................Function For Rhombus And Parallelogram........#


def draw_rhombus_and_parallelogram(screen, delay, colorRb, txtRb, txtcolorRb,
                                   colorPl, txtPl, txtcolorPl, x, y):

    square = pygame.Surface((600, 600)).convert_alpha()
    square.fill((0,0,0,0))
    rect = square.get_rect()
    rect.center = screen.get_rect().center

    bg=pygame.image.load('flippy2.png')
    bg=pygame.transform.scale(bg,(800,800))

    myfont = pygame.font.SysFont('ALGERIAN', 48)
    textsurfaceRb = myfont.render(txtRb, False, txtcolorRb)
    textsurfacePl = myfont.render(txtPl, False, txtcolorPl)

    pygame.draw.lines(square, colorRb, False, [
                      (300, 200), (350, 100), (400, 200)], 50)
    pygame.draw.lines(square, colorRb, False, [
                      (300, 200), (350, 300), (400, 200)], 50)
    pygame.draw.lines(square, colorPl, True, [
                      (300, 450), (600, 450),
                      (500, 550), (200, 550)], 10)

    screen.blit(bg,(0, 0))

    # screen.blit(paralle, rect)
    screen.blit(textsurfaceRb, (10, y+250))
    screen.blit(textsurfacePl, (10, y+500))
    screen.blit(square, rect)
    pygame.display.flip()

    # blit wlit

    current_time = pygame.time.get_ticks()
    exit_time = current_time + delay
    clock = pygame.time.Clock()

    done = False

    while not done:

        # Quit event etc
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                done = True

        current_time = pygame.time.get_ticks()

        if current_time >= exit_time:
            done = True

        clock.tick(5)
# ----------program----------
# pygame.draw.circle(screen, gold, (x,y), 40)


def randomize():
    min_rand = randint(0, 3)
    max_rand = randint(4, 7)
    rd1_s_c = randint(min_rand, max_rand)  # shape color
    rd1_s_t = randint(min_rand, max_rand)  # shape text
    rd1_s_tc = rd1_s_t
    # rd1_s_tc = randint(min_rand,max_rand)    #shape text color
    rd2_s_c = randint(min_rand, max_rand)  # shape color
    rd2_s_t = randint(min_rand, max_rand)  # shape text
    rd2_s_tc = rd2_s_t
    return (rd1_s_c, rd1_s_t, rd1_s_tc, rd2_s_c, rd2_s_t, rd2_s_tc)
# pygame.draw.rect(screen, aliceBlue, pygame.Rect(x, y, 100, 80))


def update_screen(initial_vars, cal):
    global total_time
    (rd1_s_c,  # shape color
     rd1_s_t,  # shape text
     rd1_s_tc,
     # rd1_s_tc = randint(min_rand,max_rand)    #shape text color
     rd2_s_c,  # shape color
     rd2_s_t,  # shape text
     rd2_s_tc) = randomize()
    (screen,
     font_algerian,
     text1,
     screen_rect,
     pressed,
     font_freesans,
     text_true,
     text_false,
     textRectt,
     textRectf,
     score,
     count_true,
     count_false,
     count) = initial_vars
    cal(screen, 100,
        color_name[rd1_s_c],
        color_disp[rd1_s_t],
        color_name[rd1_s_tc],
        color_name[rd2_s_c],
        color_disp[rd2_s_t],
        color_name[rd2_s_tc],
        x, y)
    pygame.draw.rect(screen, (0, 255, 0), (50, 700, 100, 50))
    pygame.draw.rect(screen, (255, 0, 0), (400, 700, 100, 50))
    screen.blit(text_true, textRectt)
    screen.blit(text_false, textRectf)
    text_score = font_freesans.render(
        "Score: "+str(score), 1, (255, 255, 0))
    textRects = text_true.get_rect()
    textRects.center = ((600+(100/2)), (50+(50/2)))
    screen.blit(text_score, textRects)
    
    ####
    time_surf, time_rect = create_timer_box(font_freesans)
    ####
    skipped=0
    pygame.display.update()
    a = 0
    ti = time.time()
    while True:
        time_elapse = time.time() - ti
        ###
        timer_surf, timer_rect = update_timer(font_freesans,total_time-time_elapse) #Add
        ###
        if time_elapse >= 5:
            
            skipped=skipped+1
            print(skipped)
            
            break
        elif total_time-time_elapse <=0:
            break\
        
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (50+100 > mouse[0] > 50 and
                            700+50 > mouse[1] > 700):
                        a = '1'
                        # print("1")
                        break
                    elif (400+100 > mouse[0] > 400 and
                            700+50 > mouse[1] > 700):
                        a = '2'
                        # print("2")
                        break
        if (a == '1' or a == '2'):
            break
        ###
        screen.blit(draw_timer(time_surf, time_rect,
                               timer_surf, timer_rect),
                    (20, 50)) #Timer position
        pygame.display.flip() #Add this for timer update
        ###
    total_time-=time_elapse
    if(a == '1'):
        if(rd1_s_c == rd1_s_t == rd1_s_tc or
                rd2_s_c == rd2_s_t == rd2_s_tc):
            score = score + 1
            # print(score)
        elif(rd1_s_c == rd2_s_t == rd2_s_tc or
                rd2_s_c == rd1_s_t == rd1_s_tc):
            score = score + 1
            # print(score)
        count_true = count_true+1
        count = count + 1
        # print('count:', count_true)

    elif(a == '2'):
        if(not rd1_s_c == rd1_s_t == rd1_s_tc and 
               (not rd2_s_c == rd2_s_t == rd2_s_tc) and
           (not rd1_s_c == rd2_s_t == rd2_s_tc) and
               (not rd2_s_c == rd1_s_t == rd1_s_tc)):
            score = score + 1
            # print(score)
        count_false = count_false+1
        # print('count:', count_false)
        count = count + 1
    else:
        count = count + 1
    print('count:     ',count)
    print ('SCORE:',score)

    FALSE_ATTEMPT= count-score

    print(".....TOTAL FALSE ATTEMPT......",FALSE_ATTEMPT)
    return [screen,
            font_algerian,
            text1,
            screen_rect,
            pressed,
            font_freesans,
            text_true,
            text_false,
            textRectt,
            textRectf,
            score,
            count_true,
            count_false,
            count]


def start_game():
    #showtextscreen('STROOP TEST')
    initial_vars = initialize()
    shapes = [draw_circle_and_square, draw_rhombus_and_parallelogram]
    #for i in range(30):
    while total_time>=0:
        initial_vars = update_screen(initial_vars, shapes[randint(0,1)])
    pygame.quit()

'''
black=(0,0,0)
end_it=False
while (end_it==False):
    
    myfont=pygame.font.SysFont("Arial", 40)
    nlabel=myfont.render("Welcome "+"TO"+" Start Screen", 1, (255, 0, 0))
    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN:
            end_it=True
    screen.blit(nlabel,(200,200))
    pygame.display.flip()
    '''
start_game()
