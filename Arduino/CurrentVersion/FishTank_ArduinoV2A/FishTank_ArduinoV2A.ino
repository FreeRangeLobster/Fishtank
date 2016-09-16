//Title:FishTank_Arduino_board
//Version             Description                          Date                       Changes
//1A              Testing communication with Pi         04/03/2016               Initial program
//Date: 04/03/2016
//Developer: Juan Vivas, www.freerangelobster.blogspot.co.uk, 
//Description:
//Recieves information from Raspberry Pi using the serial port. Updates 5 PWM channelsupdates the digital
//outputs and analog inputs
//For debugging purposes the SW serial por has been included, to enable it, set debug variable to 1
//Based on: Arduino code samples
//THE CIRCUIT
//In
//  Serial TR,RX:
//  Serial SW:
//  Analog input 0:
//Out
//  Channel1
//  Channel2
//  Channel3
//  Channel4
//  Channel5
//Note: The Arduino board is 5V based, the Raspberry pi board is 3.3V based. In order to couple the voltage between 
//the two boards it was required to use a voltage devider between the TX of the arduino and the RX of the Pi. The
//resistors used where 4k7 and 2k5
//COMMANDS
//Queries from Raspberry        Replies from Arduino      Command
//- Arduino Status       [Ch status, Pres] 1 1 1 1 1 9999    S
//- Get Pressure                      P xxxx                 P
//- Channel1 On                       _Ch1ON                Ch1ON
//- Channel2 On                       _Ch2ON                Ch2ON
//- Channel3 On                       _Ch3ON                Ch3ON
//- Channel4 On                       _Ch4ON                Ch4ON
//- Channel5 On                       _Ch5ON                Ch5ON
//- Channel1 Off                      _Ch1OFF               Ch1OFF
//- Channel2 Off                      _Ch2OFF               Ch2OFF
//- Channel3 Off                      _Ch3OFF               Ch3OFF
//- Channel4 Off                      _Ch4OFF               Ch4OFF
//- Channel5 Off                      _Ch5OFF               Ch5OFF
                 
//Software serial enabled for debugging proposes
//*/

int inByte;
String readString;
boolean Ch1=0;
boolean Ch2=0;
boolean Ch3=0;
boolean Ch4=0;
boolean Ch5=0;
int Pressure=0;
//Outputs of the board
int Ch1Pin=8;
int Ch2Pin=9;
int Ch3Pin=10;
int Ch4Pin=11;
int Ch5Pin=12;
int BoardLED=13;
//PWM values
int Ch1PWM=0;
int Ch2PWM=0;
int Ch3PWM=0;
int Ch4PWM=0;
int Ch5PWM=0;



void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(BoardLED, OUTPUT);
  pinMode(Ch1Pin, OUTPUT);
  pinMode(Ch2Pin, OUTPUT);
  pinMode(Ch3Pin, OUTPUT);
  pinMode(Ch4Pin, OUTPUT);
  Serial.println("GameOn");
}

void loop() {
  //Reads serial port and fills a sting variable readString 
  while( Serial.available()){
    delay(3);  
    char c = Serial.read();
    readString += c;   
   }
  
  //Eliminates extra characteres from the string.
  readString.trim();
  
  if (readString.length() >0) {

    
    //Instruction 1 prototype testing   
    if (readString == "on"){
        Serial.println("switching on");
        digitalWrite(13, HIGH);
    }

   //Instruction 1 prototype testing        
    else if  (readString == "off"){
        Serial.println("switching off");
        digitalWrite(13, LOW);
    }

    // Arduino Status           
    else if (readString == "S"){
      	Pressure = analogRead(A0);
        Serial.print(Ch1);
      	Serial.print(Ch2);
      	Serial.print(Ch3);
      	Serial.print(Ch4);
      	Serial.print(Ch5);
      	Serial.print("-");
      	Serial.println(analogRead(A0));
      
       //%b  %d",Ch1,Ch2,Pressure );
        //digitalWrite(13, HIGH);
    }  
      
     //Get Pressure                 
    else if (readString == "P"){
        //read pressure sensor
       Serial.println("P ");
       Serial.println(analogRead(A0));
       //digitalWrite(13, HIGH);
    }


    //Channe1 On                  
    else if (readString == "Ch1ON"){
        //read pressure sensor
       Serial.println("_Ch1ON");
       //digitalWrite(13, HIGH);
       Ch1=1;
    }
    
   //Channel 2 On 
    else if (readString == "Ch2ON"){
        //read pressure sensor
       Serial.println("_Ch2ON");
       //digitalWrite(13, HIGH);
       Ch2=1;
    }
    
   //Channel 3 On
    else if (readString == "Ch3ON"){
        //read pressure sensor
       Serial.println("_Ch3ON");
       //digitalWrite(13, HIGH);
       Ch3=1;
    }
    
   //Channel 4 On                     
    else if (readString == "Ch4ON"){
        //read pressure sensor
       Serial.println("_Ch4ON");
       //digitalWrite(13, HIGH);
       Ch4=1;
    }
    
   //Channel 5 On                  
    else if (readString == "Ch5ON"){
        //read pressure sensor
       Serial.println("_Ch5ON");
       digitalWrite(13, HIGH);
       Ch5=1;
    }
    
   //Channel 1 Off                  
    else if (readString == "Ch1OFF"){
        //read pressure sensor
       Serial.println("_Ch1OFF");
       //digitalWrite(13, HIGH);
       Ch1=0;
    }
    
   //Channel 2 Off
   else if (readString == "Ch2OFF"){
        //read pressure sensor
       Serial.println("_Ch2OFF");
       //digitalWrite(13, HIGH);
       Ch2=0;
    }
    
   // Channel 3 Off
    else if (readString == "Ch3OFF"){
        //read pressure sensor
       Serial.println("_Ch3OFF");
       //digitalWrite(13, HIGH);
       Ch3=0;
    }
    
   // Channel 4 Off
    else if (readString == "Ch4OFF"){
        //read pressure sensor
       Serial.println("_Ch4OFF");
       //digitalWrite(13, HIGH);
       Ch4=0;
    }
    
   //Channel 5 Off
   else if (readString == "Ch5OFF"){
        //read pressure sensor
       Serial.println("_Ch5OFF");
       digitalWrite(13, LOW);
       Ch5=0;
   }
     
   else 
	Serial.println("Unknown Command"); 
   }
   
   //clears the string buffer
   readString="";
 
    
 

  //Channel 1 PWM
  if (Ch1==1){
        if(Ch1PWM<255){ 
        analogWrite(BoardLED,Ch1PWM ); 
        analogWrite(Ch1Pin,Ch1PWM ); 
        Ch1PWM=Ch1PWM+1;
       }
  }
  
  if (Ch1==0){
      if(Ch1PWM>0){ 
        analogWrite(BoardLED, Ch1PWM); 
        analogWrite(Ch1Pin,Ch1PWM );
        Ch1PWM=Ch1PWM-1;
        }
   }

  //Channel 2
  if (Ch2==1){
        if(Ch2PWM<255){ 
        analogWrite(BoardLED,Ch2PWM ); 
        analogWrite(Ch2Pin,Ch2PWM ); 
        Ch2PWM=Ch2PWM+1;
       }
  }
  
  if (Ch2==0){
      if(Ch2PWM>0){ 
        analogWrite(BoardLED, Ch2PWM); 
        analogWrite(Ch2Pin,Ch2PWM );
        Ch2PWM=Ch2PWM-1;
        }
  }

  
  //Channel 3
  if (Ch3==1){
        if(Ch3PWM<255){ 
        analogWrite(BoardLED,Ch3PWM ); 
        analogWrite(Ch3Pin,Ch3PWM ); 
        Ch3PWM=Ch3PWM+1;
       }
  }
  
  if (Ch3==0){
      if(Ch3PWM>0){ 
        analogWrite(BoardLED, Ch3PWM); 
        analogWrite(Ch3Pin,Ch3PWM );
        Ch3PWM=Ch3PWM-1;
        }
  }

     
  //Channel 4
  if (Ch4==1){
        if(Ch4PWM<255){ 
        analogWrite(BoardLED,Ch4PWM ); 
        analogWrite(Ch4Pin,Ch4PWM ); 
        Ch4PWM=Ch4PWM+1;
       }
  }
  
  if (Ch4==0){
      if(Ch4PWM>0){ 
        analogWrite(BoardLED, Ch4PWM); 
        analogWrite(Ch4Pin,Ch4PWM );
        Ch4PWM=Ch4PWM-1;
        }
  }


        
  //Channel 5
  if (Ch5==1){
        if(Ch5PWM<255){ 
        analogWrite(BoardLED,Ch5PWM ); 
        analogWrite(Ch5Pin,Ch5PWM ); 
        Ch5PWM=Ch5PWM+1;
       }
  }
  
  if (Ch5==0){
      if(Ch5PWM>0){ 
        analogWrite(BoardLED, Ch5PWM); 
        analogWrite(Ch5Pin,Ch5PWM );
        Ch5PWM=Ch5PWM-1;
        }
   }
	
 

  delay(1); 
  } 


