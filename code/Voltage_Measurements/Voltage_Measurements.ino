const int voltagePin_1 = 34;
const int voltagePin_2 = 32;
const int voltagePin_3 = 26;

void setup() {
  Serial.begin(115200);
}

void loop() {
  // Volatage for battery_1:
  int sensorValue1 = analogRead(voltagePin_1);
  float voltage1 = sensorValue1 * (3.3 / 4095.0);
  // Volatage for battery_2:
  int sensorValue2 = analogRead(voltagePin_2);
  float voltage2 = sensorValue2 * (3.3 / 4095.0);
  // Volatage for battery_3:
  int sensorValue3 = analogRead(voltagePin_3);
  float voltage3 = sensorValue3 * (3.3 / 4095.0);

  // Print out the value you read:
  Serial.println("Voltage_1: ");
  Serial.print(voltage1);
  Serial.print("V");
  Serial.print(" ");

  Serial.print("Voltage_2: ");
  Serial.print(voltage2);
  Serial.print("V");
  Serial.print(" ");

  Serial.print("Voltage_2: ");
  Serial.println(voltage3);
  Serial.print("V");

  delay(10);
}
