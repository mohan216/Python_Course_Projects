import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    start.config(state=DISABLED)
    print('hi')
    if REPS == 0 or REPS == 2 or REPS == 4:
        count_down(WORK_MIN)
        REPS += 1
        return
    if REPS == 1 or REPS == 3 or REPS == 5:
        count_down(SHORT_BREAK_MIN)
        REPS += 1
        return
    if REPS > 5:
        count_down(LONG_BREAK_MIN)
        REPS = 0
        return


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(value):
    # seconds = 25 * 60
    # timer_value = seconds
    # value = WORK_MIN
    canvas.itemconfig(timer_value, text=value)
    if (value > 0):
        window.after(1000, count_down, value - 1)
        # value = value - 1
        # time.sleep(1)
        # count_down(value)
    else:
        print('bye')
        start.config(state=NORMAL)
        print('next')


# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

img1 = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img1)
timer_value = canvas.create_text(100, 128, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer = Label(text="TIMER")
timer.grid(column=1, row=0)

start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

end = Button(text="end")
end.grid(column=2, row=2)

check = Label(text="checkbox")
check.grid(column=1, row=4)

window.mainloop()
