#include "ControleDynamixel.h"
#include "Bluetooth.h"
#include "ControleFlywheel.h"

const int PERIODE_BLUETOOTH = 10;  //ms
enum { saute,
       tourne,
       wait };
volatile unsigned char instruction;

HardwareTimer Timer(TIMER_CH1);

void setup() {
  // put your setup code here, to run once:
  Timer.stop();
  Timer.setPeriod(PERIODE_BLUETOOTH * 1000);  //Timer utilise des microsecondes
  Timer.attachInterrupt(readBluetooth);
  Timer.start();
  setupControleDynamixel();
  setupControleFlywheel();
  setupBluetooth();
}

void loop() {
  /*if(Serial.available())//Select "No Line Ending" in Serial Monitor
{ 
  Serial.read();
  sauterUneFois(20);  
}*/

  switch (instruction) {

    case saute:
      sauterUneFois(20);
      instruction = wait;
      break;

    case tourne:
      //fonction tourner(angle)
      instruction = wait;
      break;
  }
}
