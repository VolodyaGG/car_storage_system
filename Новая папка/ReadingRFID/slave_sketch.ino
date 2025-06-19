#include <SPI.h>
#include <MFRC522.h>
#include <SoftwareSerial.h>

#define RST_PIN 9
#define SS_PIN 10

#define RX_PIN 2
#define TX_PIN 3

MFRC522 mfrc522(SS_PIN, RST_PIN);
SoftwareSerial mySerial(RX_PIN, TX_PIN);

unsigned long lastSendTime = 0;
const unsigned long sendInterval = 1500;  // минимальный интервал отправки UID

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);

  SPI.begin();
  mfrc522.PCD_Init();

  Serial.println("Arduino ready (local + remote UID)");
}

void loop() {
  unsigned long currentTime = millis();

  // === 📥 Прием UID от других Arduino ===
  if (mySerial.available()) {
    String incomingUID = mySerial.readStringUntil('\n'); // читаем строку до \n
    incomingUID.trim(); // убираем лишние пробелы и переносы
    if (incomingUID.length() > 0) {
      Serial.print("Received from another Arduino: ");
      Serial.println(incomingUID);
    }
  }


  if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
    if (currentTime - lastSendTime > sendInterval) {
      String uidStr = "";
      for (byte i = 0; i < mfrc522.uid.size; i++) {
        if (mfrc522.uid.uidByte[i] < 0x10) uidStr += "0";
        uidStr += String(mfrc522.uid.uidByte[i], HEX);
        if (i < mfrc522.uid.size - 1) uidStr += "-";
      }
      uidStr.toUpperCase();

      mySerial.println(uidStr);  // отправка по SoftwareSerial другим Arduino
      Serial.print("Sent local UID: ");
      Serial.println(uidStr);

      mfrc522.PICC_HaltA();
      lastSendTime = currentTime;
    }
  }
}
