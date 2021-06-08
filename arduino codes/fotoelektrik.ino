int fotoelektrik = 8;
int stateFoto = LOW;
int valueFoto;

void setup(){
    Serial.begin(9600);
    pinMode(fotoelektrik, INPUT);
}
void loop(){
    valueFoto = digitalRead(fotoelektrik);
    if(valueFoto == HIGH){
        Serial.println("Cisim Tespit Edildi!");
    }
    else if (valueFoto == LOW){
        Serial.println("Cisim tespiti yapilamadi!");
    }
}