#include <Arduino.h>
#include <Stepper.h>

#define STEPS 32

// create an instance of the stepper class using the steps and pins

Stepper stepper(STEPS, 8, 10, 9, 11);

void setup()
{
  Serial.begin(9600);
  Serial.println("serial begin");
}

void loop()
{
  stepper.setSpeed(1220);
  stepper.step(-10000);
}
