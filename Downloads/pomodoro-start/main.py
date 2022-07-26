from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark = "✔"
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global checkmark
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark=""
    check_label.config(text=checkmark)
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    global checkmark

    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    reps += 1
    if reps % 8:
        if reps % 2 == 1:
            countdown(work_sec)
            timer_label.config(text="Work time", fg=GREEN)
        elif reps % 2 == 0:
            check_label.config(text=checkmark)
            checkmark += "✔"
            countdown(short_break_sec)
            timer_label.config(text="Quick break", fg=PINK)
    else:
        check_label.config(text=checkmark)
        checkmark += "✔"
        countdown(long_break_sec)
        timer_label.config(text="Long break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if 0 <= count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="/Users/HP/Downloads/pomodoro-start/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# "timer" label
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# "check" label
check_label = Label(font=(FONT_NAME, 18), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

# start button
button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

# reset button
button_reset = Button(text="Reset", highlightthickness=0, command = reset)
button_reset.grid(column=2, row=2)












window.mainloop()