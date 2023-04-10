import customtkinter
import tkinter
import math
import time
from PIL import Image, ImageTk
import os 

class Animation(customtkinter.CTkFrame):
   def __init__(self, *args, header_name="Animation", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name
        canvas = customtkinter.CTkLabel(self, image=customtkinter.CTkImage(Image.open(os.path.join("C:\\git\\jumpy\\SolidWorksAnimation\\", "animation1-0000.png")), size=(100, 50)))
        canvas.grid(row=0, column=0, padx=10, pady=10)