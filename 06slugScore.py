from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

#####################
#Variables
#####################

#Horizontal pixels for Slug
slug = [[2,4], [3,4],[4,4]]

#List with coordinates of existing vegetables
vegetables = []

#Color for Slug
color = (255, 255, 255)

#Color for Vegetables
colorVeg = (255, 0, 0)

#Direction updated by event on joystick
direction = "right"

#erase pixel color
blank = (0, 0, 0)


#Score
score = 1


#Pause for difficulty
pause = 1

#Variable for game over
dead = False

#####################
#Functions
#####################

def draw_slug():
    for segment in slug:
        sense.set_pixel(segment[0], segment[1], color)

def move():
    global score, pause, dead
    remove = True 
    #Find the last and first items in the slug list
    last = slug[-1]
    first = slug[0]
    next = list(last)

    #Find the next pixel in the direction the slug is currently moving
    if direction == "right":
        #move along the column
        if last[0] + 1 == 8:
            next[0] = 0

        else:
            next[0] = last[0] + 1
            
    if direction == "left":
        #move along the column
        if last[0] - 1 == -1:
            next[0] = 7

        else:
            next[0] = last[0] - 1

    if direction == "down":
        #move along the row
        if last[1] + 1 == 8:
            next[1] = 0

        else:
            next[1] = last[1] + 1

    if direction == "up":
        #move along the column
        if last[1] - 1 == -1:
            next[1] = 7

        else:
            next[1] = last[1] - 1
    

    if next in slug:
        dead =  True
        
    #Add this pixel at the end of the slugs list
    slug.append(next)

    # Set the nex pixel to the slugs color
    sense.set_pixel(next[0], next[1], color)

    if next in vegetables:
        vegetables.remove(next)
        score+=1
        remove = False

        if score%5 == 0:
            pause = pause*0.8

    #Only remove last if we ate
    if remove == True:
        #Set the first pixel in the slug list to blank
        sense.set_pixel(first[0], first[1], blank)

        #Remove the first pixel from the list
        slug.remove(first)



def joystick_moved(event):
    global direction
    direction = event.direction


def make_veg():
    new = slug[0]
    while new in slug:
        x = randint(0,7)
        y = randint(0,7)
        new = [x,y]
    vegetables.append(new)    
    sense.set_pixel(x,y,colorVeg)

#####################
#Main program
#####################

sense.clear()
draw_slug()
sense.stick.direction_any = joystick_moved
while True:
    sleep(pause)
    
    move()

    #if len(vegetables)< 3 and randint(1,5) > 4: #20% chance for vegetable if there are not that many
    if len(vegetables)< 3:
        make_veg()
    if dead == True:
        sense.show_message(str(score))
