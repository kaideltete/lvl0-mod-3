import random
import turtle
from tkinter import simpledialog
import random
# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    my_turtle = turtle.Turtle()
    my_turtle.shape("turtle")
    for i in range(1000):
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
        my_turtle.speed(2)
        my_turtle.color('green')
        my_turtle.pencolor('blue')
        for i in range(4):
            my_turtle.forward(100)
            my_turtle.left(90)
    #      3) Set the pen width to 10
        my_turtle.width(10)
    #      4) Ask the user what color pen they would like to draw with
        col_1= simpledialog.askstring(title='enter a color', prompt="enter color corectly")
    #      5) Use an if/else statement to set the pen color that the user
    #         requested

        my_turtle.pencolor(col_1)



    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them
        for i in range(4):
            my_turtle.forward(100)
            my_turtle.left(90)
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
