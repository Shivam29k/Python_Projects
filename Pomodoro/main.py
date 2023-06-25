from tkinter import *
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
checkmarks =  ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer, reps, checkmarks
    window.after_cancel(timer)
    reps = 0
    checkmarks = ""
    check_marks.config(text=checkmarks)
    txt.config(text="   Timer   ")
    canvas.itemconfig(timer_text, text=f"00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    print(reps)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps%8 == 0:
        check_update()
        txt.config(text="Long Break ", fg=RED)
        count_down(long_break_sec)
    elif reps%2 == 0:
        check_update()
        txt.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    else:
        txt.config(text="    Work   ", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = int(math.floor(count/60))
    count_sec = int(count % 60)
    if count_sec<10:
        count_sec = f"0{int(count_sec)}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
   
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



# setting tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)



# Timer txt
txt = Label(text="   Timer   ", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
txt.grid(column=1, row=0)

# buttons
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command= reset_timer)
reset.grid(column=2, row=2)

# Check marks
check_marks = Label(text="", fg=GREEN, bg=YELLOW , font=(FONT_NAME, 10, "bold"))
check_marks.grid(column=1, row=3)
def check_update():
    global checkmarks
    checkmarks += "✔️"
    check_marks.config(text=checkmarks)

window.mainloop()