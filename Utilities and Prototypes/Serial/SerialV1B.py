/* 
Title:
Version:
Developer:
Description:
Recieves infromation from the serial port process the info and updates the digital outputs and analog inputs

THE CIRCUIT
In
  Serial TR,RX
  Analog input 0

Out
  Channel1
  Channel2
  Channel3
  Channel4
  Channel5
Note: The Arduino board is 5V based, the Raspberry pi board is 3.3V based. In order to couple the voltage between 
the two boards it was required to use a voltage devider between the TX of the arduino and the RX of the Pi. The
resistors used where 4k7 and 2k5

COMMANDS
Queries from Raspberry        Replies from Arduino      Command
Arduino Status
Read pressure
*/


/*-----( Import needed libraries )-----*/
/*-----( Declare Constants and Pin Numbers )-----*/
#define led 13  // built-in LED
/*-----( Declare objects )-----*/
/*-----( Declare Variables )-----*/
int ByteReceived;

//--(end setup )---


void setup()   /****** SETUP: RUNS ONCE ******/
{
  Serial.begin(9600);  
  Serial.println("--- Start Serial Monitor SEND_RCVE ---");
    Serial.println(" Type in Box above, . ");
  Serial.println("(Decimal)(Hex)(Character)");  
  Serial.println(); 
}



void loop()   /****** LOOP: RUNS CONSTANTLY ******/
{
  if (Serial.available() > 0)
  {
    ByteReceived = Serial.read();
    Serial.print(ByteReceived);   
    Serial.print("        ");      
    Serial.print(ByteReceived, HEX);
    Serial.print("       ");     
    Serial.print(char(ByteReceived));
    
    if(ByteReceived == '1') // Single Quote! This is a character.
    {
      digitalWrite(led,HIGH);
      Serial.print(" LED ON ");
    }
    
    if(ByteReceived == '0')
    {
      digitalWrite(led,LOW);
      Serial.print(" LED OFF");
    }
    
    Serial.println();    // End the line

  // END Serial Available
  }

  //to do elements


}

//--(end main loop )---

/*-----( Declare User-written Functions )-----*/

/*********( THE END )***********/























































#!/usr/bin/python

import serial



ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.open()

ser.write("testing")

try:
    while 1:
        response = ser.readline()
        print response

except KeyboardInterrupt:
    ser.close()