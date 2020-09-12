#!/usr/bin/pyhon
#spirals.py

__author__  = "Beckwith"
__version__ = "1.0"

'''Example code for Intro. exploration - draw some spirals'''

import turtle
import random

def main():
    '''creates and moves turtles in spiral pattern'''
    
    turtle_list = []  # a blank list to store all turtles in
    heading = 0       # given in degrees
    num_turtles = 15  # default is 15
    
    # create the screen for the turtles:
    wn = turtle.Screen()
    wn.setup(500, 500)
    wn.colormode(255)  # allows for specifying RGB values - see below
    
    # create a bunch of turtles, each will draw a spiral:
    for i in range(num_turtles):
        current_turtle = turtle.Turtle()   # Make a new turtle, initialize values
        current_turtle.setheading(heading)
        current_turtle.pensize(2)          # default is 2
        
        # set the color of a turtle randomly - giving amount of Red, Green, Blue betwee 0 and 255
        current_turtle.color((random.randrange(256), random.randrange(256), random.randrange(256)))
        
        wn.tracer(4, 0)        # 1st number adjusts speed
        
        turtle_list.append(current_turtle)       # add the new turtle to the list
        
        heading = heading + 360 / num_turtles  # change angle for next turtle

    # move all the turtles created above:
    distance_to_move = 15
    for angle in range(100):
        move_turtles(turtle_list, distance_to_move, angle)

    # display some text:
    w = turtle_list[0] # get the first turtle to use to display text
    w.up()

    # 14 and 17 below are font sizes:
    w.goto(0, 40)
    w.write("Running your first program", font=("Arial", 14, "normal"))
    w.goto(0, -35)
    w.write("in Python at CCHS", font=("Arial", 17, "normal"))

def move_turtles(t_list, dist, angle):
    '''moves all the turtles in spiral pattern, since a new angle is being
    sent each time'''
    
    for turtle in t_list:
        turtle.forward(dist)
        turtle.right(angle)

main()

