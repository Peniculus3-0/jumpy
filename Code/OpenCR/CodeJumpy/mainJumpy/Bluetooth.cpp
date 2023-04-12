#include "Bluetooth.h"
#include "String"
#include <Arduino.h>
extern volatile char instruction;
void setupBluetooth() {
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
  }
}

void sendMessage(char message, int position) {

char s[10];
itoa(position,s,10);
char temp[2] = {message, '\0'} ;
strcat(temp,s);

 
Serial.println(temp);
  // Serial4.write(mess_char);
}