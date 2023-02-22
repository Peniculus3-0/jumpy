SoftwareSerial hc06(2,3);
/*
Setup the bluetooth device
*/
void setupBluetooth()  {
    // Define pin modes for TX and RX
    pinMode(rxPin, INPUT);
    pinMode(txPin, OUTPUT);
    
    // Set the baud rate for the SoftwareSerial object
    mySerial.begin(9600);
}
/*
Read Bluetooth signal
*/
void readBluetooth() {
    if (mySerial.available() > 0) {
        mySerial.read();
    }
}