#include "ControleDynamixel.h"
#include "ControleFlywheel.h"
#include "Bluetooth.h"

const int PERIODE_BLUETOOTH = 10;  //ms
const int RMP_FLYWHEEL = 80; //Vitesse de la flywheel
const int RMP_JUMP = 6;

volatile char instruction;
volatile int RPM_flywheel_bluetooth = RMP_FLYWHEEL;
volatile int RPM_jump_bluetooth = RMP_JUMP;
volatile float CourrantM1_bluetooth = 0;

  

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
  turn(0);
}

void loop() {
  if (Serial.available())  //Choisir "No Line Ending" dans Serial Monitor
  {
    instruction = Serial.read();
  }

  /* Instrction pour le switch case
   j : sauter
   l : tourner à gauche
   r : tourner à droite
   w : attente
  */
  switch (instruction) {
    case 'j':
      jump(RMP_JUMP);
      instruction = 'w';
      break;

    case 'l':
      jump(RMP_JUMP);
      turn(RMP_FLYWHEEL);
        instruction = 'w';
      break;

    case 'r':
      jump(RMP_JUMP);
      turn(RMP_FLYWHEEL);
        instruction = 'w';
      break;
  }
}
