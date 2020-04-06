from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('127.0.0.1', port=5020)
client.connect()

request = client.read_input_registers(address=0xff,count=1,unit=28)
print(request.registers[0])


client.close()