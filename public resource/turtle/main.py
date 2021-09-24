
'''
practice one:
just give student a example.

'''
from turtle import *
import turtle
def practice_one():
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        print(pos())
        if abs(pos()) < 1:
            break
    end_fill()
    done()
'''
function:
1. shape
2. pensize
3. speed
4. forward
5. backward
6. setposition   
7. right
8. penup
9. pendown 
10.home： go back to the 0,0 coordination.

'''
def practice_two():
    tim = turtle.Turtle();
    tim.color("blue")
    tim.pensize(3)
    tim.shape('turtle')
    tim.speed(1)
    tim.forward(500)
    tim.backward(50)
    tim.right(90)
    tim.forward(325)
    tim.left(34)
    tim.backward(432)
    tim.penup()
    tim.setposition(300,300)



