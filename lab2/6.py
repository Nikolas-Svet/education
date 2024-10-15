import turtle

def dragon_curve(t, length, depth, sign=1):
    if depth == 0:
        t.forward(length)
    else:
        t.right(45 * sign)
        dragon_curve(t, length / (2 ** 0.5), depth - 1, 1)
        t.left(90 * sign)
        dragon_curve(t, length / (2 ** 0.5), depth - 1, -1)
        t.right(45 * sign)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(0, 0)
    t.pendown()
    depth = 12
    length = 400
    dragon_curve(t, length, depth)
    myWin.exitonclick()

main()
