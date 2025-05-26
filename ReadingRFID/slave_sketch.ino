#include <Wire.h>
#include <SPI.h>
#include <MFRC522.h>

#define I2C_ADDRESS 0x10
#define RST_PIN     9
#define SS_PIN      10

MFRC522 mfrc522(SS_PIN, RST_PIN);
byte uidBuffer[4] = {0};

void setup() {
  Wire.begin(I2C_ADDRESS);
  Wire.onRequest(sendUID);
  SPI.begin();
  mfrc522.PCD_Init();
}

void loop() {
  if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
    for (byte i = 0; i < 4; i++) {
      uidBuffer[i] = mfrc522.uid.uidByte[i];
    }
    mfrc522.PICC_HaltA();
  }
}

void sendUID() {
  Wire.write(uidBuffer, 4);
  // Сброс UID после отправки
  for (byte i = 0; i < 4; i++) uidBuffer[i] = 0;
}
