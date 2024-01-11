#include <Servo.h>

Servo servo1;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  servo1.attach(5); // Подключите сервопривод к пину 9
}

void loop() {
  if (Serial.available() > 0) {
    int command = Serial.parseInt(); // Считываем число из COM-порта

    // В зависимости от значения, выполняем соответствующее действие
    if (command == 1) {
      digitalWrite(13, HIGH); // Включаем светодиод
    } else if (command == 2) {
      digitalWrite(13, LOW); // Выключаем светодиод
    } else if (command == 3) {
      // Считываем градус поворота
      int angle = Serial.parseInt();
      
      // Ограничиваем градус в пределах от 0 до 180
      angle = constrain(angle, 0, 180);

      // Поворачиваем сервопривод
      servo1.write(angle);
      delay(15); // Делаем небольшую задержку для стабилизации сервопривода
    }
  }
}
