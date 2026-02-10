import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "C:\\Users\\Home\\Desktop\\Python Project (100 days of python with Angela Yu)\\Python-Project-100-days-of-python-with-Angela-Yu-\\Day25\\blank_states_img.gif"

screen.bgpic(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

states_data = pd.read_csv("C:\\Users\\Home\\Desktop\\Python Project (100 days of python with Angela Yu)\\Python-Project-100-days-of-python-with-Angela-Yu-\\Day25\\50_states.csv")
states_data.state = states_data.state.str.lower()

all_states = states_data.state.to_list()

guessed_states = []

correct_answer = 0

messsage = turtle.Turtle()
messsage.hideturtle()
messsage.penup()
messsage.goto(0, 300)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{correct_answer} States Correct, {len(guessed_states)}/50 Number Of Guess", prompt = "What's another state's name?")

    if answer_state is None:
        break

    answer_state = answer_state.strip().lower()

    if answer_state == "exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        missing_states_data = pd.DataFrame(missing_states)
        missing_states_data.to_csv("missing_states.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        correct_answer += 1

        state_row = states_data[states_data.state == answer_state]
        writer.goto(int(state_row.iloc[0].x), int(state_row.iloc[0].y))
        writer.write(answer_state.title())

    elif answer_state in guessed_states:
        messsage.clear()
        messsage.write("You already guessed that state, try again!", align = "center", font = ("Arial", 16, "normal"))

    else:
        messsage.clear()
        messsage.write("Wrong answer, try again!", align = "center", font = ("Arial", 16, "normal"))
