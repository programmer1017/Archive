import turtle as t
import random

te = t. Turtle()

te. shape("turtle")              #악당 거북이(빨간색)
te. color("red")
te. speed(0)
te. up()
te. goto(0, 200)


ts = t. Turtle()                 #먹이(초록색 동그라미)
ts. shape("circle")
ts. color("green")
ts. speed(0)
ts. up()
ts. goto(0, -200)


def turn_right():
    t. seth(0)

def turn_up():
    t. seth(90)

def turn_left():
           t. seth(180)
def turn_down():
    t. seth(270)

def play():
     t. fd(10)
     ang = te.towards(t. pos())
     te. seth(ang)
     te. fd(9)
     if t. distance(ts) < 12:
         star_x = 
     
