import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
guessed_states = []
turtle.shape(image)
scribe = turtle.Turtle()
scribe.hideturtle()
scribe.penup()

state_data = pandas.read_csv("50_states.csv")
list_of_states = state_data.state.to_list()
remaining_states = list_of_states

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 Correct States", prompt="What's another state?").title()

    if answer == "Exit":
        print(remaining_states)
        new_data = pandas.DataFrame(remaining_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in list_of_states:
        guessed_states.append(answer)
        remaining_states.remove(answer)
        answer_data = state_data[state_data.state == answer]
        scribe.goto(answer_data.x.item(), answer_data.y.item())
        scribe.write(answer)
