import customtkinter
import tkinter
import math
import time
from PIL import Image, ImageTk
import os
import sys
sys.setrecursionlimit(20000)

class Animation(customtkinter.CTkFrame):
   def __init__(self, *args, header_name="Animation",**kwargs):
        super().__init__(*args, **kwargs)
        self.fps_idle = 500
        self.bool = 0
        self.fps_jump = 500
        self.num_frames_jump = 480
        self.num_frames_idle = 1140
        self.size_x = 550
        self.size_y = 550
        self.frame_prefix_idle = "idle-"
        self.frame_prefix_jump = "jump-"
        self.folder_name = "C:\\git\\jumpy\\SolidWorksAnimation\\"
        self.frame_type = "000"
        self.header_name = header_name

        # Load and store all frames in a dictionary
        self.frames = {}
        for i in range(1,self.num_frames_jump + 1):
        #self.num_frames_jump + 1
            if i <= 9:
                self.frame_type = "000"
            elif i <= 99 and i >= 10:
                self.frame_type = "00"
            elif i >= 100 and i <= 999:
                self.frame_type = 0
            elif i >= 1000:
                self.frame_type = ''

            filename = os.path.join(f"{self.folder_name}{self.frame_prefix_jump}{self.frame_type}{i}.png")
            image = Image.open(filename).resize((self.size_x, self.size_y), resample=Image.LANCZOS)
            self.frames[i] = ImageTk.PhotoImage(image)
        print("dic1 is finished")
        for i in range(1, self.num_frames_idle + 1):
        #self.num_frames_idle + 1
            if i <= 9:
                self.frame_type = "000"
            elif i <= 99 and i >= 10:
                self.frame_type = "00"
            elif i >= 100 and i <= 999:
                self.frame_type = 0
            elif i >= 1000:
                self.frame_type = ''

            filename = os.path.join(f"{self.folder_name}{self.frame_prefix_idle}{self.frame_type}{i}.png")
            image = Image.open(filename).resize((self.size_x, self.size_y), resample=Image.LANCZOS)
            self.frames[i + self.num_frames_jump] = ImageTk.PhotoImage(image)

        print("dic2 is finished")
        self.frame_type = "000"
        self.frame_num = 1
        self.canvas = customtkinter.CTkLabel(self, image=customtkinter.CTkImage(Image.open(os.path.join(f"{self.folder_name}{self.frame_prefix_idle}{self.frame_type}{self.frame_num}.png")), size=(self.size_x, self.size_y)))
        self.canvas.configure(text="")
        self.canvas.grid(row=0, column=0, padx=10, pady=10)

   def change(self):
       self.update_frame(1)

   def start(self):

       self.update_frame(0)

   def boolean(self):
       self.bool = 1
       print("jai change la valeur de bool à 1!")
   def boolean_false(self):
       self.bool = 0
       print("jai change la valeur de bool à 0!")
   def idle(self):

       fps = self.fps_idle
       num_frames = self.num_frames_idle

       i = 1
       while 1:

           if i > self.num_frames_idle:
               i = 1

           new_tk_image = self.frames[i + self.num_frames_jump]
           self.canvas.configure(image=new_tk_image)
           self.canvas.image = new_tk_image
           self.canvas.after(int(1000 / fps))
           i += 1
           print("je suis juste avant le if bool")
           # print(self.bool)
           if self.bool == 1:
               print("je suis dans le break")
               break
       print("j'ai réussi a break!")

   def jump(self):

       fps = self.fps_jump
       num_frames = self.num_frames_jump

       for i in range(1, num_frames):
           new_tk_image = self.frames[i]
           self.canvas.configure(image=new_tk_image)
           self.canvas.image = new_tk_image
           self.canvas.after(int(1000 / fps))
       print("j'ai finis de jump")
       Animation.idle(self)