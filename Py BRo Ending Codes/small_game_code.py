import pygame
import sys
import random
from random import randint
from time import sleep
import time
from constants import *

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
    textRectt.center = ((150+(100/2)), (450+(50/2)))
    textRectf = text_false.get_rect()
    textRectf.center = ((550+(100/2)), (450+(50/2)))
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
    circle = pygame.Surface((100, 100))
    rect = circle.get_rect()
    rect.center = screen.get_rect().center
    pygame.draw.circle(circle, colorCr, (x, y), 40)

    square = pygame.Surface((200, 200))
    rect = square.get_rect()
    rect.center = screen.get_rect().center
    # pygame.draw.rect(square, color2, pygame.Rect(x+60, y+60, 100, 100))
    pygame.draw.rect(square, colorSq, pygame.Rect(x-40, y+80, 100, 100))

    myfont = pygame.font.SysFont('ALGERIAN', 48)
    textsurfaceCr = myfont.render(txtCr, False, txtcolorCr)

    textsurfaceSq = myfont.render(txtSq, False, txtcolorSq)

    screen.fill((0, 0, 0))
    screen.blit(textsurfaceSq, (10, y+300))
    screen.blit(textsurfaceCr, (10, y+200))
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

        total_mins = time_left//60 # minutes left
        total_sec = time_left-(60*(total_mins)) #seconds left
        time_left -= 1
        if time_left > -1:
            text = font.render(("Time left: "+str(total_mins)+":"+str(total_sec)), True, color)
            screen.blit(text, (20, 20))
            pygame.display.flip()
            screen.fill((20,20,20))
            time.sleep(1)#making the time interval of the loop 1sec
        else:
            text = font.render("Time Over!!", True, color)
            screen.blit(text, (20, 20))
            pygame.display.flip()
            screen.fill((20,20,20))



   #     if current_time >= exit_time:
   #         done = True
      #  if time_left > -1:
       #     continue
     #   else:
      #      done = True

        clock.tick(5)

# ..................Function For Rhombus And Parallelogram........#


def draw_rhombus_and_parallelogram(screen, delay, colorRb, txtRb, txtcolorRb,
                                   colorPl, txtPl, txtcolorPl, x, y):

    square = pygame.Surface((500, 500))
    rect = square.get_rect()
    rect.center = screen.get_rect().center

    myfont = pygame.font.SysFont('ALGERIAN', 48)
    textsurfaceRb = myfont.render(txtRb, False, txtcolorRb)
    textsurfacePl = myfont.render(txtPl, False, txtcolorPl)

    pygame.draw.lines(square, colorRb, False, [
                      (100+100, 100), (150+100, 0), (200+100, 100)], 7)
    pygame.draw.lines(square, colorRb, False, [
                      (100+100, 100), (150+100, 200), (200+100, 100)], 7)
    pygame.draw.lines(square, colorPl, True, [
                      (100+100, 100+150), (400+100, 100+150),
                      (300+100, 200+150), (0+100, 200+150)], 7)

    screen.fill((0, 0, 0))

    # screen.blit(paralle, rect)
    screen.blit(textsurfaceRb, (10, y+300))
    screen.blit(textsurfacePl, (10, y+200))
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
    pygame.draw.rect(screen, (0, 255, 0), (150, 450, 100, 50))
    pygame.draw.rect(screen, (255, 0, 0), (550, 450, 100, 50))
    screen.blit(text_true, textRectt)
    screen.blit(text_false, textRectf)
    text_score = font_freesans.render(
        "Score: "+str(score), 1, (255, 255, 0))
    textRects = text_true.get_rect()
    textRects.center = ((600+(100/2)), (50+(50/2)))
    screen.blit(text_score, textRects)
    pygame.display.update()
    a = 0
    ti = time.time()
    while True:
        time_elapse = time.time() - ti
        if(time_elapse >= 5.0):
            # print(time_elapse)
            break
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (150+100 > mouse[0] > 150 and
                            450+50 > mouse[1] > 450):
                        a = '1'
                        # print("1")
                        break
                    elif (550+100 > mouse[0] > 550 and
                            450+50 > mouse[1] > 450):
                        a = '2'
                        # print("2")
                        break
        if (a == '1' or a == '2'):
            break
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
        if(rd1_s_c != rd1_s_t != rd1_s_tc or
                rd2_s_c != rd2_s_t != rd2_s_tc):
            score = score + 1
            # print(score)
        elif(rd1_s_c != rd2_s_t != rd2_s_tc or
                rd2_s_c != rd1_s_t != rd1_s_tc):
            score = score + 1
            # print(score)
        count_false = count_false+1
        # print('count:', count_false)
        count = count + 1
    else:
        count = count + 1
    print(count)
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
    initial_vars = initialize()
    shapes = [draw_circle_and_square, draw_rhombus_and_parallelogram]
    for i in range(10):
        initial_vars = update_screen(initial_vars, shapes[randint(0, 1)])
    pygame.quit()


start_game()
