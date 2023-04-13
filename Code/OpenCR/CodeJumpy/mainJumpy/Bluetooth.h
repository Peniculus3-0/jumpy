#ifndef   BLUETOOTH_H
#define   BLUETOOTH_H

#include <Arduino.h>

void setupBluetooth();
void readBluetooth();
void sendMessage(char message,int position);

#endif
