#include <Wire.h>

byte slaveUID[4];

void setup() {
  Wire.begin();
  Serial.begin(9600);
}

void loop() {
  for (byte addr = 8; addr < 120; addr++) {
    Wire.requestFrom(addr, 4);
    int i = 0;
    while (Wire.available()) {
      slaveUID[i++] = Wire.read();
    }

    if (i == 4 && !(slaveUID[0] == 0 && slaveUID[1] == 0 && slaveUID[2] == 0 && slaveUID[3] == 0)) {
      Serial.print("[0x");
      Serial.print(addr, HEX);
      Serial.print(", ");
      for (int j = 0; j < 4; j++) {
        if (slaveUID[j] < 0x10) Serial.print("0");
        Serial.print(slaveUID[j], HEX);
        if (j < 3) Serial.print(":");
      }
      Serial.println("]");
    }
    delay(50);
  }

  delay(200);
}
