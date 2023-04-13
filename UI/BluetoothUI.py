from bleak import BleakScanner, BleakClient, discover
import asyncio
import logging
import UI
import threading
device_address = "94:A9:A8:3A:52:90"
CHARACTERISTIC_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"


async def connect_to_device(message):
    logging.info(f'Current registered tasks: {len(asyncio.all_tasks())}')
    print("Connecting to device")
    async with BleakClient(device_address) as client:
        # do something with the client connection
        if client.is_connected:
            UI.App.label_avertissement.configure(text="Connected")
            await client.start_notify(CHARACTERISTIC_UUID, callback)
            while open :
                await asyncio.sleep(1)

            # print(f"Connected to {device_address}")
            # services = client.services
            # print("Services:")
            # for service in services:
            #     print(service)
                await client.write_gatt_char(CHARACTERISTIC_UUID, bytearray(message.encode()))
                    
        else:
            app.label_avertissement.configure(text="Not Connected")

#             class BLEScanner: 
# def __init__(self, device_list):
#         self.device_list = device_list
        
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
    
async def readdevice():
    async with BleakClient(device_address) as client:
        x = await client.read_gatt_char(CHARACTERISTIC_UUID)
        print(bytes(x).decode("utf-8"))
        return bytes(x).decode("utf-8")

        

def start_scanning_async():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_scanning(device_list))
    loop.close()
    on_scan_finished(device_list)

def connect_to_device_async(device_address):
    print(threading.current_thread().name)
    asyncio.run(connect_to_device(device_address))