from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

#####################
#Variables
#####################

#Horizontal pixels for Slug
slug = [[2,4], [3,4],[4,4]]
#Color for Slug
color = (255, 255, 255)
#Direction
direction = "right"
#erase pixel color
blank = (0, 0, 0)

#####################
#Functions
#####################

def draw_slug():
    for segment in slug:
        sense.set_pixel(segment[0], segment[1], color)

def move():
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
    
        
    #Add this pixel at the end of the slugs list
    slug.append(next)

    # Set the nex pixel to the slugs color
    sense.set_pixel(next[0], next[1], color)

    #Set the first pixel in the slug list to blank
    sense.set_pixel(first[0], first[1], blank)

    #Remove the first pixel from the list
    slug.remove(first)

def joystick_moved(event):
    global direction
    direction = event.direction
#####################
#Main program
#####################

sense.clear()
draw_slug()
sense.stick.direction_any = joystick_moved
while True:
    sleep(0.5)
    move()
