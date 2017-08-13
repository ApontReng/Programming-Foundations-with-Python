
import turtle


def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():     
    windows = turtle.Screen()
    windows.bgcolor("red")
    #Create the turtle brad - draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    draw_square(brad)
    #Creat the turtle Angie - Draws circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    

    
    windows.exitonclick()
    
draw_art()
