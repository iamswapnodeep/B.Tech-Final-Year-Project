unsigned int x = 0;
const int currentSensorPin = 27;
void setup(){
  Serial.begin(115200);
}

void loop(){
  float AcsValue=0.0,Samples=0.0,AvgAcs=0.0,AcsValueF=0.0;
  for(int x = 0; x < 150; x++){ //Get 150 samples
     AcsValue = analogRead(currentSensorPin); //Read current sensor values 
     Samples = Samples + AcsValue; //Add samples together
     delay(3); //let ADC settle before next sample 3ms
  }
  AvgAcs=Samples/150.0;//Taking Average of Samples
  AcsValueF = (1.42 - (AvgAcs * (3.3 / 4095.0)) ) / 0.1;
  //Serial.println(AvgAcs);
  Serial.println(AcsValueF);//Print the read current on Serial monitor
  delay(5000);
}