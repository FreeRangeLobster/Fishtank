int number = 0;
int val=48;

void setup(){
Serial.begin(9600);
}

void loop(){
  //val=val+1;
  Serial.write("Hello"); 
  if (Serial.available()) {
    number = Serial.read();
    Serial.print("recieved");
    
    //Serial.println(number, DEC);
    //delay(500);
  }
     delay(500);
}
