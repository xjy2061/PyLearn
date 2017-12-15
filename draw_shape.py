import turtle


def draw_rect(pen):
    for i in range(0, 4):
        pen.forward(100)
        pen.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    pen = turtle.Turtle()
    pen.color("yellow")
    pen.shape("turtle")
    for i in range(0, 360, 10):
        draw_rect(pen)
        pen.right(10)

    window.exitonclick()


draw_art()
