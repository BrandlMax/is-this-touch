int x1 = 0;
int x2 = 0;
int x3 = 0;
int x4 = 0;

int l = 0;
void setup()
{
  Serial.begin(115200);

  // Analog
  pinMode(0, INPUT);
}

void loop()
{
  x1 = 1 + x1;
  x2 = 1 + x2;
  x3 = 1 + x3;
  x4 = 1 + x4;
  
  // Analog Pin
  Serial.println(999);
  // Serial.println(x1);
  // Serial.println(x2);
  // Serial.println(x3);
  // Serial.println(x4);
  sendData();

}

void sendData(){
  delay(10);
  l = l + 1;
  for (int x = 0; x < 160; x++)
    {
      Serial.println(x + l);
    }
  
  // Serial.println(x2);
  // Serial.println(x3);
  // Serial.println(x4);
}
