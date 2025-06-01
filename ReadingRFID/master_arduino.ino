#include <SPI.h>
#include <MFRC522.h>
#include <SoftwareSerial.h>

#define RST_PIN 9
#define SS_PIN 10

#define RX_PIN 2
#define TX_PIN 3

MFRC522 mfrc522(SS_PIN, RST_PIN);
SoftwareSerial mySerial(RX_PIN, TX_PIN);

int childCounter = 0;

unsigned long lastScanTime = 0;
const unsigned long scanInterval = 1000; // сканируем каждые 1 секунду

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);

  SPI.begin();
  mfrc522.PCD_Init();

  Serial.println("Master ready");
}

void loop() {
  unsigned long currentTime = millis();

  // Периодическое сканирование на главной
  if (currentTime - lastScanTime >= scanInterval) {
    lastScanTime = currentTime;
    if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
      String uidStr = "";
      for (byte i = 0; i < mfrc522.uid.size; i++) {
        if (mfrc522.uid.uidByte[i] < 0x10) uidStr += "0";
        uidStr += String(mfrc522.uid.uidByte[i], HEX);
        if (i < mfrc522.uid.size - 1) uidStr += "-";
      }
      uidStr.toUpperCase();

      Serial.print("Master UID: ");
      Serial.println(uidStr);
      mfrc522.PICC_HaltA();
    }
  }

  // Приём данных от дочерних
  if (mySerial.available()) {
    String uid = mySerial.readStringUntil('\n');
    childCounter++;
    Serial.print("Child ");
    Serial.print(childCounter);
    Serial.print(" UID: ");
    Serial.println(uid);
  }
}
