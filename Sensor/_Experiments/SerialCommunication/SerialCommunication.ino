void setup()
{
  Serial.begin(115200);

  // Analog
  pinMode(0, INPUT);
}

void loop()
{
  int x1 = 1 + random(0, 2);
  int x2 = 2 + random(0, 2);
  int x3 = 3 + random(0, 2);
  int x4 = 4 + random(0, 2);
  
  // Analog Pin
  Serial.println(7);
  Serial.println(x1);
  Serial.println(x2);
  Serial.println(x3);
  Serial.println(x4);
  delay(1);
}
