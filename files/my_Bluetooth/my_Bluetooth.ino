char inputByte;

void setup() {
 Serial.begin(9600);
 pinMode(13,OUTPUT);
 digitalWrite(13,HIGH);
}

void loop() {
  while(Serial.available()>0){

      inputByte = Serial.read();
      Serial.println(inputByte);

      if (inputByte=='1'){
      digitalWrite(13,HIGH);
    }

    else if (inputByte=='0'){
      digitalWrite(13,LOW);
      } 
    }
}
