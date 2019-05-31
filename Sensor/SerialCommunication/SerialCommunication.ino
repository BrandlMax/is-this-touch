void setup()
{
  Serial.begin(115200);

  // Analog
  pinMode(0, INPUT);
}

void loop()
{
  // Analog Pin
  Serial.println(7);
  Serial.println(1);
  Serial.println(2);
  Serial.println(3);
  Serial.println(4);
  delay(1);
}
