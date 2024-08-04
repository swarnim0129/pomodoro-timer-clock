from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_button():
    window.after_cancel(timer)
    canvas.itemconfig(timer_canvas, text="00:00")
    text_Label.config(text="Timer", bg=YELLOW, fg=GREEN)
    tick_mark_label.config(text="")
    start_btn.config(state="normal")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 3  # converts mins into seconds so that it can be formatted
    short_break_sec = SHORT_BREAK_MIN * 3
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:  # rep 8 for long break
        count_down(long_break_sec)
        text_Label.config(text="Long Break", fg=RED, bg=YELLOW)
        start_btn.config(state="disabled")

    elif reps % 2 == 0:  # even number of reps for short min breaks
        count_down(short_break_sec)
        text_Label.config(text="Break", fg=PINK, bg=YELLOW)
        start_btn.config(state="disabled")

    else:
        count_down(work_sec)  # odd number of reps for work
        text_Label.config(text="Work", fg=GREEN, bg=YELLOW)
        start_btn.config(state="disabled")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)  # to get into mins format
    count_sec = count % 60  # the remainder will be the seconds
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_canvas, text=f'{count_min}:{count_sec}')

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        tick_mark = ""
        for _ in range(math.floor(reps / 2)):
            tick_mark += "✔"
        tick_mark_label.config(text=tick_mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

text_Label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 38, "bold"))
text_Label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)  # half of the width and half of the height
timer_canvas = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

stop_btn = Button(text="Stop", highlightthickness=0, command=reset_button)
stop_btn.grid(column=2, row=2)

tick_mark_label = Label(fg=GREEN, bg=YELLOW)
tick_mark_label.grid(column=1, row=3)
window.mainloop()
