import random
from turtle import Turtle,Screen
screen = Screen()
screen.setup(500,400)
user_choice = screen.textinput("Go by your own power: ","who will win? ")
screen.listen()
colors = ["red", "yellow", "purple", "green", "pink", "blue"]
all_turtle = []
degrees = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(-230, y=degrees[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtle.append(new_turtle)
on = False
if user_choice:
    on = True

while on:
    for key in all_turtle:
        if key.xcor() >230:
            winner_color = key.pencolor()
            if winner_color == user_choice:
                print(f"your are winner {winner_color}")
                on = False
            else:
                print(f"you loose the winner is {winner_color}")
                on = False
        rand = random.randint(0, 10)
        key.forward(rand)
screen.exitonclick()

