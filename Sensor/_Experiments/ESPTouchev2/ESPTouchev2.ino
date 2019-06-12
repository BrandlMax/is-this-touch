    

// Arduino Version by:
//****************************************************************************************
// Illutron take on Disney style capacitive touch sensor using only passives and Arduino
// Dzl 2012
//****************************************************************************************
// ESP take on by @brandlmax

//                              10n
// PIN 9 --[10k]-+-----10mH---+--||-- OBJECT
//               |            |
//              3.3k          |
//               |            V 1N4148 diode
//              GND           |
//                            |
//Analog 0 ---+------+--------+
//            |      |
//          100pf   1MOmhm
//            |      |
//           GND    GND


#define N 160 //How many frequencies

float results[N];            //-Filtered result buffer
float freq[N];            //-Filtered result buffer
int sizeOfArray = N;

void setup()
{
  
  pinMode(13,OUTPUT);        //-Signal generator pin
  pinMode(15,OUTPUT);        //-Sync (test) pin

  Serial.begin(115200);

  for(int i=0;i<N;i++)      //-Preset results
    results[i]=0;         //-+
}

void loop()
{
  unsigned int d;

  int counter = 0;
  for(unsigned int d=0;d<N;d++)
  {
    int v = analogRead(A0);    //-Read response signal
    delayMicroseconds(1);
    results[d]=results[d]*0.5+(float)(v)*0.5; //Filter results
   
    freq[d] = d;
  } 
      
      PlottArray(1,freq,results);
      digitalWrite(13, !digitalRead(13));
      digitalWrite(15, !digitalRead(15));
}
   

   
    
 
