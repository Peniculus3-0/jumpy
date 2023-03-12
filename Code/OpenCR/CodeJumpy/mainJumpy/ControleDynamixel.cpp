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


const uint8_t DXL_ID = 1;
const float DXL_PROTOCOL_VERSION = 2.0;
unsigned long tempsActuel = 0;
unsigned long tempsPrecedent = 0;
const int PERIODE = 20;
const int RANGE_DETECTION_LOAD = 40;


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
  dxl.ping(DXL_ID);

  // Turn off torque when configuring items in EEPROM area
  dxl.torqueOff(DXL_ID);
  dxl.setOperatingMode(DXL_ID, OP_VELOCITY);
  dxl.torqueOn(DXL_ID);
}

//INPUT : Pourcentage de la vitesse du moteur [-100/100%]
//OUTPUT : Bool return 1 si pas d'erreur
bool sauterUneFois(int percent) {
  dxl.setGoalVelocity(DXL_ID, percent, UNIT_PERCENT);
  int loadActuel = dxl.readControlTableItem(PRESENT_LOAD, DXL_ID);
  int loadPrecedent = loadActuel;
  tempsActuel = millis();
  while (loadActuel + RANGE_DETECTION_LOAD > loadPrecedent) {
    if (millis() - tempsActuel > PERIODE) {
      loadPrecedent = loadActuel;
      tempsActuel = millis();
    }
    loadActuel = dxl.readControlTableItem(PRESENT_LOAD, DXL_ID);
    // Serial.print(loadPrecedent);
    // Serial.print("\t");
    // Serial.println(loadActuel);
  }
  dxl.setGoalVelocity(DXL_ID, 0, UNIT_PERCENT);
  return 1;
}




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