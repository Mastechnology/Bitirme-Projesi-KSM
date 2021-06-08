int inductive=10;
int stateInd= LOW;
int valueInd;
int valueInd2;
void setup()
{
Serial.begin(9600);
pinMode(inductive,INPUT);
 
}
void loop()
{
valueInd = digitalRead(inductive);
valueInd2 =analogRead(inductive);
if(valueInd!=stateInd)
{
  stateInd=valueInd;
  Serial.println(valueInd2);
  if (stateInd==0)
  {
    Serial.println("target detected");
    
  }
    
   else{
     Serial.println("No target detected");
    }
 }
}