#include <Arduino.h>
#include <Servo.h>
#include <U8g2lib.h>
#include <Wire.h>

Servo ESC;
U8G2_SSD1306_64X32_1F_F_HW_I2C u8g2(U8G2_R0, /* reset=*/ U8X8_PIN_NONE);

int potValue;

void setup() {
      ESC.attach(3, 1000, 2000);
      u8g2.begin();
      u8g2.setFont(u8g2_font_profont22_tf);
}

void loop()
{
      potValue = analogRead(A1);
      potValue = map(potValue, 0, 1023, 0, 180);
      u8g2.clearBuffer();
      u8g2.setCursor(10, 30);
      u8g2.print(potValue);
      u8g2.sendBuffer();
      ESC.write(potValue);
      // delay(100);
}

