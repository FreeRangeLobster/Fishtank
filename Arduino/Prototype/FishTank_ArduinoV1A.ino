/* 
Title:FishTank_Arduino_board

Version             Description                          Date                       Changes
1A              Testing communication with Pi         04/03/2016               Initial program

Date: 04/03/2016

Developer: Juan Vivas, www.freerangelobster.blogspot.co.uk, 

Description:
Recieves information from Raspberry Pi using the serial port. Updates 5 PWM channelsupdates the digital
outputs and analog inputs
For debugging purposes the SW serial por has been included, to enable it, set debug variable to 1
Based on: Arduino code samples


THE CIRCUIT
In
  Serial TR,RX:
  Serial SW:
  Analog input 0:

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

Software serial enabled for debugging proposes
*/



void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:

}
