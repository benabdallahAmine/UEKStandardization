from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('127.0.0.1', port=5020)
client.connect()


client.write_register(address=0x200, value= 50, unit= 48)
try:
    while(True):
        request = client.read_input_registers(address=0xff,count=1,unit=28)
        if(request.registers[0] >= 9600 and request.registers[0] > 9900) :
            client.write_register(address=0x200, value= 0, unit= 48)
        else:
            client.write_register(address=0x200, value= 50, unit= 48)
except Exception :
    print('You saved the world')

client.close()