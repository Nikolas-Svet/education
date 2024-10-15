import turtle
import random

def tree(branchLen, t, thickness):
    if branchLen > 5:
        t.width(thickness)
        if branchLen < 20:
            t.color("green")
        else:
            t.color("brown")
        t.forward(branchLen)
        angle = random.randint(15, 45)
        t.right(angle)
        tree(branchLen - random.randint(10, 20), t, thickness - 1)
        t.left(2 * angle)
        tree(branchLen - random.randint(10, 20), t, thickness - 1)
        t.right(angle)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree(75, t, 7)
    myWin.exitonclick()

main()
