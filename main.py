import tkinter as tk
from tkinter import ttk
import pyttsx3
import sv_ttk

# Initialize the main window
# Center the window on the screen
window_width = 400
window_height = 600
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.title("Text-to-Speech")

# Function to speak the entered text
def on_button_click():
    engine = pyttsx3.init("sapi5")  # Use SAPI5 for Windows
    engine.setProperty('rate', speed.get())  # Set the speech rate from the slider
    engine.say(entry.get())
    engine.runAndWait()

# Function to save the spoken text to a file
def save():
    engine = pyttsx3.init()
    engine.save_to_file(entry.get(), filename.get() + ".mp3")
    engine.runAndWait()

# Entry field for the text to be spoken
entry = ttk.Entry(root, width=50)
entry.pack(pady=10)
# Slider to adjust the speech rate
speed = ttk.Scale(root, from_=50, to=300, orient='horizontal', length=300)
speed.pack(pady=10)
# Label for the slider
speed_label = ttk.Label(root, text="Speech Rate (words per minute):")
speed_label.pack(pady=5)

# Button to speak the text
say_button = ttk.Button(root, text="Say", command=on_button_click)
say_button.pack(pady=5)

# Entry field for the filename
filename = ttk.Entry(root, width=50)
filename.pack(pady=10)

# Button to save the audio to a file
save_button = ttk.Button(root, text="Save", command=save)
save_button.pack(pady=5)

# Set the theme to dark
sv_ttk.set_theme("dark")

# Start the main event loop
root.mainloop()
