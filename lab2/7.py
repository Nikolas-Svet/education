import turtle
import random

def draw_mountain(t, x1, y1, x2, y2, displace, depth):
    if depth == 0:
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)
    else:
        mid_x = (x1 + x2) / 2 + random.uniform(-displace, displace)
        mid_y = (y1 + y2) / 2 + random.uniform(-displace, displace)
        draw_mountain(t, x1, y1, mid_x, mid_y, displace / 2, depth - 1)
        draw_mountain(t, mid_x, mid_y, x2, y2, displace / 2, depth - 1)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-300, -100)
    t.pendown()
    draw_mountain(t, -300, -100, 300, -100, 150, 8)
    myWin.exitonclick()

main()
