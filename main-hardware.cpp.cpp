#include <Arduino.h>
#include <Bounce2.h>
#define BUTTON 34
Bounce debouncer = Bounce();
int count=0;
void setup()
{
     Serial.begin(9600);
  delay(1000); // give me time to bring up serial monitor
  Serial.println("BUTTON");
  debouncer.attach(BUTTON, INPUT_PULLUP);
  debouncer.interval(25); 
  delay(200);
}

void loop()
{
    debouncer.update();
      if (debouncer.fell()) 
      { 
        count++;
        Serial.println(count);
      }
}