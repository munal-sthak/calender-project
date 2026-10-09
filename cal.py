import tkinter as tk
import time
import calendar
from datetime import datetime

window = tk.Tk()
window.title("Clock and Calendar")
window.geometry("400x450")
window.configure(bg="#1e1e2e")
window.resizable(False, False)

tk.Label(
    window,
    text="CLOCK & CALENDAR",
    font=("Arial", 18, "bold"),
    bg="#1e1e2e",
    fg="#89b4fa"
).pack(pady=15)

clock_label = tk.Label(
    window,
    font=("Arial", 36, "bold"),
    bg="#1e1e2e",
    fg="#a6e3a1"
)
clock_label.pack()

date_label = tk.Label(
    window,
    font=("Arial", 14),
    bg="#1e1e2e",
    fg="white"
)
date_label.pack(pady=5)

calendar_label = tk.Label(
    window,
    font=("Courier New", 13),
    bg="#1e1e2e",
    fg="#f9e2af",
    justify="left"
)
calendar_label.pack(pady=15)

def update_clock():
    now = datetime.now()

    clock_label.config(text=now.strftime("%I:%M:%S %p"))
    date_label.config(text=now.strftime("%A, %d %B %Y"))

    month_calendar = calendar.month(
        now.year, now.month
    )
    calendar_label.config(text=month_calendar)

    window.after(1000, update_clock)

update_clock()
window.mainloop()
