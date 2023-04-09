#include "actuator.h"
#include "Dynamixel2Arduino.h"
#include "ControleDynamixel.h"
#include "actuator.h"

#if defined(ARDUINO_OpenCR)  // When using official ROBOTIS board with DXL circuit.
// For OpenCR, there is a DXL Power Enable pin, so you must initialize and control it.
// Reference link : https://github.com/ROBOTIS-GIT/OpenCR/blob/master/arduino/opencr_arduino/opencr/libraries/DynamixelSDK/src/dynamixel_sdk/port_handler_arduino.cpp#L78
#define DXL_SERIAL Serial3
#define DEBUG_SERIAL Serial
const int DXL_DIR_PIN = 84;  // OpenCR Board's DIR PIN.
#endif
// #if defined(ARDUINO_OpenCR)  // When using official ROBOTIS board with DXL circuit.
// // For OpenCR, there is a DXL Power Enable pin, so you must initialize and control it.
// // Reference link : https://github.com/ROBOTIS-GIT/OpenCR/blob/master/arduino/opencr_arduino/opencr/libraries/DynamixelSDK/src/dynamixel_sdk/port_handler_arduino.cpp#L78
// #define DXL_SERIAL Serial3
// #define DEBUG_SERIAL Serial
// const int DXL_DIR_PIN = 84;  // OpenCR Board's DIR PIN.
// #endif

const uint8_t DXL_ID1 = 17;
const uint8_t DXL_ID2 = 1;
const float DXL_PROTOCOL_VERSION = 2.0;
unsigned long tempsActuel = 0;
unsigned long tempsPrecedent = 0;
const int PERIODE = 100;
const float RANGE_DETECTION_LOAD = 200;


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

void sauter() {
  dxl.setGoalVelocity(DXL_ID1, 15, UNIT_RPM);
  DEBUG_SERIAL.println(dxl.getPresentCurrent(DXL_ID1, UNIT_MILLI_AMPERE));
  dxl.setGoalVelocity(DXL_ID2, 15, UNIT_RPM);
  DEBUG_SERIAL.println(dxl.getPresentCurrent(DXL_ID2, UNIT_MILLI_AMPERE));
  delay(500);
}

//INPUT : Pourcentage de la vitesse du moteur [-100/100%]
//OUTPUT : Bool return 1 si pas d'erreur
bool sauterUneFois(float RPMGOAL) {
  //percent = percent * 0.02;
  dxl.torqueOn(DXL_ID1);
  dxl.torqueOn(DXL_ID2);
  dxl.setGoalVelocity(DXL_ID1, RPMGOAL, UNIT_RPM);
  dxl.setGoalVelocity(DXL_ID2, RPMGOAL, UNIT_RPM);

  float loadActuel = (dxl.getPresentCurrent(DXL_ID1));
  float loadPrecedent = loadActuel;

  DEBUG_SERIAL.println(dxl.getPresentCurrent(DXL_ID1));
  DEBUG_SERIAL.println(dxl.getPresentCurrent(DXL_ID2));


  tempsActuel = millis();
  while ((loadActuel - RANGE_DETECTION_LOAD) < loadPrecedent) {
    //      Serial.print((loadActuel - RANGE_DETECTION_LOAD));
    //      Serial.print("\t");
    //      Serial.println(loadPrecedent);
    // if (Serial1.available() > 0) {
    //   if (Serial1.read() == 's') {
    //     dxl.setGoalVelocity(DXL_ID1, 0);
    //     dxl.setGoalVelocity(DXL_ID2, 0);
    //     Serial.println("yo");
    //     return 0;
    //   }
    // }

    if (Serial.available()) {
      Serial.read();
      dxl.setGoalVelocity(DXL_ID1, 0);
      dxl.setGoalVelocity(DXL_ID2, 0);
      // dxl.torqueOff(DXL_ID1);
      // dxl.torqueOff(DXL_ID2);
      Serial.println("yo");
      return 0;
    }


    Serial.print(dxl.getPresentCurrent(DXL_ID1));
    Serial.print("\t");
    Serial.print(dxl.getPresentCurrent(DXL_ID2));
    Serial.print("\t");
    Serial.println(dxl.getPresentCurrent(DXL_ID2) - dxl.getPresentCurrent(DXL_ID1));

    if (millis() - tempsActuel > PERIODE) {
      // Serial.print(loadPrecedent);
      // Serial.print("\t");
      // Serial.println(loadActuel);
      loadPrecedent = loadActuel;
      tempsActuel = millis();
    }
    loadActuel = dxl.getPresentCurrent(DXL_ID1);
  }
  dxl.setGoalVelocity(DXL_ID1, 0);
  dxl.setGoalVelocity(DXL_ID2, 0);
  return 1;
}

// void sauter (){
//     dxl.setGoalVelocity(DXL_ID, 200);
//   delay(1000);
// }


/*
  void mainControleDynamixel(int Percent) {
  // Set Goal Velocity using RPM
  dxl.setGoalVelocity(DXL_ID, 25.8, UNIT_RPM);
  delay(1000);
  DEBUG_SERIAL.print("Present Velocity(rpm) : ");
  DEBUG_SERIAL.println(dxl.getPresentVelocity(DXL_ID, UNIT_RPM));
  delay(1000);
  }
*/