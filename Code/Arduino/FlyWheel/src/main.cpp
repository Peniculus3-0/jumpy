#include <Arduino.h>
#include "Wire.h"

// I2Cdev and MPU6050 must be installed as libraries, or else the .cpp/.h files
// for both classes must be in the include path of your project
#include "I2Cdev.h"
#include "MPU6050.h"

// class default I2C address is 0x68
// specific I2C addresses may be passed as a parameter here
// AD0 low = 0x68 (default for InvenSense evaluation board)
// AD0 high = 0x69
MPU6050 accelgyro;
I2Cdev   I2C_M;

void get_one_sample_date_mxyz();
void getAccel_Data(void);
void getGyro_Data(void);
void PID();

uint8_t buffer_m[6];


int16_t ax, ay, az;
int16_t gx, gy, gz;
int16_t   mx, my, mz;





float Axyz[3];
float Gxyz[3];
float Mxyz[3];


#define sample_num_mdate  5000      

void setup() {
  // join I2C bus (I2Cdev library doesn't do this automatically)
  Wire.begin();

  // initialize serial communication
  // (38400 chosen because it works as well at 8MHz as it does at 16MHz, but
  // it's really up to you depending on your project)
  Serial.begin(38400);
  pinMode(A0, OUTPUT);
  pinMode(A1, OUTPUT);
  // initialize device
  Serial.println("Initializing I2C devices...");
  accelgyro.initialize();

  // verify connection
	Serial.println("Testing device connections...");
	Serial.println(accelgyro.testConnection() ? "MPU6050 connection successful" : "MPU6050 connection failed");
	
	delay(1000);
	Serial.println("     ");
 
	//Mxyz_init_calibrated ();
  
}

void loop() 
{   
	
	getAccel_Data();
	//getGyro_Data();
  Axyz[0] = (Axyz[0]*90) + 90;    
	//Serial.print("Accel(g):  ");
	//Serial.println(Axyz[0]); 
  PID();


 
	/*Serial.print(" ");
	Serial.print(Axyz[1]); 
	Serial.print(" ");
	Serial.print(Axyz[2]);Serial.print("\t");*/

}
  //create a PID that set motor direction to 1 if error is positive and 0 if error is negative
void PID(){
  int position = Axyz[0];
  int setpoint = 91;
  int error = setpoint - position;
  if (error > 10){
    analogWrite(A1, 0);
    analogWrite(A0, 1023);
  }
  else if (error < -10){
    analogWrite(A0, 0);
    analogWrite(A1, 1023);
  }
  
}



void getAccel_Data(void)
{
  accelgyro.getMotion9(&ax, &ay, &az, &gx, &gy, &gz, &mx, &my, &mz);
  Axyz[0] = (double) ax / 16384;
  Axyz[1] = (double) ay / 16384;
  Axyz[2] = (double) az / 16384; 
}

void getGyro_Data(void)
{
  accelgyro.getMotion9(&ax, &ay, &az, &gx, &gy, &gz, &mx, &my, &mz);
  Gxyz[0] = (double) gx * 250 / 32768;
  Gxyz[1] = (double) gy * 250 / 32768;
  Gxyz[2] = (double) gz * 250 / 32768;
}
