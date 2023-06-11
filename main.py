from turtle import Screen
import pandas as pd
import turtle

data = pd.read_csv('50_states.csv')


# All U.S States
states = data.state.to_list()


screen = Screen()
screen.title('U.S. States Game ')


image_path = "blank_states_img.gif"

screen.addshape(image_path)
turtle.shape(image_path)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 State correct", prompt='Whats another state name?').title()

    if answer_state == "Exit":
        missing_state = []
        for state in states:
            if state not in guessed_states:
                missing_state.append(state)

        new_data_frame = pd.DataFrame(missing_state)
        new_data_frame.to_csv('missing_states.csv')
        break

    # Check if the answer_state is one of the columns in the data states
    if answer_state in states:
        state_row = data[data.state == answer_state]
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_row.x), int(state_row.y))
        t.write(state_row.state.item())
    # If they got it right:
    # Create a turtle to right the answer state

turtle.mainloop()

screen.exitonclick()
