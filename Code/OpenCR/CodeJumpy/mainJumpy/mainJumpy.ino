#include "ControleDynamixel.h"
#include "ControleFlywheel.h"
#include "Bluetooth.h"
volatile char instruction;
const int PERIODE_BLUETOOTH = 10;  //ms

//Timer pour l'interruption
HardwareTimer Timer(TIMER_CH1);

void setup() {
  setupBluetooth();
  setupControleDynamixel();
  setupControleFlywheel();
  Timer.stop();
  Timer.setPeriod(PERIODE_BLUETOOTH * 1000);  //Timer utilise des microsecondes
  Timer.attachInterrupt(readBluetooth);
  Timer.start();
}

void loop() {
  if (Serial.available())  //Choisir "No Line Ending" dans Serial Monitor
  {

    char com = Serial.read();
    Serial.read();  //Au cas ou il y a "Line Ending"
    if (com == 'm') {
      Serial.println("Message m sent");
      char mes = 'v';
      sendMessage(mes, 10);
    } else
      jump(8);
  }

  /* Instrction pour le switch case
   j : sauter
   t : tourner
   w : attente
  */
  switch (instruction) {
    case 'j':
      jump(6);
      instruction = 'w';
      break;

    case 't':
      //fonction turn(angle)
      instruction = 'w';
      break;
  }
}
