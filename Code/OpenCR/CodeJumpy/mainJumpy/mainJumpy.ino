#include "ControleDynamixel.h"
#include "Bluetooth.h"

void setup() {
  // put your setup code here, to run once:
  setupBluetooth();


}

void loop() {
  // put your main code here, to run repeatedly:
  readBluetooth();
}
