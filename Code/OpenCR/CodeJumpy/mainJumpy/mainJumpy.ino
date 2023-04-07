#include "ControleDynamixel.h"
// #include "Bluetooth.h"
#include "ControleFlywheel.h"
void setupBluetooth();
void readBluetooth() ;

const int PERIODE_BLUETOOTH = 10;  //ms
// enum { saute,
//        tourne,
//        wait };

HardwareTimer Timer(TIMER_CH1);
volatile char instruction;
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
//   if(Serial.available())//Select "No Line Ending" in Serial Monitor
// { 
  
//   Serial.read();
//   sauterUneFois(5);  
// }
// sauter();
  switch (instruction) {

    case 's':
      sauterUneFois(20);
      instruction = 'w';
      break;

    case 't':
      //fonction tourner(angle)
      instruction = 'w';
      break;
  }
}




void setupBluetooth()  {
    // Define pin modes for TX and RX
    pinMode(24, OUTPUT);
    // Set the baud rate for the SoftwareSerial object
    Serial4.begin(9600);
}
/*
Read Bluetooth signal
*/
void readBluetooth() {
    if (Serial1.available() > 0) {
      instruction = Serial4.read();
      // Serial.println(speed);
      // //return speed;
      }

}