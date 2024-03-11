import time
import os
import subprocess
import PySimpleGUI as sg
import platform

# Function to play the beep sound
def play_beep():
    sound_path = os.path.join(os.path.dirname(__file__), "complete.oga")

    # Check the platform and use the appropriate command to play the sound
    if platform.system() == "Windows":
        # Windows command using the start command to play the sound
        subprocess.Popen(["start", "/min", "mplay32", "/play", sound_path], shell=True)
    elif platform.system() == "Darwin":  # macOS
        subprocess.Popen(["afplay", sound_path])
    else:  # Assume Unix-based systems, will work for distribution that uses pulseaudio
        subprocess.Popen(["paplay", sound_path])

# Timer function
def timer():

# Theme
sg.theme('DarkTanBlue')   # Add a touch of color

# GUI Layout
layout = [
    [sg.Text("=_T I M E R_=", justification='center',size=(55,1))],
    [sg.Button("Start")],
    [sg.Button("Stop")],
    [sg.Button("Pause")],
    [sg.Text(size=(30, 2), key="-OUTPUT-")]  # Element to display countdown status
]

# Create the window and set resizable attribute to True
window = sg.Window("PomoTimer", layout, size=(250, 200), resizable=True)

