from builtins import str
from tkinter import DISABLED
from turtle import window_height

import customtkinter as customtkinter
import os 
from PIL import Image
import asyncio
from bleak import BleakScanner, BleakClient, discover
import threading
import animationv4
import time
import logging
import BluetoothUI



logging.basicConfig(level=logging.DEBUG, filename='UI.log',format='%(asctime)s:%(levelname)s:%(message)s')

device_address = "94:A9:A8:3A:52:90"
CHARACTERISTIC_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"
message = 's'
stop = 'e'
label_text = "Bienvenue "
device_list = []
combo_box_values = []





def setlabel():
   for thread in threading.enumerate(): 
    print(thread.name)



class MotorPanel(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="Motor Panel", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name

        self.header = customtkinter.CTkLabel(self, text=self.header_name, font=("Helvetica", 16, "bold"))
        self.header.grid(row=0, column=0, padx=10, pady=10)


        self.speed_label = customtkinter.CTkLabel(self, text="Motor Speed:", )
        self.speed_label.grid(row=1, column=0, padx=10, pady=10)

        self.torque_label =customtkinter.CTkLabel(self, text="Motor Torque:")
        self.torque_label.grid(row=2, column=0, padx=10, pady=10)
    
    def set_torque(self, torque):
        self.torque_label.configure(text= "Motor Speed: "+ str(torque))

    def set_speed(self, speed):
        self.speed_label.configure(text= "Motor speed:" + str(speed))
        

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        current_thread = threading.current_thread()
        print("Current Thread: {}".format(current_thread.name))
        # load images 
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo-color.png")), size=(100, 50))
        self.robot_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "robot.png")), size=(250, 250))


        self.title("Bluetooth Application")
        self.geometry("700x450")
        self.iconbitmap(os.path.join(image_path, "logo.ico"))

        button_font = customtkinter.CTkFont(family="Arial", size=20)	
        label_font = customtkinter.CTkFont(family="Arial", size=20)


        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

       
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0, )
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(2, weight=1)



        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" jumpy",
                                                             compound="left", font=button_font)
        
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"))
                                                   
        self.home_button.grid(row=1, column=0, sticky="ew")


        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")


        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, bg_color="gray20")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_rowconfigure(2, weight=1)

        self.motor_panel = MotorPanel(self.navigation_frame)
        self.motor_panel.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        self.motor_panel.set_speed(0)

        

        self.jump_button = customtkinter.CTkButton(self.home_frame, text="JUMP",font=button_font, compound="bottom", height=60, width=200, state="disabled",
                                                   command=lambda: threading.Thread(target=BluetoothUI.connect_to_device_async, args=(self,'j',)).start()) ## Pour commencer un thread ne pas mettre () après la fonction
        self.jump_button_left = customtkinter.CTkButton(self.home_frame, text="JUMP LEFT",font=button_font, compound="bottom", height=60, width=200, state="disabled",
                                                   command=lambda: threading.Thread(target=BluetoothUI.connect_to_device_async, args=(self,'l',)).start())
        self.jump_button_right = customtkinter.CTkButton(self.home_frame, text="JUMP RIGHT",font=button_font, compound="bottom", height=60, width=200, state="disabled",
                                                   command=lambda: threading.Thread(target=BluetoothUI.connect_to_device_async, args=(self,'r',)).start())
        self.stop_button = customtkinter.CTkButton(self.home_frame, text="STOP",font=button_font, compound="bottom", height=60, width=200, state="normal",
                                                   command=lambda: threading.Thread(target=BluetoothUI.connect_to_device_async, args=(self,'s',)).start())
        self.jump_button.grid(row=0, column=1, padx=40, pady=20)
        self.jump_button_left.grid(row=0, column=0, padx=40, pady=20)
        self.jump_button_right.grid(row=0, column=2, padx=40, pady=20)
        self.stop_button.grid(row=1, column=1, padx=40, pady=20)

        self.read_button = customtkinter.CTkButton(self.home_frame, text="READ",font=button_font, compound="bottom", height=60, width=200, 
                                                   command=lambda: threading.Thread(target=BluetoothUI.read_device_async, args=(self,)).start())
        self.read_button.grid(row=1, column=2, padx=40, pady=20)


        self.find_button = customtkinter.CTkButton(self.home_frame, text="Scan", font=button_font, compound="bottom", height=60, width=200, 
                                                   command=lambda: BluetoothUI.thread_scan_devices(self, device_list)) #mettre une virgule après args sinon ça ne marche pas
        self.find_button.grid(row=1, column=0, padx=40, pady=20)
     
        self.label_avertissement = customtkinter.CTkLabel(self.home_frame, text=label_text, font=label_font)
        self.label_avertissement.grid(row=2, column=1, padx=20, pady=20)

        self.combobox = customtkinter.CTkComboBox(self.home_frame)
        self.combobox.grid(row=3, column=1, padx=20, pady=20)
    
   
        self.home_frame.grid(row=0, column=1, sticky="nsew")
        

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

 


if __name__ == "__main__":
    app = App()
    app.mainloop()
    


    

