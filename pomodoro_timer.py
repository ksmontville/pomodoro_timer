from tkinter import *
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
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='POMODORO', fg=GREEN)
    checkmark_label['text'] = ''


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count = 60 * LONG_BREAK_MIN
        timer_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count = 60 * SHORT_BREAK_MIN
        timer_label.config(text="BREAK", fg=PINK)
    else:
        count = 60 * WORK_MIN
        timer_label.config(text='POMODORO', fg=GREEN)

    count_down(count)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count // 60
    count_sec = count % 60

    if count_min < 10:
        count_min = f'0{count_min}'

    if count_sec == 0:
        count_sec = '00'
    elif count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 != 0:
            checkmark_label.config(text=f"{checkmark_label['text']} {check_mark}")
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.minsize(width=500, height=400)
window.config(padx=100, pady=25, bg=YELLOW)

check_mark = "✔"
tomato_img = PhotoImage(file='tomato.png')
check_img = PhotoImage(file='check_mark.png')

# Timer label
timer_label = Label()
timer_label.config(text='POMODORO', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, 'bold'), highlightthickness=0)
timer_label.grid(row=0, column=1)

# Canvas with image and timer text
canvas = Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 115, image=tomato_img)
timer_text = canvas.create_text(100, 130, font=(FONT_NAME, 30, 'bold'), text='00:00', fill='white')
canvas.grid(row=1, column=1)

# Start button
start_button = Button()
start_button.config(command=start_timer, text='START', font=(FONT_NAME, 10),
                    bg='white', fg=PINK, relief='groove', highlightthickness=0)

start_button.grid(row=2, column=0)

# Reset button
reset_button = Button()
reset_button.config(command=reset_timer, text='RESET', font=(FONT_NAME, 10),
                    bg='white', fg=PINK, relief='groove', highlightthickness=0)
reset_button.grid(row=2, column=2)

# Checkboxes
checkmark_label = Label()
checkmark_label.config(padx=10, pady=10, text='', font=(FONT_NAME, 12), fg=GREEN, bg=YELLOW, highlightthickness=0)
checkmark_label.grid(row=3, column=1)


window.mainloop()
