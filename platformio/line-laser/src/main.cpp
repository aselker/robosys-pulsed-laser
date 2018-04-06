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

int laserPin = PB1;
char in = '0';

void setup()
{
  pinMode(laserPin, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);

  //Serial.begin(9600);
  usb.begin(115200);

}

void loop() {

  while (usb.available()) {
    in = usb.read();
    usb.println(in); //Acknowledge that we got it
  }

  //analogWrite(laserPin, (unsigned int)in);
  digitalWrite(laserPin, (in == '0') ? LOW : HIGH);
  digitalWrite(LED_BUILTIN, (in == '0') ? HIGH : LOW);

  //usb.println(in + '0'); //Print the char's ASCII value

  delay(10);
}
  
