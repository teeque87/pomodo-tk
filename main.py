import customtkinter as ctk
from tkinter import Frame
# Constants
DEFAULT_TIMER = 1800

# Global variables
timer_in_seconds = DEFAULT_TIMER
running = False
timer_job = None

# Set appearance and theme
ctk.set_appearance_mode("dark")


def timer_toggle():
    """Toggle the timer between running and paused states."""
    global running, timer_job
    running = not running
    if running:
        button.configure(text="Pause")
        update_timer()
        timer_label.configure(text_color="#adff2f")
    else:
        button.configure(text="Start")
        timer_label.configure(text_color="white")
        if timer_job:
            root.after_cancel(timer_job)


def reset_timer():
    """Reset the timer to the default state."""
    global timer_in_seconds, running
    timer_in_seconds = DEFAULT_TIMER
    running = False
    update_timer_display(timer_in_seconds)
    timer_label.configure(text_color="white")
    button.configure(text="Start")


def update_timer():
    """Update the timer countdown if running, otherwise stop."""
    global timer_in_seconds, running, timer_job
    if running and timer_in_seconds > 0:
        timer_in_seconds -= 1
        update_timer_display(timer_in_seconds)
        timer_job = root.after(1000, update_timer)
    elif timer_in_seconds == 0:
        running = False
        button.configure(text="Start")


def update_timer_display(timer):
    """Convert the timer into a string and update the label."""
    time_string = resolve_time_to_string(timer)
    timer_label.configure(text=time_string)


def resolve_time_to_string(timer):
    """Convert time in seconds to a formatted string (MM:SS)."""
    minutes = timer // 60
    seconds = timer % 60
    return f"{minutes:02d}:{seconds:02d}"


# Main application window setup
root = ctk.CTk()
root.title("Pomodoro App")
root.geometry("300x300")
root.resizable(0, 0)

# Add Frame
bottom = Frame(root, background="#26242f")
bottom.pack(side="bottom", fill="both", expand=True)

# Timer Label
timer_label = ctk.CTkLabel(root, text=resolve_time_to_string(timer_in_seconds), font=(None, 48))
timer_label.pack(side="top", anchor="center", pady=100)

# Start/Pause Button
button = ctk.CTkButton(bottom, text="Start", command=timer_toggle, corner_radius=0)
button.pack(side="left", fill="both")

# Reset Button
button_reset = ctk.CTkButton(bottom, text="Reset", command=reset_timer, corner_radius=0, fg_color="#AA0000", hover_color="red")
button_reset.pack(side="right", fill="both")



# Start the Tkinter event loop
root.mainloop()