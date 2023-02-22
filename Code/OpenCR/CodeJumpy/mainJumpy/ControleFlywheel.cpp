#include "ControleFlywheel"

cIMU    IMU;

void setupControleFlywheel(){
  IMU.begin();
}


void mainControleFlywheel(){

  static uint32_t tTime[3];
  static uint32_t imu_time = 0;

  tTime[2] = micros();
  if( IMU.update() > 0 ) imu_time = micros()-tTime[2];

  if( (millis()-tTime[1]) >= 50 )
  {
    tTime[1] = millis();

    Serial.print(imu_time);
    Serial.print(" ");
    Serial.print(IMU.rpy[0]);
    Serial.print(" ");
    Serial.print(IMU.rpy[1]);
    Serial.print(" ");
    Serial.println(IMU.rpy[2]);
  }


  if( Serial.available() )
  {
    char Ch = Serial.read();

    if( Ch == '1' )
    {
      Serial.println("ACC Cali Start");

      IMU.SEN.acc_cali_start();
      while( IMU.SEN.acc_cali_get_done() == false )
      {
        IMU.update();
      }

      Serial.print("ACC Cali End ");
    }
  }

}