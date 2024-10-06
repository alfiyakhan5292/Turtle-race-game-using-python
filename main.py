import turtle
import random

def move_turtle(turtle):
    distance = random.randint(1, 20)
    turtle.forward(distance)

def setup_race():
    screen = turtle.Screen()
    screen.setup(800, 900)

    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
    turtles = []

    y = -100 

    for color in colors:
        new_turtle = turtle.Turtle(shape='turtle')
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(-380, y)
        new_turtle.pendown()
        turtles.append(new_turtle)
        y  += 50
    return turtles

def race(turtles):
    race_on = True
    while race_on:
     for turtle in turtles:
            move_turtle(turtle)
            x =  turtle.xcor()
            if x  > 380:
                race_on = False
                winner = turtle.color()[0]
                break
    return winner
def main():
     turtle = setup_race()
     winner = race(turtle)
     print(f"The {winner} turtle wins!")
     turtle.done()

main()

