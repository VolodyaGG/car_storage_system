import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())

for port in ports:
    print(f"Порт: {port.device}\n Описание: {port.description}\n Производитель: {port.manufacturer}")