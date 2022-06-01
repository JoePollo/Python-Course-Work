from tkinter import *
from tkinter.ttk import *
import datetime

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 1
WORK_REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global REPS
    global WORK_REPS
    REPS = 1
    WORK_REPS = 0
    mainapp.after_cancel(TIMER)
    checkmark_label.config(text = "")
    tomato_canvas.itemconfig(timer_text, text = "0:00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer():
    global REPS
    global WORK_REPS
    if REPS == 8:
        REPS = 0
        WORK_REPS = 0
        count_down(LONG_BREAK_MIN * 60)
        task_label.config(text = "Long break!", foreground = RED, font = (FONT_NAME, 35, "bold"))
        checkmark_label.config(text = "")
    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        task_label.config(text = "Short break!", foreground = PINK, font = (FONT_NAME, 35, "bold"))
        WORK_REPS += 1
        if WORK_REPS == 1:
            checkmark_label.config(text = "✔")
        elif WORK_REPS == 2:
            checkmark_label.config(text = "✔✔")
        elif WORK_REPS == 3:
            checkmark_label.config(text = "✔✔✔")
    else:
        count_down(WORK_MIN * 60)
        task_label.config(text = "WORK", foreground = RED, font = (FONT_NAME, 35, "bold"))
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global REPS
    global TIMER
    time = datetime.timedelta(seconds = count)
    tomato_canvas.itemconfig(timer_text, text = f"{time}")
    if count > 0:
        TIMER = mainapp.after(1000, count_down, count-1)
    elif count == 0 and REPS < 8:
        REPS += 1
        timer()
# ---------------------------- UI SETUP ------------------------------- #
mainapp = Tk()
mainapp.title("Pomodoro")
mainapp.config(padx = 100, pady = 50, bg = YELLOW)

task_label = Label(text = "", background = YELLOW)
task_label.grid(row = 0, column = 1)

timer_label = Label(text = "Timer", background = YELLOW, foreground = GREEN, font = (FONT_NAME, 35, "bold"))
timer_label.grid(row = 1, column = 1)

tomato_canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = "tomato.png")
tomato_canvas.create_image(100, 112, image = tomato_img)
timer_text = tomato_canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
tomato_canvas.grid(row = 2, column = 1)

start_button = Button(text = "Start", command = timer)
start_button.grid(row = 3, column = 0)

checkmark_label = Label(background = YELLOW, foreground = GREEN, font = (FONT_NAME, 15, "bold"), padding = 5)
checkmark_label.grid(row = 3, column = 1)

reset_button = Button(text = "Reset", command = reset)
reset_button.grid(row = 3, column = 2)


mainapp.mainloop()