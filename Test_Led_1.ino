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
    byte mode = Serial.read();
    switch (mode) {
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
      case '3':
        Serial.println("3");
        if (Serial.available()>0){
          byte grad = Serial.parseInt();
          Serial.println(grad);
          servo1.write(grad);
          delay(1500);
          break;
      }   
    }
  }
}