/**
 * Blink
 *
 * Turns on an LED on for one second,
 * then off for one second, repeatedly.
 */
#include "Arduino.h"

// Set LED_BUILTIN if it is not defined by Arduino framework
#define LED_BUILTIN PC13

USBSerial usb;

int laserPin = LED_BUILTIN;
char in = '0';

void setup()
{
  pinMode(laserPin, OUTPUT);

  //Serial.begin(9600);
  usb.begin(115200);

  while (usb.available()) usb.read(); //Flush the buffer
}

void loop() {

  while (usb.available()) in = usb.read();

  //analogWrite(laserPin, (unsigned int)in);
  digitalWrite(laserPin, (in == '0') ? HIGH : LOW);

  usb.println(in);

  delay(1000);
}
  
