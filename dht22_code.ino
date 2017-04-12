//https://learn.adafruit.com/dht/using-a-dhtxx-sensor
#include "DHT.h"
#define DHTTYPE DHT22 

//which pins the sensors are attached to
#define SENSOR_1 2
#define SENSOR_2 3
#define SENSOR_3 4

#define DELAY 2000

DHT dht_1(SENSOR_1,DHTTYPE);
DHT dht_2(SENSOR_2,DHTTYPE);
DHT dht_3(SENSOR_3,DHTTYPE);

void setup(){
  Serial.begin(9600);
  Serial.print("Getting data from Sensors");
  dht_1.begin();
  //dht_2.begin();
  //dht_3.begin();
}

void loop(){
  
  //sensor 1
  float humidity_1 = dht_1.readHumidity();
  float temp_1 = dht_1.readTemperature(false); //true for F
  
  if(isnan(humidity_1) || isnan(temp_1)){
    Serial.println("Sensor 1 isn't working properly");
  }
  else{
    Serial.print("Humidity from Sensor 1: "); Serial.print(humidity_1); Serial.print("%\t");
    Serial.print("Temp from Sensor 1: "); Serial.print(temp_1); Serial.print(" C\n");
  }
  
  /*
  
  //sensor 2
  float humidity_2 = dht_2.readHumidity();
  float temp_2 = dht_2.readTemperature(false); //true for F
  
  if(isnan(humidity_2) || isnan(temp_2)){
    Serial.println("Sensor 2 isn't working properly");
  }
  else{
    Serial.print("Humidity from Sensor 2: "); Serial.print(humidity_2); Serial.print("%\t");
    Serial.print("Temp from Sensor 2: "); Serial.print(temp_2); Serial.print(" C\n");
  }
  
  //sensor 3
  float humidity_3 = dht_3.readHumidity();
  float temp_3 = dht_3.readTemperature(false); //true for F
  
  if(isnan(humidity_3) || isnan(temp_3)){
    Serial.println("Sensor 3 isn't working properly");
  }
  else{
    Serial.print("Humidity from Sensor 3: "); Serial.print(humidity_3); Serial.print("%\t");
    Serial.print("Temp from Sensor 3: "); Serial.print(temp_3); Serial.print(" C\n");
  }
  
  */
  
  delay(DELAY);
}
