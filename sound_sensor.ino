// test code for Grove - Sound Sensor
// loovee @ 2016-8-30

const int pinAdc = A0;

void setup()
{
    Serial.begin(115200);
    //Serial.println("Grove - Sound Sensor Test...");
}

void loop()
{
    long sum = 0;
    for(int i=0; i<32; i++)
    {
        sum += analogRead(pinAdc);
    }

    sum >>= 5;

    //Serial.println(sum);
    Serial.write(sum); //writes the voltage to the serial port so python can pick it up
    //essentially this is writing 1024 bits to serial every 10ms
    delay(10);
}
