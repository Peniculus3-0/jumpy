#ifndef   BLUETOOTH_H
#define   BLUETOOTH_H
// #include "ControleDynamixel.h"

#include <Arduino.h>
#include "main.h"

void setupBluetooth();
void readBluetooth();
void sendMessage(char message,int position);

#endif
