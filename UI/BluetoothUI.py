from bleak import BleakScanner, BleakClient, discover
import asyncio
import logging
import threading
device_address = "94:A9:A8:3A:52:90"
CHARACTERISTIC_U = "0000ffe1-0000-1000-8000-00805f9b34fb"
import UI



combo_box_values = []


    
# Cette fonction lance un nouveau thread pour appeler la fonction 
# scan_devices avec l'application et la liste de dispositifs donnés
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


#Cette fonction est appelée lorsque la numérisation est terminée. Cette fonction est appelée par le thread principal. 
# Elle met à jour l'interface utilisateur avec les dispositifs numérisés.
def on_scan_finished(app,device_list):
        current_thread = threading.current_thread()
        print("Current Thread: {}".format(current_thread.name))
        print("Scan finished.")
        for dev in device_list:
            print("Device %s, name=%s " % (dev.address, dev.name))
            if dev.name != None:
                combo_box_values.append(dev.address +  str(dev.name))

        if combo_box_values != []:
        
            app.label_avertissement.configure(text="Select a device")
            app.combobox.configure(state="readonly")
            app.combobox.configure(values=(combo_box_values))
            app.jump_button.configure(state="normal")
            app.jump_button_left.configure(state="normal")
            app.jump_button_right.configure(state="normal")
        else:
            app.label_avertissement.configure(text="No device found")
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

        

#Cette fonction est appelée lorsque l'utilisateur sélectionne un dispositif dans la liste déroulante.
def connect_to_device_async(app,device_address):
    print(threading.current_thread().name)
    asyncio.run(connect_to_device(app,device_address))

#Cette fonction se connecte au dispositif sélectionné et envoie un message.
async def connect_to_device(app,message):
    logging.info(f'Current registered tasks: {len(asyncio.all_tasks())}')
    print("Connecting to device")
    async with BleakClient(device_address) as client:
        if client.is_connected:
            app.label_avertissement.configure(text="Connected")
            app.motor_panel.set_speed("12")
            await client.write_gatt_char(CHARACTERISTIC_U, bytearray(message.encode()))
            print("Message sent")
                    
        else:
            app.label_avertissement.configure(text="Not Connected")

#
def read_device_async(app):
    asyncio.run(read_device(app))

#Cette fonction se connecte au dispositif et lit les données.
async def read_device(app):
     dataholder = dataHolder(app)
     async with BleakClient(device_address) as client:
        if client.is_connected:
            app.label_avertissement.configure(text="Connected")
            services = await client.get_services()      
            await client.start_notify(17, dataholder.callback)
            while True : 
                await asyncio.sleep(1)
        else:
            app.label_avertissement.configure(text="Not Connected")

#Cette classe est utilisée pour stocker les données lues du dispositif et les afficher dans l'interface utilisateur.
class dataHolder:
    def __init__(self, app_instance):
        self.data1 = 0
        self.app = app_instance

    def callback(self, sender, data):
        self.data1 = data.decode("utf-8")
        print(self.data1)
        self.app.motor_panel.set_speed(self.data1)

    def get_data(self):
        return self.data1

    

    
    

