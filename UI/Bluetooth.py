# scanner.py
import asyncio
from bleak import BleakScanner, BleakClient

uuid_battery_service = '0000180f-0000-1000-8000-00805f9b34fb'
uuid_battery_level_characteristic = '00002a19-0000-1000-8000-00805f9b34fb'

async def main():
    devices = await BleakScanner.discover()

    for details in devices:
        print(details.name)
        if(details.name=="LE_WH-1000XM4"):
            address = details
            print(address)
            async with BleakClient(address) as client:
                svcs = await client.get_services()
                for service in svcs:
                    print(service)



asyncio.run(main())