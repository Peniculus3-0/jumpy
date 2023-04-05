import threading
import tkinter as tk
import asyncio
from bleak import BleakScanner, BleakClient, discover

device_address = "94:A9:A8:3A:52:90"
CHARACTERISTIC_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"
message = 'F'

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
    print("Connecting to device")
    async with BleakClient(device_address) as client:
        # do something with the client connection
        print(f"Connected to {device_address}")
        services = client.services
        print("Services:")
        for service in services:
            print(service)
        
        await client.write_gatt_char(CHARACTERISTIC_UUID, bytearray(message.encode()))



root = tk.Tk()
root.geometry("400x400")
root.title("BLE Scanner")

device_list = []

start_button = tk.Button(root, text="Start Scanning", command=lambda: threading.Thread(target=start_scanning_async, args=(device_list,)).start())
start_button.pack(pady=20)

stop_button = tk.Button(root, text="Stop Scanning", command=lambda: threading.Lock())
stop_button.pack(pady=20)

connect_button = tk.Button(root, text="Connect to device", command=lambda: threading.Thread(target=connect_to_device_async, args=(message)).start())
connect_button.pack(pady=20)

# send_button = tk.Button(root, text="Send Message", command=lambda: threading.Thread(target=send_message, args=(device_list[listbox.curselection()[0]], message_entry.get())).start())
# send_button.pack(pady=10)

listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)

def update_listbox():
    listbox.delete(0, tk.END)
    for dev in device_list:
        listbox.insert(tk.END, "Device %s, Name=%s" % (dev.address, dev.name))
    root.after(1000, update_listbox)

root.after(1000, update_listbox)
root.mainloop()

