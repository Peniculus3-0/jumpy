from builtins import str
from tkinter import DISABLED
from turtle import window_height

import customtkinter as customtkinter
import os 
from PIL import Image
import asyncio
from bleak import BleakScanner, BleakClient, discover
import threading
import animationv2 as animation
import time
    
device_address = "94:A9:A8:3A:52:90"
CHARACTERISTIC_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"
message = 'N'
label_text = " "
device_list = []
combo_box_values = []
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
        # app.textbox.insert(tk.END, "Device %s, Name=%s \n" % (dev.address, dev.name))
        if dev.name != None:
            combo_box_values.append(dev.address + " " + str(dev.name))

    if combo_box_values != []:
        app.label_avertissement.configure(text="Select a device")
        app.combobox.configure(state="readonly")
        app.combobox.configure(values=(combo_box_values))
        # app.button_scan.configure(state="disabled")
        # app.button_connect.configure(state="normal")
    else:
        app.label_avertissement.configure(text="No device found")
        # app.button_scan.configure(state="normal")
        # app.button_connect.configure(state="disabled")
        app.combobox.configure(state="disabled")
        app.combobox.configure(values=[])
        app.combobox.set("")
    
 
        

def start_scanning_async():
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
    time.sleep(10)
    app.label_avertissement.configure(text="Not Connected")
            
class RadioButtonFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="RadioButtonFrame", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name

        self.header = customtkinter.CTkLabel(self, text=self.header_name)
        self.header.grid(row=0, column=0, padx=10, pady=10)

        self.radio_button_var = customtkinter.StringVar(value="")

        self.radio_button_1 = customtkinter.CTkRadioButton(self, text="Option 1", value="Option 1", variable=self.radio_button_var)
        self.radio_button_1.grid(row=1, column=0, padx=10, pady=10)
        self.radio_button_2 = customtkinter.CTkRadioButton(self, text="Option 2", value="Option 2", variable=self.radio_button_var)
        self.radio_button_2.grid(row=2, column=0, padx=10, pady=10)
        self.radio_button_3 = customtkinter.CTkRadioButton(self, text="Option 3", value="Option 3", variable=self.radio_button_var)
        self.radio_button_3.grid(row=3, column=0, padx=10, pady=(10, 20))

    def get_value(self):
        """ returns selected value as a string, returns an empty string if nothing selected """
        return self.radio_button_var.get()

    def set_value(self, selection):
        """ selects the corresponding radio button, selects nothing if no corresponding radio button """
        self.radio_button_var.set(selection)



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Bluetooth Application")
        self.geometry("700x450")
        button_font = customtkinter.CTkFont(family="Arial", size=30, weight="bold")
        label_font = customtkinter.CTkFont(family="Arial", size=20)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

       

        # load images 
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo-color.png")), size=(100, 50))
        self.robot_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "robot.png")), size=(250, 250))

        # set icon
        self.iconbitmap(os.path.join(image_path, "logo.ico"))

        # c 
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0, )
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(2, weight=1)

         # create animation frame
        # self.animation_canvas = animation.canvas(self)
        # self.animation_canvas.grid(row=0, column=5, sticky="nsew")


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
        self.home_frame.grid_rowconfigure(2, weight=1)



        # self.connect_button = customtkinter.CTkButton(self.home_frame, text="Connect", compound="right", command=lambda: threading.Thread(target=connect_to_device_async, args=(message)).start())
        # self.connect_button.grid(row=2, column=0, padx=20, pady=10)
       

        self.jump_button = customtkinter.CTkButton(self.home_frame, text="JUMP",font=button_font, compound="bottom", height=60, width=200, command=lambda: threading.Thread(target=connect_to_device_async, args=(message)).start())
        self.jump_button.grid(row=0, column=0, padx=40, pady=20)

        self.find_button = customtkinter.CTkButton(self.home_frame, text="Find", font=button_font, compound="bottom", height=60, width=200, command=lambda: threading.Thread(target=start_scanning_async, args=(device_list)).start())
        self.find_button.grid(row=3, column=0, padx=40, pady=20)
        # self.hello_buttun = customtkinter.CTkButton(self.home_frame, text="Hello", font=button_font, compound="bottom", height=60, width=200, command=animation.print)
        # self.hello_buttun.grid(row=1, column=0, padx=40, pady=20)
        self.label_avertissement = customtkinter.CTkLabel(self.home_frame, text=label_text, font=label_font)
        self.label_avertissement.grid(row=1, column=0, padx=20, pady=20)

        # self.textbox = customtkinter.CTkTextbox(self.home_frame, width=400, corner_radius=0)
        # self.textbox.grid(row=5, column=0, sticky="n", padx=20, pady=20)

        self.combobox = customtkinter.CTkComboBox(self.home_frame,  values=["Device"])
        self.combobox.grid(row=5, column=0, sticky="n", padx=20, pady=20)

        self.robot_label = customtkinter.CTkLabel(self.home_frame, image=self.robot_image, text=None)
        self.robot_label.grid(row=2, column=0)

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





