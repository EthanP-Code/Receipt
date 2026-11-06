# navigator.py

import tkinter as tk

# Window configurations
TITLE = "Receipt Processor"
W_SIZE = "400x300"
BG_COLOR = "#1E1E1E"
TEXT_COLOR = "#FFFFFF"
FONT = "Courier"
CURSOR_COLOR = "white"

# Text options
START_PROMPT = "[1] Browse images\n> "

def route_input(event):
    raw_input = event.widget.get("1.0", "end-1c")
    user_input = raw_input.strip()
    print(user_input)

def launch_nav():
    
    # 1. Initialize the main window constructor
    root = tk.Tk()
    root.title(TITLE)
    root.geometry(W_SIZE) 

    # 2. Initialize the text constructor
    nav_display = tk.Text(root, bg=BG_COLOR, fg=TEXT_COLOR, 
                          insertbackground=CURSOR_COLOR, font=(FONT, 12))

    # 3. Mount text widget to window dynamically
    nav_display.pack(expand=True, fill="both")

    # 4. Initialize the baseline UX state
    nav_display.insert("1.0", START_PROMPT)
    nav_display.focus_set() # automatic cursor into window

    # 5. Route input
    nav_display.bind("<Return>", route_input)

    # 6. Start the application's event loop
    root.mainloop()


if __name__ == "__main__":
    launch_nav()

