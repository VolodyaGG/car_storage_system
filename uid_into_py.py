import serial
import time

port = "COM6" #find name of a port using port_definition.py

def record_uid():
    ser = serial.Serial(port, 9600, timeout=1.7)


    response = ser.readline()

    decoded_response = response.decode('utf-8').strip()

    ser.close()

    return decoded_response if decoded_response else None