# scanner.py
import asyncio
from bleak import BleakScanner, BleakClient, discover

address = "94:A9:A8:3A:52:90"
uuid = '0000ffe1-0000-1000-8000-00805f9b34fb'
uuid_battery_level_characteristic = '00002a19-0000-1000-8000-00805f9b34fb'
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




loop = asyncio.get_event_loop()
loop.run_until_complete(write())
