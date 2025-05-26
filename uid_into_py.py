import serial
import threading

class UIDReader:
    def __init__(self, port: str = "COM3", baudrate: int = 9600, callback=None):
        self.ser = serial.Serial(port, baudrate, timeout=1)
        self.callback = callback
        self.running = False

    def start(self):
        self.running = True
        thread = threading.Thread(target=self.read_loop, daemon=True)
        thread.start()

    def stop(self):
        self.running = False
        if self.ser.is_open:
            self.ser.close()

    def read_loop(self):
        while self.running:
            if self.ser.in_waiting:
                line = self.ser.readline().decode('utf-8').strip()
                if line.startswith("[") and line.endswith("]"):
                    slave_id, uid = line[1:-1].split(", ")
                    if self.callback:
                        self.callback(slave_id, uid)
    
    def record_uid(port="COM3", baudrate=9600, timeout=5):
        try:
            ser = serial.Serial(port, baudrate, timeout=timeout)
            line = ser.readline().decode('utf-8').strip()
            ser.close()
            if line.startswith("[") and line.endswith("]"):
                slave_id, uid = line[1:-1].split(", ")
                return uid
            else:
                return None
        except Exception as e:
            print(f"Ошибка при чтении UID: {e}")
            return None
