// rewritten by @brandlmax
void SendData(int Command, unsigned int yValue, unsigned int xValue)
{
  Serial.println(xValue);
}

void PlottArray(unsigned int Cmd, float Array1[], float Array2[])
{
  Serial.println(999); // Divider
  delay(1);
  for (int x = 0; x < sizeOfArray; x++)
  {
    SendData(Cmd, round(Array1[x]), round(Array2[x]));
  }
}
