import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
# Bring the image in the folder into the code and use to set the shape
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# store the data into csv using pandas
data = pd.read_csv("50_states.csv")
states = data.state.to_list()

missing_states = []
guess_states = []

while len(guess_states) < 50:
    # ask the user for a guess and title the input such that it has first letter capitalize
    answer_state = screen.textinput(title=f"{len(guess_states)}/5 States Correct", prompt="what's another state's name?").title()
    if answer_state == "Exit":
        for state in states:
            if state not in guess_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("Learn_states.csv")

        break
    elif answer_state in guess_states:
        print("Answer Already Typed")

    elif answer_state in states:
        guess_states.append(answer_state)
        pen = turtle.Turtle()
        state_data = data[data.state == answer_state]
        pen.hideturtle()
        pen.penup()
        pen.goto(int(state_data.x), int(state_data.y))
        pen.write(answer_state)

# Generate the list of state not stated




