# scanner.py
import asyncio
from bleak import BleakScanner, BleakClient, discover

address = "94:A9:A8:3A:52:90"
uuid = '0000ffe1-0000-1000-8000-00805f9b34fb'
CHARACTERISTIC_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"
message = 'F'
global Device_not_found 

async def main():
    # Device_not_found = True
    # while  Device_not_found:
    #     devices = await BleakScanner.discover()+++
    #     if(len(devices)==0):
    #         print("No devices found")

    #     for details in devices:
    #         print(details.name)
    #         if(details.name=="DSD TECH"):
    #             address = details
    #             print(address)
                async with BleakClient(address) as client:
                    services = await client.get_services()
                    for service in services:
                        print('service', service.handle, service.uuid, service.description)
                        characteristics = service.characteristics

                        for char in characteristics:
                            print('  characteristic', char.handle, char.uuid, char.description, char.properties)

                            descriptors = char.descriptors

                            for desc in descriptors:
                                print('    descriptor', desc)

                        
async def write():
  async with BleakClient(address) as client:
    if (not client.is_connected):
      raise "client not connected"

    # services = await client.get_services()

    await client.write_gatt_char(uuid, bytearray(message.encode()))
    print("write done")

           

async def discover_devices():
    devices = BleakScanner.discovered_devices
    print("Discovered devices:")
    print(devices) 
       
async def connect_to_device(device_address):
    print("Connecting to device")
    async with BleakClient(device_address) as client:
        # do something with the client connection
        print(f"Connected to {device_address}")
        services = client.services
        print("Services:")
        for service in services:
            print(service)


async def read_ble_device(device_address, uuid):
    async with BleakClient(device_address) as client:
        print("connection_status")
        #await client.connect()
        print("Connected to device")
        
        # Read data from the characteristic or descriptor with the given UUID

        await client.start_notify(client.read_characteristic, client.notification_handler)
        # Process the data as needed

async def connect(self):
        if self.connected:
            return
        try:
            await self.client.connect()
            self.connected = await self.client.is_connected()
            if self.connected:
                print(f"Connected to {self.connected_device.name}")
                self.client.set_disconnected_callback(self.on_disconnect)
                await self.client.start_notify(
                    self.read_characteristic, self.notification_handler,
                )
                while True:
                    if not self.connected:
                        break
                    await asyncio.sleep(5.0, loop=loop)
            else:
                print(f"Failed to connect to {self.connected_device.name}")
        except Exception as e:
            print(e)

def callback(sender , data):

    data1 = data.decode("utf-8")
    print(f"{data1}")



async def main():
    client = BleakClient(address)
    await client.connect()
    print("connected")
       
            #await client.star(uuid, callback)
    await client.start_notify(uuid, callback)
    while True:
        await asyncio.sleep(1)
        #print("data: {0}".format("".join(map(chr, data))))
   

asyncio.run(main())



#loop = asyncio.get_event_loop()
# futur=asyncio.ensure_future(main())
# asyncio.run(futur)