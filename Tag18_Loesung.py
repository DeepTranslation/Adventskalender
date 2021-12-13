import turtle as t
from turtle import Screen
import math

class Dreieck:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3


def zeichne_dreieck(turtle, dreieck, farbe):
    turtle.penup()
    turtle.color(farbe)
    turtle.goto(dreieck.x1, -dreieck.y1)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(dreieck.x2, -dreieck.y2)
    turtle.goto(dreieck.x3, -dreieck.y3)
    turtle.goto(dreieck.x1, -dreieck.y1)
    turtle.end_fill()

def zeichne_stamm(turtle, x1, y1, x2, y2, farbe):
    turtle.penup()
    turtle.color(farbe)
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(x2, y1)
    turtle.goto(x2, y2)
    turtle.goto(x1, y2)
    turtle.goto(x1, y1)
    turtle.end_fill()

def sierpinski_dreieck(turtle, x1, y1, x2, y2, farbe, tiefe, maximaltiefe):
    faktor = math.sqrt(3)/2
    if tiefe == maximaltiefe:
        x_neu = (x1 + x2) / 2 + faktor * (y2 - y1)
        y_neu = (y1 + y2) / 2 + faktor * (x1 - x2)
        neues_dreieck = Dreieck(x1, y1,x2,y2, x_neu, y_neu)
        zeichne_dreieck(turtle, neues_dreieck, farbe)
    else:
        sierpinski_dreieck(turtle, x1, y1, (x1 + x2) / 2, (y1 + y2) / 2, farbe, tiefe + 1, maximaltiefe)
        sierpinski_dreieck(turtle, (x1 + x2) / 2, (y1 + y2) / 2, x2, y2, farbe, tiefe + 1, maximaltiefe)
        sierpinski_dreieck(turtle, ((3 * x1 + x2) / 4 + faktor * (y2 - y1) / 2),
                                 ((3 * y1 + y2) / 4 + faktor * (x1 - x2) / 2),
                                 ((x1 + 3 * x2) / 4 + faktor * (y2 - y1) / 2),
                                 ((y1 + 3 * y2) / 4 + faktor * (x1 - x2) / 2), farbe, tiefe + 1, maximaltiefe)


tim = t.Turtle("turtle")
screen = Screen()
screen.bgcolor("blanched almond")
tim.speed("fastest")

tim.color( "sienna")
zeichne_stamm(tim, -100, -200, 100,-350, "sienna")
sierpinski_dreieck(tim, -300, 200, 300, 200, "forest green", 0, 2)
tim.hideturtle()

screen.exitonclick()

