#include "Bluetooth.h"
#include "String"
#include <Arduino.h>
extern volatile char instruction;
extern volatile int RPM_flywheel_bluetooth;
extern volatile int RPM_jump_bluetooth;
extern volatile float CourrantM1_bluetooth;
void setupBluetooth() {
  // Définition des modes de pin TX et RX
  pinMode(24, OUTPUT);
  // Définition du baud rate pour l'objet SoftwareSerial
  Serial4.begin(9600);
}
/*
Lecture du Bluetooth
*/
void readBluetooth() {
  if (Serial4.available() > 0) {
    instruction = Serial4.read();
    Serial.println(instruction);
  }
  char t[10];
  Serial4.write(itoa(CourrantM1_bluetooth, t, 10)); 
}

void sendMessage(char message, int position) {

  char s[10];
  itoa(position, s, 10);
  char temp[2] = { message, '\0' };
  strcat(temp, s);


  Serial.println(temp);
  Serial4.write(temp);
}