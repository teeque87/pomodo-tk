import customtkinter as ctk

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
    else:
        button.configure(text="Start")
        if timer_job:
            root.after_cancel(timer_job)


def reset_timer():
    """Reset the timer to the default state."""
    global timer_in_seconds, running
    timer_in_seconds = DEFAULT_TIMER
    running = False
    update_timer_display(timer_in_seconds)
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

# Layout configuration
for i in range(3):
    root.columnconfigure(i, weight=1)
root.rowconfigure(1, weight=1)

# Timer Label
timer_label = ctk.CTkLabel(root, text=resolve_time_to_string(timer_in_seconds), font=(None, 40))
timer_label.grid(row=1, column=1, padx=0, pady=0)

# Start/Pause Button
button = ctk.CTkButton(root, text="Start", command=timer_toggle, corner_radius=0)
button.grid(row=2, column=1, padx=5, pady=0)

# Reset Button
button_reset = ctk.CTkButton(root, text="Reset", command=reset_timer, corner_radius=0, hover_color="red")
button_reset.grid(row=3, column=1, pady=10)

# Start the Tkinter event loop
root.mainloop()