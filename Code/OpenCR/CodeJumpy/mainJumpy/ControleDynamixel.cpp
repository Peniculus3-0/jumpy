#include "actuator.h"
#include "Dynamixel2Arduino.h"
#include "ControleDynamixel.h"

#if defined(ARDUINO_OpenCR)  // When using official ROBOTIS board with DXL circuit.
// For OpenCR, there is a DXL Power Enable pin, so you must initialize and control it.
// Reference link : https://github.com/ROBOTIS-GIT/OpenCR/blob/master/arduino/opencr_arduino/opencr/libraries/DynamixelSDK/src/dynamixel_sdk/port_handler_arduino.cpp#L78
#define DXL_SERIAL Serial3
#define DEBUG_SERIAL Serial
const int DXL_DIR_PIN = 84;  // OpenCR Board's DIR PIN.
#endif


const uint8_t DXL_ID1 = 17;
const uint8_t DXL_ID2 = 1;
const float DXL_PROTOCOL_VERSION = 2.0;
unsigned long ActualTime = 0;
unsigned long lastTime = 0;
const int PERIODE = 100;
const float RANGE_DETECTION_LOAD = 125;


Dynamixel2Arduino dxl(DXL_SERIAL, DXL_DIR_PIN);

//This namespace is required to use Control table item names
using namespace ControlTableItem;


void setupControleDynamixel() {
  // Use UART port of DYNAMIXEL Shield to debug.
  DEBUG_SERIAL.begin(115200);

  // Set Port baudrate to 57600bps. This has to match with DYNAMIXEL baudrate.
  dxl.begin(57600);
  // Set Port Protocol Version. This has to match with DYNAMIXEL protocol version.
  dxl.setPortProtocolVersion(DXL_PROTOCOL_VERSION);
  // Get DYNAMIXEL information
  dxl.ping(DXL_ID1);
  dxl.ping(DXL_ID2);

  // Turn off torque when configuring items in EEPROM area
  dxl.torqueOff(DXL_ID1);
  dxl.setOperatingMode(DXL_ID1, OP_VELOCITY);
  dxl.torqueOn(DXL_ID1);

  dxl.torqueOff(DXL_ID2);
  dxl.setOperatingMode(DXL_ID2, OP_VELOCITY);
  dxl.torqueOn(DXL_ID2);
}

//INPUT : Pourcentage de la vitesse du moteur [-100/100%]
//OUTPUT : Bool return 1 si pas d'erreur
bool jump(float RPMGOAL) {
  //percent = percent * 0.02;
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

    if ((abs(currentdx1) + abs(currentdx2)) >= 650) {
      dxl.setGoalVelocity(DXL_ID1, 0);
      dxl.setGoalVelocity(DXL_ID2, 0);
      dxl.torqueOff(DXL_ID1);
      dxl.torqueOff(DXL_ID2);
      Serial.println("Safety engaged");
      return 1;
    }

    if (Serial.available()) {
      Serial.read();
      dxl.setGoalVelocity(DXL_ID1, 0);
      dxl.setGoalVelocity(DXL_ID2, 0);
      // dxl.torqueOff(DXL_ID1);
      // dxl.torqueOff(DXL_ID2);
      Serial.println("stop");
      return 0;
    }

    // if (millis() - ActualTime > PERIODE) {
    //   // Serial.print(lastLoad);
    //   // Serial.print("\t");
    //   // Serial.println(actualLoad);

    //   ActualTime = millis();
    // }      
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
