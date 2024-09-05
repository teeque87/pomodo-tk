import customtkinter as ctk
import time

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

DEFAULT_TIMER = 3600
timer_in_seconds = 3600
running = False
timer_job = None


def timer_toggle():
    global running, timer_job
    running = not running
    if running:
        button.configure(text="Pause")
        update_label()
    else:
        button.configure(text="Start")
        if timer_job:
            root.after_cancel(timer_job)

def reset_timer():
    global timer_in_seconds, DEFAULT_TIMER, running
    timer_in_seconds = DEFAULT_TIMER
    running = False
    time_string = resolve_time_to_string(timer_in_seconds)
    timer_label.configure(text=time_string)
    button.configure(text="Start")

def update_label():
    global timer_in_seconds, running, timer_job
    if running and timer_in_seconds > 0:
        timer_in_seconds -= 1
        time_string = resolve_time_to_string(timer_in_seconds)
        timer_label.configure(text=time_string)
        timer_job = root.after(1000, update_label)
    elif timer == 0:
        running = False
        button.configure(text="Start")

def resolve_time_to_string(timer):
    minutes = int(timer / 60)
    seconds = int(timer % 60)
    return f"{minutes:02d}:{seconds:02d}"

root = ctk.CTk()

root.title("Pomodoro App")
root.geometry("300x300")
root.resizable(0,0)

for i in range(3):
    root.columnconfigure(i, weight=1)
root.rowconfigure(1, weight=1)

timer = resolve_time_to_string(timer_in_seconds)

timer_label = ctk.CTkLabel(root, text=timer, font=(None, 40))
button = ctk.CTkButton(root, text="Start", command=timer_toggle, corner_radius=0)
button_reset = ctk.CTkButton(root, text="Reset", command=reset_timer, corner_radius=0)
timer_label.grid(row=1, column=1, padx=0, pady=0)
button.grid(row=2, column=1, padx=5, pady=0)
button_reset.grid(row=3, column=1, pady=10)

root.mainloop()

