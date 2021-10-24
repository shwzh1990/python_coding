'''
use turtle describe the syntax and gramma of the python
'''


from turtle import *
import turtle
import argparse
import time

def circle(radiation = 10, fillcolor = 'red'):
    turtle.color("black", fillcolor)
    pendown()
    turtle.color("black", "red")
    turtle.begin_fill()
    turtle.circle(radiation)
    turtle.end_fill()
    penup()

def square(width=40, length=80,fillcolor = "red"):
    pendown()
    turtle.color("black",fillcolor)
    turtle.begin_fill()
    turtle.speed(1)
    turtle.forward(length)
    turtle.left(90)
    turtle.backward(width)
    turtle.right(90)
    turtle.backward(length)
    turtle.right(90)
    turtle.backward(width)
    turtle.end_fill()
    penup()

def pen_setpostion(x=-800,y=400):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()


def position_home():
    pen_setpostion()

def For_loop_test(times,shape, gap = 100, fillcolor = 'red'):
    turtle.reset()
    position_home()

    for i in range(1, times+1):
        if shape == "square":
            square(fillcolor=fillcolor)
            turtle.left(90)
            turtle.forward(gap)
        elif shape == "circle":
            circle()
            turtle.forward(gap)
    print("for loop test done")

def list_empty():
    For_loop_test(100,'square',gap = 80,fillcolor='white')


list_a = []
shape_dict = {"square": square, 'circle':circle}

def scan_list():
    for i in list_a:
        if i == "square":
            square()
            turtle.left(90)
            turtle.forward(100)
        elif i == "circle":
            circle()
            turtle.forward(100)

def list_append(*args):
    list_a.extend(args)
    turtle.reset()
    position_home()
    scan_list()


def list_pop():
    if list_a:
        list_a.pop()
    turtle.reset()
    position_home()
    for i in list_a:
        if i == "square":
            square()
            turtle.left(90)
            turtle.forward(100)
        elif i == "circle":
            circle()
            turtle.forward(100)

def list_remove(str):
    list_a.remove(str)
    scan_list()
















