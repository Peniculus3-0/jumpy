import customtkinter as tk
import tkinter
import math
import time
from PIL import Image, ImageTk

class AnimationPlayer:
    def __init__(self, root, fps=30, num_frames=300, frame_prefix="animation1-"):
        self.root = root
        self.fps = fps
        self.num_frames = num_frames
        self.frame_prefix = frame_prefix
        self.folder_name = "C:\\git\\jumpy\\SolidWorksAnimation\\"

        # Load the first frame
        self.frame_type = "000"
        self.frame_num = 1
        self.frame_image = Image.open(f"{self.folder_name}{self.frame_prefix}{self.frame_type}{self.frame_num}.png")
        self.tk_image = ImageTk.PhotoImage(self.frame_image)

        # Create a label to display the frame
        root.after(500)
        self.label = tkinter.Label(self.root, image=self.tk_image)
        self.label.pack()

    def update_frame(self):
        # Load the next frame
        self.frame_num += 1

        if self.frame_num > self.num_frames:
            self.frame_num = 1

        if self.frame_num <= 9:
            self.frame_type = "000"
        elif self.frame_num <= 99 and self.frame_num >= 10:
            self.frame_type = "00"
        elif self.frame_num >= 100 and self.frame_num <= 999:
            self.frame_type = 0
        else:
            self.frame_type = ''

        self.frame_image = Image.open(f"{self.folder_name}{self.frame_prefix}{self.frame_type}{self.frame_num}.png")

        # Update the label with the new frame
        self.tk_image = ImageTk.PhotoImage(self.frame_image)
        self.label.configure(image=self.tk_image)

        # Schedule the next update
        self.root.after(int(1000 / self.fps), self.update_frame)

    def start(self):
        self.update_frame()

    def stop(self):
        self.root.after_cancel(self.update_frame)

# Create the root window
root = tk.CTk()

# Create the animation player
player = AnimationPlayer(root, fps=30, num_frames=300, frame_prefix="animation1-")

# Start the animation
player.start()

# Run the window
root.mainloop()