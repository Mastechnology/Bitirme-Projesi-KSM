int capasitive = 10;
int stateCap = LOW;

void setup() {
  
  Serial.begin(9600);
  pinMode(capasitive,INPUT);
  
}

void loop() {
  
  int val = digitalRead(capasitive);
  
  if( val != stateCapCap ){
     stateCapCap = val;
     Serial.print("Sensor value = ");
     if( stateCapCap == 0 )
       Serial.println( "(0) Target Hit!" );
     else
       Serial.println( "(1) None");
  }
}
