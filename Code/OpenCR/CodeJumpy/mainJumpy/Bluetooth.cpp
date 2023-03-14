#include "Bluetooth.h"

void setupBluetooth()  {
    // Define pin modes for TX and RX
    pinMode(24, OUTPUT);
    // Set the baud rate for the SoftwareSerial object
    Serial.begin(9600);
    Serial4.begin(9600);
}
/*
Read Bluetooth signal
*/
void readBluetooth() {
    /*if (Serial1.available() > 0) {
      int speed = Serial4.parseInt();
      Serial.println(speed);
      //return speed;
      }*/

}