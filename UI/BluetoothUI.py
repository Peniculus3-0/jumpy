from bleak import BleakScanner, BleakClient, discover
import asyncio
import logging
import threading
device_address = "94:A9:A8:3A:52:90"
CHARACTERISTIC_U = "0000ffe1-0000-1000-8000-00805f9b34fb"
import UI


combo_box_values = []

# class BLEScanner: 
#     def __init__(self, device_list):
#         self.device_list = device_list
        
#     async def scan_devices(self):
#         devices = await discover()
#         self.device_list.extend(devices)

# async def start_scanning(device_list):
#     print("start scanning")
#     scanner = BLEScanner(device_list)
#     await scanner.scan_devices()
#     print("scan finished-----")
    
def thread_scan_devices(app, device_list):
    current_thread = threading.current_thread()
    print("Current Thread: {}".format(current_thread.name))
    mythread = threading.Thread(target=scan_devices, args=(device_list,))
    mythread.start()
    mythread.join()
    print("thread finished")
    print(device_list)
    current_thread = threading.current_thread()
    print("Current Thread: {}".format(current_thread.name))
    on_scan_finished(app,device_list)

def on_scan_finished(app,device_list):
        current_thread = threading.current_thread()
        print("Current Thread: {}".format(current_thread.name))
        print("Scan finished.")
        for dev in device_list:
            print("Device %s, name=%s " % (dev.address, dev.name))
            # app.textbox.insert(tk.END, "Device %s, Name=%s \n" % (dev.address, dev.name))
            if dev.name != None:
                combo_box_values.append(dev.address +  str(dev.name))

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

    

    
def scan_devices(device_list):
    current_thread = threading.current_thread()
    print("Current Thread: {}".format(current_thread.name))
    asyncio.run(start_scanning(device_list))
    
async def start_scanning(device_list):

        devices = await BleakScanner.discover()
        device_list.extend(devices)

        

           
        

def connect_to_device_async(device_address):
    print(threading.current_thread().name)
    asyncio.run(connect_to_device(device_address))

async def connect_to_device(message):
    logging.info(f'Current registered tasks: {len(asyncio.all_tasks())}')
    print("Connecting to device")
    async with BleakClient(device_address) as client:
        # do something with the client connection
        if client.is_connected:
            app.label_avertissement.configure(text="Connected")
            await client.start_notify(CHARACTERISTIC_U, callback)
            while open :
                await asyncio.sleep(1)

            # print(f"Connected to {device_address}")
            # services = client.services
            # print("Services:")
            # for service in services:
            #     print(service)
                await client.write_gatt_char(CHARACTERISTIC_U, bytearray(message.encode()))
                    
        else:
            app.label_avertissement.configure(text="Not Connected")

