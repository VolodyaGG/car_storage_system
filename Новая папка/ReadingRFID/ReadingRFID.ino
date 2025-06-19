#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN 9
#define SS_PIN 10

MFRC522 mfrc522(SS_PIN, RST_PIN);

void setup() {
  Serial.begin(9600);
  SPI.begin();
  mfrc522.PCD_Init();
}

void loop() {
  if (!mfrc522.PICC_IsNewCardPresent() || !mfrc522.PICC_ReadCardSerial()) {
    return;
  }

  // Формируем UID в виде строки (например, "A3-4B-12-8F")
  String uidStr;
  for (byte i = 0; i < mfrc522.uid.size; i++) {
    uidStr += (mfrc522.uid.uidByte[i] < 0x10 ? "0" : "");
    uidStr += String(mfrc522.uid.uidByte[i], HEX);
    if (i < mfrc522.uid.size - 1) uidStr += "-";
  }
  uidStr.toUpperCase();

  // Отправляем в Serial-порт
  Serial.println(uidStr);

  mfrc522.PICC_HaltA();
}