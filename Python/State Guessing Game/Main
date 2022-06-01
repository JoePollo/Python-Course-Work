import turtle
import pandas
import screen_printer
import sys

GAME_IS_ON = True
user_score = 0
screen = turtle.Screen()
screen.title("US States Game")
states_map = "blank_states_img.gif"
screen.addshape(states_map)
turtle.shape(states_map)
states_df = pandas.read_csv("50_states.csv")
states_list = states_df["state"].tolist()
writey_boi = screen_printer.Screen_Writer()
while GAME_IS_ON == True:
    while user_score < 50:
        answer_state = screen.textinput(title = f"{user_score}/50 States Correct", prompt = "Guess a State:")
        answer_state = answer_state.capitalize()
        if answer_state in states_list:
            correct_state = states_df[states_df["state"] == answer_state]
            writey_boi.correct_answer(x = int(correct_state["x"]), y = int(correct_state["y"]), state = answer_state)
            states_list.remove(answer_state)
            user_score += 1
        if user_score == 50:
            writey_boi.winner()
        if answer_state == "Exit":
            missed_states_df = pandas.DataFrame(states_list)
            missed_states_df.to_csv("Missed States.csv")
            sys.exit()
    screen.mainloop()
