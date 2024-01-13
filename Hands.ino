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
int command = Serial.parseInt(); // Считываем число из COM-порта
// В зависимости от значения, выполняем соответствующее действие
if (command == 1) {
  digitalWrite(13, HIGH); // Включаем светодиод
  } else if (command == 0) {
  digitalWrite(13, LOW); // Выключаем светодиод
  } else if (command == 3) {
  // Считываем градус поворота
  int angle = Serial.parseInt();
  Serial.print("Received angle: ");
  Serial.println(angle);
  // Поворачиваем сервопривод
  servo1.write(angle);
  delay(15); // Делаем небольшую задержку для стабилизации сервопривода
  }
}   
