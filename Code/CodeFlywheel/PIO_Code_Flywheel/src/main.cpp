#include <Arduino.h>
#include <Servo.h>
#include <U8g2lib.h>
#include <Wire.h>
#include <Stepper.h>

#define STEPS 32
#define REDUCTION_RATIO 64
#define STEPS_PER_REVOLUTION (STEPS * REDUCTION_RATIO)

Servo ESC;
U8G2_SSD1306_64X32_1F_F_HW_I2C u8g2(U8G2_R0, /* reset=*/ U8X8_PIN_NONE);
Stepper stepper(STEPS, 8, 10, 9, 11);
int potValue;

void PrintScreen(int potValue, int steps);

void setup() {
      Serial.begin(9600);
      ESC.attach(3, 1000, 2000);
      u8g2.begin();
      u8g2.setFont(u8g2_font_profont12_tf);
}

void loop()
{
      potValue = analogRead(A1);
      potValue = map(potValue, 0, 1023, 0, 180);
      
      int steps;
      int totalSteps;

      stepper.setSpeed(300);
      stepper.step(-10000);


      // if (Serial.available() > 0) {
      //       steps = Serial.parseInt();
      //       stepper.step(steps);
      // }
      ESC.write(potValue);

      PrintScreen(potValue, totalSteps += steps);
      // delay(100);
}

void PrintScreen(int potValue, int steps)
{
      u8g2.clearBuffer();
      char buf_stp[20];
      sprintf(buf_stp, "STP : %d", steps);
      u8g2.setCursor(10, 20);
      u8g2.print(buf_stp);

      u8g2.setCursor(10, 30);
      char buf_pot[20];
      sprintf(buf_pot, "POT : %d", potValue);
      u8g2.print(buf_pot);      
      u8g2.sendBuffer();
}


