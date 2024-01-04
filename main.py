import turtle

screen = turtle.Screen()
screen.bgcolor('black')
t = turtle.Turtle()
t.shape()
t.speed(10000)


def draw_star(points, rotate, step):
    angle = 360/points
    angle_rotate = 360/rotate
    red = 0.9
    green = 0.9
    blue = 0.9
    for i in range(0, points * 100):
        t.forward(300)
        t.right(angle+angle_rotate + step)
        red *= 0.95
        green *= 0.95
        blue *= 0.95
        t.pencolor(red, green, blue)

draw_star(60, 5, 1)

screen.exitonclick()
