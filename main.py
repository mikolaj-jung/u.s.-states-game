import turtle
import pandas
from state_text import StateText

# Screen settings - US map
screen = turtle.Screen()
screen.title("USA States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=730, height=500)

#Converting data from .csv file
data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()

game_over = False
score = 0

while not game_over:
    if score == 50:
        game_over = True

    guess = screen.textinput(prompt="Enter state name:", title=f"{score}/50 USA States")

    if guess == "" or guess is None:
        game_over = True
    else:
        guess = guess.title()

    if guess == "Exit":
        states_s = pandas.Series(states)
        states_s.to_csv("states_left.csv")
        game_over = True

    if guess in states:
        x_cor = data.loc[data["state"] == guess, "x"].values[0]
        y_cor = data.loc[data["state"] == guess, "y"].values[0]

        state = StateText()
        state.show_state(x_cor, y_cor, guess)

        score += 1

        states.remove(guess)

    else:
        continue