import serial

port = "" #find name of a port using port_definition.py

def record_uid():
    ser = serial.Serial(port, 9600)

    response = ser.readline()

    decoded_response = response.decode('utf-8')

    ser.close()

    return decoded_response
