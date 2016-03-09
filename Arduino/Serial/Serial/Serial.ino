void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    //int incoming = Serial.read();
    //Serial.print("character recieved: ");
    //Serial.print(incoming, DEC);
    Serial.write(Serial.read());
  }
}

/*
int number = 0;
int val=48;


void setup(){
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop(){
  val=val+1;
  //Serial.write("Hello"); 
  //if (Serial.available()) {
  //  number = Serial.read();
   Serial.print("recieved");
    
    //Serial.println(number, DEC);
    delay(250);
    Serial.print(val);       // print as an ASCII-encoded decimal - same as "DEC"
    Serial.print("\t"); 
    digitalWrite(13, HIGH);
  //}
     delay(250);
     digitalWrite(13, LOW);
     
     
}
*/
