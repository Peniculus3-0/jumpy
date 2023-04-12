import customtkinter
import tkinter
import math
import time
from PIL import Image, ImageTk
import os 

class Animation(customtkinter.CTkFrame):
   def __init__(self, *args, header_name="Animation",**kwargs):
        super().__init__(*args, **kwargs)
        self.fps_idle = 30
        self.fps_jump = 30
        self.num_frames_jump = 439
        self.num_frames_idle = 420
        self.frame_prefix_idle = "animation6-"
        self.frame_prefix_jump = "animation5-"
        self.folder_name = "C:\\git\\jumpy\\SolidWorksAnimation\\"
        self.header_name = header_name

        self.frame_type = "000"
        self.frame_num = 1
        self.size_x = 1500
        self.size_y = 800
        self.canvas = customtkinter.CTkLabel(self, image=customtkinter.CTkImage(Image.open(os.path.join(f"{self.folder_name}{self.frame_prefix_idle}{self.frame_type}{self.frame_num}.png")), size=(self.size_x, self.size_y)))
        self.canvas.configure(text="")
        self.canvas.grid(row=0, column=0, padx=10, pady=10)

        self.update_frame(0)

   def update_frame(self, num):

       if num == 1:
           frame_prefix = self.frame_prefix_jump
           fps = self.fps_jump
           num_frames = self.num_frames_jump
       elif num == 0:
           frame_prefix = self.frame_prefix_idle
           fps = self.fps_idle
           num_frames = self.num_frames_idle

       self.frame_num += 1

       if self.frame_num > num_frames:
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
           os.path.join(f"{self.folder_name}{frame_prefix}{self.frame_type}{self.frame_num}.png"))

       new_image = new_image.resize((self.size_x, self.size_y))

       new_tk_image = ImageTk.PhotoImage(new_image)

       self.canvas.configure(image=new_tk_image)
       self.canvas.image = new_tk_image

       self.canvas.after(int(1000 / fps), self.update_frame(num))

   def change(self):
       self.update_frame(1)
       self.canvas.after(1/(fps_jump/num_frames_jump),self.update_frame(0))

