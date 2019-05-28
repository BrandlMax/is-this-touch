void setup()
{
  Serial.begin(115200);

  // Analog
  pinMode(A0, INPUT);
}

void loop()
{
  // put your main code here, to run repeatedly:

  // Analog Pin
  Serial.println(analogRead(A0));
  delay(10);
}
