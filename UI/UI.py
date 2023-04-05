from builtins import str
from tkinter import DISABLED
from turtle import window_height

import customtkinter as customtkinter
import os 
from PIL import Image
import bluetooth
import asyncio
from bleak import BleakScanner, BleakClient, discover
import tkinter as tk
from tkinter import ttk
import threading
    
device_address = "94:A9:A8:3A:52:90"
CHARACTERISTIC_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"
message = 'N'
label_text = " "
class BLEScanner:
    def __init__(self, device_list):
        self.device_list = device_list
        
    async def scan_devices(self):
        devices = await discover()
        self.device_list.extend(devices)

async def start_scanning(device_list):
    print("start scanning")
    scanner = BLEScanner(device_list)
    await scanner.scan_devices()
    print("scan finished-----")
    
def on_scan_finished(device_list):
    print("Scan finished.")
    for dev in device_list:
        print("Device %s, name=%s " % (dev.address, dev.name))

def start_scanning_async(device_list):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_scanning(device_list))
    loop.close()
    on_scan_finished(device_list)

def connect_to_device_async(device_address):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_connecting(device_address))
    loop.close()

async def start_connecting(device_address):
    await connect_to_device(device_address)

async def connect_to_device(message):
    # print("Connecting to device")
    # async with BleakClient(device_address) as client:
    #     # do something with the client connection
    #     if client.is_connected:
    #         print(f"Connected to {device_address}")
    #         services = client.services
    #         print("Services:")
    #         for service in services:
    #             print(service)
            
    #         await client.write_gatt_char(CHARACTERISTIC_UUID, bytearray(message.encode()))
    #     else:
            app.label_avertissement.configure(text="Not Connected")
            




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Bluetooth Application")
        self.geometry("700x450")
        button_font = customtkinter.CTkFont(family="Arial", size=30, weight="bold")
        label_font = customtkinter.CTkFont(family="Arial", size=20)

        # set grid layout 1x2
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images 
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo-color.png")), size=(100, 50))

        # set icon
        self.iconbitmap(os.path.join(image_path, "logo.ico"))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0, )
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(2, weight=1)

         # create animation frame
        canvas = customtkinter.CTkCanvas(self, width=500, height=500, bg="white")
        canvas.grid(row=1, column=1, sticky="nsew")


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
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)



        # self.connect_button = customtkinter.CTkButton(self.home_frame, text="Connect", compound="right", command=lambda: threading.Thread(target=connect_to_device_async, args=(message)).start())
        # self.connect_button.grid(row=2, column=0, padx=20, pady=10)
       

        self.jump_button = customtkinter.CTkButton(self.home_frame, text="JUMP",font=button_font, compound="bottom", height=60, width=200, command=lambda: threading.Thread(target=connect_to_device_async, args=(message)).start())
        self.jump_button.grid(row=4, column=0, padx=40, pady=20)

        self.label_avertissement = customtkinter.CTkLabel(self.home_frame, text=label_text, font=label_font)
        self.label_avertissement.grid(row=1, column=0, padx=20, pady=20)

# if multiple frame

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        # self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        # self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()



    def home_button_event(self):
        self.select_frame_by_name("home")

    # def frame_2_button_event(self):
    #     self.select_frame_by_name("frame_2")

    # def frame_3_button_event(self):
    #     self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    async def discover_devices(self):
        
        devices = await discover()
        print("Discovered devices:")
        for device in devices:
            print(device)
        self.progress.stop()
    
    def connect(self):
        asyncio.run(self.discover_devices())

if __name__ == "__main__":

    app = App()
    app.mainloop()





