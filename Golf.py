import math
import turtle
from turtle import Screen


# Golf module to import
class Golf:
    # Change this height if the window is not fitting properly
    WIDTH, HEIGHT = 690, 350
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    origin_x = 0
    origin_y = 0
    G = 9.80665
    t = turtle.Turtle()

    # initialiation function, set turtle origin to bottom of screen
    def __init__(self):
        self.screen.tracer(0)
        self.t.hideturtle()
        self.t.penup()
        self.t.goto(self.origin_x, self.origin_x)
        self.t.pendown()
        self.t.speed(0)
        self.t.left(45)
        self.t.showturtle()

    # Clear Screen
    def clearScreen(self):
        self.t.clear()

    # Draw text function, optional x,y coordinates
    def drawText(self, text, x=0, y=330):
        # self.t.hideturtle()
        self.origin_x = x
        self.origin_y = y
        self.t.penup()
        self.t.goto(self.origin_x, self.origin_y)
        self.t.pendown()
        self.t.write(text)
        self.origin_x = 0
        self.origin_y = 0
        self.t.penup()
        self.t.goto(self.origin_x, self.origin_y)

    # Draw golf hole
    def drawHole(self, distance):
        self.origin_x = 0
        self.origin_y = 0
        self.t.penup()
        self.t.goto(self.origin_x, self.origin_y)
        self.t.setheading(0)
        self.t.goto(distance - 20, 20)
        self.t.pendown()
        self.t.fillcolor("red")
        self.t.begin_fill()
        self.t.forward(20)  # draw base
        self.t.left(90)
        self.t.forward(20)
        self.t.left(135)
        self.t.forward(28.28)
        self.t.end_fill()
        self.t.penup()
        self.t.left(135)
        self.t.forward(20)
        self.t.right(90)
        self.t.forward(30)
        self.t.pendown()
        # Horizontal Oval for green
        penX, penY = self.t.pos()
        self.t.fillcolor("#6ded5c")
        self.t.begin_fill()
        for i in range(0, 360):
            penX += math.cos(i * math.pi / 180) * 200 / 180
            penY += math.sin(i * math.pi / 180) * 15 / 180
            self.t.goto(penX, penY)
        self.t.end_fill()
        self.t.right(180)
        self.t.penup()
        self.t.forward(5)
        self.t.pendown()
        self.t.forward(25)
        self.t.penup()
        self.origin_x = 0
        self.origin_y = 0
        self.t.penup()
        self.t.goto(self.origin_x, self.origin_y)

    # Shoot ball function, optional angle parameter
    # returns distance shot
    def shootBall(self, power: object, angle: object = 45) -> object:
        # Reverse ball direction if power is negative
        if power >= 0:
            negative = 1
        elif power < 0:
            negative = -1

        self.t.penup()
        self.t.goto(self.origin_x, self.origin_y)
        self.t.pendown()
        self.t.shape("circle")
        self.t.turtlesize(.5)
        self.t.fillcolor("#ebebeb")

        angle = angle
        power = abs(power)
        y = 0
        x = 0
        time = 0
        distance = 0
        # Parabolic arc
        while y >= 0:
            time += .01
            x = negative * power * math.cos(
                math.radians(angle)) * time + self.origin_x
            y = power * math.sin(math.radians(angle)) * time - ((
                                                                        (time ** 2) * self.G) / 2) + self.origin_y
            self.t.goto(
                negative * power * math.cos(math.radians(angle)) * time +
                self.origin_x,
                power * math.sin(math.radians(angle)) * time -
                (((time ** 2) * self.G) / 2) + self.origin_y)
        self.t.stamp()
        distance = x - self.origin_x
        self.origin_x = x
        self.origin_y = y
        self.screen.update()
        return distance
