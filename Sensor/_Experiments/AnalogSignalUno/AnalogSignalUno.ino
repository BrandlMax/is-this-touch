void setup()
{
    Serial.begin(115200);

    // Analog
    pinMode(9, OUTPUT); //-Signal generator pin
    pinMode(8, OUTPUT); //-Sync (test) pin

    // pinMode(0, INPUT);
}

void loop()
{
    // put your main code here, to run repeatedly:

    // Analog Pin
    Serial.println(analogRead(0));
    digitalWrite(9, !digitalRead(9));
}
