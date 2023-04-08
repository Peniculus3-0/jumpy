#include "Bluetooth.h"
#include <Arduino.h>
extern volatile char instruction;
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