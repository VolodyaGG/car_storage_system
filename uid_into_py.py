import serial
from port_definition import return_com


def record_uid():
    port = return_com()

    ser = serial.Serial(port, 9600, timeout=1.7)


    response = ser.readline()

    decoded_response = response.decode('utf-8').strip()

    ser.close()

    return decoded_response if decoded_response else None