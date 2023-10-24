from turtle import Turtle, Screen


tur = Turtle()
screen = Screen()


def movefor():
    tur.forward(10)


def moveback():
    tur.backward(10)


def movecCount():
    tur.left(10)


def moveclock():
    tur.right(10)


def clear():
    tur.reset()


screen.listen()
screen.onkeypress(movefor, "w")
screen.onkeypress(moveback, "s")
screen.onkeypress(movecCount, "a")
screen.onkeypress(moveclock, "d")
screen.onkey(clear, "c")

screen.exitonclick()
