import turtle
import pandas

screen = turtle.Screen()
screen.title("US states game")
image = "/Users/HP/Downloads/us-states-game-start/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_guesses = []
score = 0


while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 states", prompt="What's another state's name?")

    states = pandas.read_csv("/Users/HP/Downloads/us-states-game-start/us-states-game-start/50_states.csv")
    states_list = states["state"].to_list()

    if answer_state.title() == 'End':
        break

    for state in states_list:
        if answer_state.title() == state:
            correct_answer = states[states.state == state]
            ans_xcor = int(correct_answer.x)
            ans_ycor = int(correct_answer.y)

            tu = turtle.Turtle()
            tu.up()
            tu.hideturtle()
            tu.goto(ans_xcor, ans_ycor)
            tu.write(state)

            if answer_state in correct_guesses:
                pass
            else:
                correct_guesses.append(answer_state.title())
                score = len(correct_guesses)


# missed_states_list = []
# for states in states_list:
#     if states not in correct_guesses:
#         missed_states_list.append(states)

missed_states_list = [states for states in states_list if states not in correct_guesses]
print(missed_states_list)
missed_states = pandas.DataFrame(missed_states_list)
missed_states.to_csv("missed_states.csv")


#TODO 1: CONVERT THE GUESS TO TITLE CASE %
#TODO 2: CHECK IF THE GUESS IS AMONG THE 50 STATES
#TODO 3: WRITE CORRECT GUESSES ONTO THE MAP
#TODO 4: USE A LOOP TO ALLOW THE USER KEEP GUESSING
#TODO 5: RECORD THE CORRECT GUESSES IN A LIST
#TODO 6: KEEP TRACK OF THE SCORE

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#

#turtle.mainloop()


