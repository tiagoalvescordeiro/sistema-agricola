#include <Arduino.h>
#include <DHT.h>

#define DHTPIN 14
#define DHTTYPE DHT22
#define PH_PIN 34
#define FOSFORO_PIN 22
#define POTASSIO_PIN 23
#define RELE_PIN 12

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();

  pinMode(FOSFORO_PIN, INPUT_PULLUP);
  pinMode(POTASSIO_PIN, INPUT_PULLUP);
  pinMode(RELE_PIN, OUTPUT);
  digitalWrite(RELE_PIN, LOW);
}

void loop() {
  float umidade = dht.readHumidity();
  int fosforo = digitalRead(FOSFORO_PIN); // 1 = pressionado (presença)
  int potassio = digitalRead(POTASSIO_PIN);
  int phRaw = analogRead(PH_PIN);
  float ph = map(phRaw, 0, 4095, 0, 14);

  Serial.print("Umidade: "); Serial.print(umidade); Serial.print(" % ");
  Serial.print(" | P: "); Serial.print(!fosforo);
  Serial.print(" | K: "); Serial.print(!potassio);
  Serial.print(" | pH: "); Serial.println(ph);

  if (umidade < 30 || !fosforo || !potassio || ph < 5.5 || ph > 7.5) {
    digitalWrite(RELE_PIN, HIGH); // Liga bomba
  } else {
    digitalWrite(RELE_PIN, LOW);  // Desliga bomba
  }

  delay(2000);
}