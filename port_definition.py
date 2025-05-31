import serial.tools.list_ports


def return_com():
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if "Arduino" in port.description or "CH340" in port.description:
            return port.device

return_com()