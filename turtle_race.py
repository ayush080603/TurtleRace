from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Choose a turtle color", prompt="Enter a color (e.g., red, blue, green):").lower()
print(f"You chose: {user_bet}")
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

y_positions = [-70, -40, -10, 20, 50, 80] # Y positions for the turtles
turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")


    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()