#include "ControleDynamixel.h"
#include "ControleFlywheel.h"
#include "main.h"
#include "Bluetooth.h"
volatile char instruction;
const int PERIODE_BLUETOOTH = 10;  //ms

HardwareTimer Timer(TIMER_CH1);

void setup() {
  // put your setup code here, to run once:
  setupBluetooth();
  Timer.stop();
  Timer.setPeriod(PERIODE_BLUETOOTH * 1000);  //Timer utilise des microsecondes
  Timer.attachInterrupt(readBluetooth);
  Timer.start();
  setupControleDynamixel();
  setupControleFlywheel();
}

void loop() {
  if (Serial.available())  //Select "No Line Ending" in Serial Monitor
  {

    char com = Serial.read();
    if (com == 'm' ) {
      Serial.println("Message m sent");
      char mes = 'v';
      sendMessage(mes,10);
    } else
      jump(8);
  }
  // sauter();
  // switch (instruction) {

  //   case 's':
  //     jump(6);
  //     instruction = 'w';
  //     break;

  //   case 't':
  //     //fonction turn(angle)
  //     instruction = 'w';
  //     break;
  // }
}
