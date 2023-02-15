import machine
import time
sda=machine.Pin(26)
scl=machine.Pin(27)
i2c=machine.I2C(1,sda=sda, scl=scl, freq=400000)

print('Scan i2c bus...')
devices = i2c.scan()

if len(devices) == 0:
    print("No i2c device !")
else:
    print('i2c devices found:',len(devices))

for device in devices:
    print("Decimal address: ",device," | Hexa address: ",hex(device))

while 1:
    valueMS = int(*i2c.readfrom_mem(0x68,0x43,1,addrsize=8))
    valueLS = int(*i2c.readfrom_mem(0x68,0x44,1,addrsize=8))
    value = (valueMS << 8) | valueLS
    #print(bin(*valueMS) << 8)
    print(value)
    time.sleep(0.1)