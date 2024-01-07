#include <Servo.h>
Servo servo1;

void setup() {
  Serial.begin(9600);
  pinMode (13, OUTPUT);
  Serial.println("1-LED_ON");
  Serial.println("2-LED_OFF");
  Serial.println("0-Servo");
  servo1.attach(5);
}

void loop() {
  if (Serial.available()){
    byte c = Serial.read();
    switch (c) {
      case '1':
        digitalWrite(13, 1);
        break;
      case '0':
        digitalWrite(13, 0);
        break;
      case '2':
        servo1.write(0);
        delay(1500);
        servo1.write(180);
        delay(1500);
        break;
    }
  }
}