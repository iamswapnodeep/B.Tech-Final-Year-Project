#include <OneWire.h>
#include <DallasTemperature.h>

// pins used for voltage measurements:
const int voltagePin_1 = 35;
const int voltagePin_2 = 32;
const int voltagePin_3 = 33;
const int tempPin = 16;
const int currentSensorPin = 27;
unsigned int x = 0;

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(tempPin);
// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature sensors(&oneWire);

void setup() {
  Serial.begin(115200);
  sensors.begin();
}

void loop() {
  // <-- VOLTAGE MEASUREMENTS -->
  // Volatage for battery_1:
  int sensorValue1 = analogRead(voltagePin_1);
  float voltage1 = sensorValue1 * (3.3 / 4095.0);
  // Volatage for battery_2:
  int sensorValue2 = analogRead(voltagePin_2);
  float voltage2 = sensorValue2 * (3.3 / 4095.0);
  // Volatage for battery_3:
  int sensorValue3 = analogRead(voltagePin_3);
  float voltage3 = sensorValue3 * (3.3 / 4095.0);
  // <-- TEMPERATURE MEASUREMENTS -->
  float AcsValue=0.0,Samples=0.0,AvgAcs=0.0,AcsValueF=0.0;
  for(int x = 0; x < 150; x++){ //Get 150 samples
     AcsValue = analogRead(currentSensorPin); //Read current sensor values 
     Samples = Samples + AcsValue; //Add samples together
     delay(3); //let ADC settle before next sample 3ms
  }
  AvgAcs=Samples/150.0;//Taking Average of Samples
  AcsValueF = (1.42 - (AvgAcs * (3.3 / 4095.0)) ) / 0.1;
  // <-- TEMPERATURE MEASUREMENTS -->
  sensors.requestTemperatures(); 
  float temperatureC = sensors.getTempCByIndex(0);
  float temperatureF = sensors.getTempFByIndex(0);

  // Print out the voltage value you read:
  Serial.print("Voltage_1: ");
  Serial.print(voltage1);
  Serial.print("V");
  Serial.print("\t");
  Serial.print("Voltage_2: ");
  Serial.print(voltage2);
  Serial.print("V");
  Serial.print("\t");
  Serial.print("Voltage_3: ");
  Serial.print(voltage3);
  Serial.print("V");
  Serial.println("\n");
  //Print the current Value in ampere
  Serial.print("Current: ");
  Serial.print(AcsValueF);
  Serial.print("V");
  Serial.println("\n");
  //Print the temp value:
  Serial.print("Temperature in ºC: ");
  Serial.print(temperatureC);
  Serial.print("ºC");
  Serial.print("\t");
  Serial.print("Temperature in ºF: ");
  Serial.print(temperatureF);
  Serial.print("ºF");
  Serial.println("\n");

  delay(10000);
}
