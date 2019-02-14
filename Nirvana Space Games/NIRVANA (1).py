#space invaders part-1
import turtle
import os
import math
import random
from turtle import *


#set the screen
wn=turtle.Screen()
wn.bgcolor('black')
wn.title('NIRVANA')
wn.bgpic('795.png')

turtle.register_shape('spaceee.gif')


#draw border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(4)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#set the score to 0
score=0

#draw the score
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290,280)
scorestring='score:%s'%score
score_pen.write(scorestring,False,align='left',font=('Arial',14,'normal'))
score_pen.hideturtle()


#player turtle
player=turtle.Turtle()
player.color('white')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
playerspeed=15

#choose a no of enemies
noofenemies=5
#create an empty list for enemies
enemies=[]

#add enemies to the list
for i in range(noofenemies):
    #create enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color('red')
    enemy.shape('spaceee.gif')
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-200,200)
    y=random.randint(100,250)
    enemy.setposition(x,y)

    enemyspeed=2


#create flame
flame=turtle.Turtle()
flame.color('blue')
flame.shape('triangle')
flame.penup()
flame.speed(0)
flame.setheading(90)
flame.shapesize(0.5,0.5)
flame.hideturtle()

flamespeed=30

#flamestate
#falme is ready
#flame is unleashed
flamestate='ready'


#move the player left and right
def move_left():
    x=player.xcor()
    x-=playerspeed
    if x<-280:
        x=-280
    player.setx(x)
def move_right():
    x=player.xcor()
    x+=playerspeed
    if x>280:
        x=280
    player.setx(x)

def fire_flame():
    #declare flamestate as a global
    global flamestate
    if flamestate=='ready':
        flamestate='fire'
        #flame moves just above the player
        x=player.xcor()
        y=player.ycor() + 10
        flame.setposition(x,y)
        flame.showturtle()
def isacollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
                       
                       
                    
    
#keyboard
turtle.listen()
turtle.onkey(move_left,'Left')
turtle.onkey(move_right,'Right')
turtle.onkey(fire_flame,'space')

 #main game loop
while True:
    
    

    for enemy in enemies:
        #move the enemy
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)

        #move the enemy back and down
        if enemy.xcor()>280:
            #move all enemies down
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
                #CHANGE DIRECTION
            enemyspeed*=-1

        if enemy.xcor()<-280:
            #MOVE ALL ENEMIES DOWN
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
                #CHANGES DIRECTION
            enemyspeed*=-1
                
    #check for q collision b/w flame and enemy
        if isacollision(flame,enemy):
                           #rest flame
                           flame.hideturtle()
                           flamestate='ready'
                           flame.setposition(0,-400)
                           #reset enemy
                           x=random.randint(-200,200)
                           y=random.randint(100,250)
                           enemy.setposition(x,y)
                           #update the score
                           score+=10
                           scorestring='score:%s'%score
                           score_pen.clear()
                           score_pen.write(scorestring,False,align='left',font=('Arial',14,'normal'))
                           


         #if collision takes place b/w player and enemy
        if isacollision(player,enemy):
             player.hideturtle()
             enemy.hideturtle()
             print('game over')
            
             breakpoint
             quit()

    #MOVE THE flame
    if flamestate=='fire':
        y=flame.ycor()
        y+=flamespeed
        flame.sety(y)

    #test to see if bullet has crossed the boundary
    if flame.ycor()>275:
        flame.hideturtle()
        flamestate='ready'
        
     
    
                    
        
