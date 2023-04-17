#include "ControleFlywheel.h"
#include <Servo.h>
#include <Wire.h>

Servo ESC;

unsigned long actualTime = 0;
const int PERIODE = 100;

void setupControleFlywheel() {
  ESC.attach(11, 1000, 2000);
}


void turn(int RPMGOAL) {
  actualTime = millis();

  while (actualTime + PERIODE > millis()) {
    ESC.write(RPMGOAL);
  }
  ESC.write(0);
}
