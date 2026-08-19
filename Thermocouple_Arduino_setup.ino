//This line adds the adafruit library required to communicate with the amplifier 
#include <Adafruit_MAX31856.h>

// This is for setting up the pins you wish to connect to on the Arduino 
Adafruit_MAX31856 max1=Adafruit_MAX31856(10, 11, 12, 13); 

void setup() {
  //This is where we start both the thermocouple and our serial output
  max1.begin();// For starting out thermocouple
  Serial.begin(115200);//You could change this Baud rate if you needed to this is just what work with my computer best
  max1.setThermocoupleType(MAX31856_TCTYPE_K);// This sets our thermocouple type, originally I used K type but this can be changed if necessary

}

void loop() {
  float temp = max1.readThermocoupleTemperature();// This assigns the output value from the MAX amp to the variable temp and ensures its a float
  Serial.println(temp);// This prints the temperature value 
  delay(1000);// This provides a delay inbetween measurements from the thermocouple, this is in ms so currently it is set to 1 second and I would not reccomend going less than that 

}
