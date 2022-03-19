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
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def resetTimer():
    window.after_cancel(timer)
    canvas.itemconfig(timerText, text=f"00:00")
    workLabel.config(text="Timer", fg=GREEN)
    checkLabel.config(text="")
    global reps
    reps = 0
    startButton.config(state="normal")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def startTimer():
    global reps
    reps += 1
    workSec = WORK_MIN * 60
    shortBreakSec = SHORT_BREAK_MIN * 60
    longBreakSec = LONG_BREAK_MIN * 60
    startButton.config(state="disabled")

    if reps % 2 == 1:
        workLabel.config(text="Work", fg=GREEN)
        countDown(workSec)
    elif reps % 8 == 0:
        countDown(longBreakSec)
        workLabel.config(text="Long Break", fg=RED)
    else:
        countDown(shortBreakSec)
        workLabel.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countDown(count):

    countMin = math.floor(count / 60)
    if countMin < 10:
        countMin = f"0{countMin}"
    countSec = count % 60
    if countSec < 10:
        countSec = f"0{countSec}"

    canvas.itemconfig(timerText, text=f"{countMin}:{countSec}")
    if count > 0:
        global timer
        timer = window.after(1000, countDown, count - 1)
    else:
        startTimer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        checkLabel.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)




canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomatoImg)
timerText = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)



workLabel = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
workLabel.grid(column=1, row=0)
checkLabel = Label(font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
checkLabel.grid(column=1, row=3)


startButton = Button(text="Start", command=startTimer)
startButton.grid(column=0, row=2)

resetButton = Button(text="Reset", command=resetTimer)
resetButton.grid(column=2, row=2)



window.mainloop()