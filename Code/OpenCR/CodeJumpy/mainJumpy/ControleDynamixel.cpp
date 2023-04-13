#include "actuator.h"
#include "Dynamixel2Arduino.h"
#include "ControleDynamixel.h"

#if defined(ARDUINO_OpenCR)  // Pour les cartes officiel ROBOTIS avec circuit DXL.
// Pour le OpenCR, il y a une pin "DXL Power Enable" qui doit être initialisé et contrôlé
// Reference : https://github.com/ROBOTIS-GIT/OpenCR/blob/master/arduino/opencr_arduino/opencr/libraries/DynamixelSDK/src/dynamixel_sdk/port_handler_arduino.cpp#L78
#define DXL_SERIAL Serial3
#define DEBUG_SERIAL Serial
const int DXL_DIR_PIN = 84;  // OpenCR DIR PIN.
#endif


const uint8_t DXL_ID1 = 17;
const uint8_t DXL_ID2 = 1;
const float DXL_PROTOCOL_VERSION = 2.0;
unsigned long ActualTime = 0;
unsigned long lastTime = 0;
const int PERIODE = 100;
const float RANGE_DETECTION_LOAD = 125;


Dynamixel2Arduino dxl(DXL_SERIAL, DXL_DIR_PIN);

//Requis pour contrôler la "control table"
using namespace ControlTableItem;


void setupControleDynamixel() {
  // Utilise port UART du DYNAMIXEL Shield pour debug.
  DEBUG_SERIAL.begin(115200);

  // Définis le baudrate à 57600bps. Cela doit être pareil que le baudrate du DYNAMIXEl.
  dxl.begin(57600);
  // Définis la version du protocole. Cela doit être pareil que la version de protocole du DYNAMIXEL.
  dxl.setPortProtocolVersion(DXL_PROTOCOL_VERSION);
  // Reçois les informations du DYNAMIXEL 
  dxl.ping(DXL_ID1);
  dxl.ping(DXL_ID2);

  // Désactivation du torque lors de la configuaration dans le EEPROM
  dxl.torqueOff(DXL_ID1);
  dxl.setOperatingMode(DXL_ID1, OP_VELOCITY);
  dxl.torqueOn(DXL_ID1);

  dxl.torqueOff(DXL_ID2);
  dxl.setOperatingMode(DXL_ID2, OP_VELOCITY);
  dxl.torqueOn(DXL_ID2);
}

//INPUT : RPM [-10/10]
//OUTPUT : Bool return 0 si pas d'erreur
bool jump(float RPMGOAL) {

  dxl.torqueOn(DXL_ID1);
  dxl.torqueOn(DXL_ID2);

  dxl.setGoalVelocity(DXL_ID1, RPMGOAL, UNIT_RPM);
  dxl.setGoalVelocity(DXL_ID2, RPMGOAL, UNIT_RPM);

  float actualLoad = (dxl.getPresentCurrent(DXL_ID1));
  float lastLoad = actualLoad;

  DEBUG_SERIAL.println(dxl.getPresentCurrent(DXL_ID1));
  DEBUG_SERIAL.println(dxl.getPresentCurrent(DXL_ID2));
  float currentdx1 = 0;
  float currentdx2 = 0;

  /*Cette boucle permet de détecté si il y a un front déscendant de courant
    dans les moteurs signifiant qu'il y a eu un saut, ainsi d'arrêter le robot */
  ActualTime = millis();
  while ((actualLoad + RANGE_DETECTION_LOAD) > lastLoad) {

    currentdx1 = dxl.getPresentCurrent(DXL_ID1);
    currentdx2 = dxl.getPresentCurrent(DXL_ID2);


    Serial.print(currentdx1);
    Serial.print("\t");
    Serial.print(currentdx2);
    Serial.print("\t");
    Serial.print(currentdx2 - currentdx1);
    Serial.print("\t");
    Serial.println(abs(currentdx2) + abs(currentdx1));
    
    //Arrêt d'urgence si le torque devient trop élevé pour pas brisé le robot
    if ((abs(currentdx1) + abs(currentdx2)) >= 650) {
      dxl.setGoalVelocity(DXL_ID1, 0);
      dxl.setGoalVelocity(DXL_ID2, 0);
      dxl.torqueOff(DXL_ID1);
      dxl.torqueOff(DXL_ID2);
      Serial.println("Safety engaged");
      return 1;
    }
    //Arrêt manuel si l'on souhaite arrêter le robot lors d'un saut
    if (Serial.available()) {
      Serial.read();
      dxl.setGoalVelocity(DXL_ID1, 0);
      dxl.setGoalVelocity(DXL_ID2, 0);
      dxl.torqueOff(DXL_ID1);
      dxl.torqueOff(DXL_ID2);
      Serial.println("stop");
      return 0;
    }
    lastLoad = actualLoad;
    actualLoad = currentdx1;
  }

  Serial.print(currentdx1);
  Serial.print("\t");
  Serial.print(currentdx2);
  Serial.print("\t");
  Serial.print(currentdx2 - currentdx1);
  Serial.print("\t");
  Serial.println(abs(currentdx2) + abs(currentdx1));

  Serial.println("Drop detected");
  dxl.setGoalVelocity(DXL_ID1, 0);
  dxl.setGoalVelocity(DXL_ID2, 0);
  return 0;
}
