int relay1 = 12;
int relay2 = 11;
int relay3 = 10;
int relay4 = 9;
char input;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(relay1,OUTPUT);
pinMode(relay2,OUTPUT);
pinMode(relay3,OUTPUT);
pinMode(relay4,OUTPUT);
Serial.print("press Y to turn ON the LED\n press N to turn OFF the LED");
}

void loop() {
  input = Serial.read();
  if(input == 'Q'){
    digitalWrite(relay1,HIGH);
  }
  if(input == 'W'){
    digitalWrite(relay1,LOW);
  }
    if(input == 'E'){
    digitalWrite(relay2,HIGH);
  }
  if(input == 'R'){
    digitalWrite(relay2,LOW);
  }
    if(input == 'T'){
    digitalWrite(relay3,HIGH);
  }
  if(input == 'Y'){
    digitalWrite(relay3,LOW);
  }
    if(input == 'U'){
    digitalWrite(relay4,HIGH);
  }
  if(input == 'I'){
    digitalWrite(relay4,LOW);
  }
  if(input == 'A'){
    digitalWrite(relay1,LOW);
    digitalWrite(relay2,LOW);
    digitalWrite(relay3,LOW);
    digitalWrite(relay4,LOW);
  }
    if(input == 'a'){
    digitalWrite(relay1,HIGH);
    digitalWrite(relay2,HIGH);
    digitalWrite(relay3,HIGH);
    digitalWrite(relay4,HIGH);
  }
  // put your main code here, to run repeatedly:

}
