#include "ControleDynamixel.h"
#include "ControleFlywheel.h"
#include "main.h"
#include "Bluetooth.h"
// void setupBluetooth();
// void readBluetooth();
volatile char instruction;
const int PERIODE_BLUETOOTH = 10;  //ms
// enum { saute,
//        tourne,
//        wait };

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
  if(Serial.available())//Select "No Line Ending" in Serial Monitor
{ 
  
  Serial.read();
  sauterUneFois(4);  
}
// sauter();
  // switch (instruction) {

  //   case 's':
  //     sauterUneFois(6);
  //     instruction = 'w';
  //     break;

  //   case 't':
  //     //fonction tourner(angle)
  //     instruction = 'w';
  //     break;
  // }
}




