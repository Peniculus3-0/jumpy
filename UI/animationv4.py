import customtkinter
import tkinter
import math
import time
from PIL import Image, ImageTk
import os 

class Animation(customtkinter.CTkFrame):
   def __init__(self, *args, header_name="Animation", fps=60, num_frames=300, frame_prefix="animation1-", **kwargs):
        super().__init__(*args, **kwargs)
        self.fps = fps
        self.num_frames = num_frames
        self.frame_prefix = frame_prefix
        self.folder_name = "C:\\git\\jumpy\\SolidWorksAnimation\\"
        self.header_name = header_name

        self.frame_type = "000"
        self.frame_num = 1
        self.size_x = 1800
        self.size_y = 500
        self.canvas = customtkinter.CTkLabel(self, image=customtkinter.CTkImage(Image.open(os.path.join(f"{self.folder_name}{self.frame_prefix}{self.frame_type}{self.frame_num}.png")), size=(self.size_x, self.size_y)))
        self.canvas.configure(text="")
        self.canvas.grid(row=0, column=0, padx=10, pady=10)

   def update_frame(self):
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

       new_image = Image.open(
           os.path.join(f"{self.folder_name}{self.frame_prefix}{self.frame_type}{self.frame_num}.png"))

       new_image = new_image.resize((self.size_x, self.size_y))

       new_tk_image = ImageTk.PhotoImage(new_image)

       self.canvas.configure(image=new_tk_image)
       self.canvas.image = new_tk_image

       self.canvas.after(int(1000 / self.fps), self.update_frame)

   def start(self):
       self.update_frame()

   def stop(self):
       self.root.after_cancel(self.update_frame)