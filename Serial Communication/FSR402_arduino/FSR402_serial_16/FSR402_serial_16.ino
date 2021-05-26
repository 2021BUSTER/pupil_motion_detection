int FSRsensor0 = A0;
int FSRsensor1 = A1;
int FSRsensor2 = A2;
int FSRsensor3 = A3;
int FSRsensor4 = A4;
int FSRsensor5 = A5;
int FSRsensor6 = A6;
int FSRsensor7 = A7;
int FSRsensor8 = A8;

int FSRsensor9 = A9;
int FSRsensor9 = A11;
int FSRsensor10 = A10;
int FSRsensor12 = A12;
int FSRsensor13 = A13;
int FSRsensor14 = A14;
int FSRsensor15 = A15;

int value0 = 0;
int value1 = 0;
int value2 = 0;
int value3 = 0;
int value4 = 0;
int value5 = 0;
int value6 = 0;
int value7 = 0;
int value8 = 0;

int value9 = 0;
int value10 = 0;
int value11 = 0;
int value12 = 0;
int value13 = 0;
int value14 = 0;
int value15 = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  value0 = analogRead(FSRsensor0);
  value1 = analogRead(FSRsensor1);
  value2 = analogRead(FSRsensor2);
  value3 = analogRead(FSRsensor3);
  value4 = analogRead(FSRsensor4);
  value5 = analogRead(FSRsensor5);
  value6 = analogRead(FSRsensor6);
  value7 = analogRead(FSRsensor7);
  value8 = analogRead(FSRsensor8);
  
  value9 = analogRead(FSRsensor9);
  value10 = analogRead(FSRsensor10);
  value11 = analogRead(FSRsensor11);
  value12 = analogRead(FSRsensor12);
  value13 = analogRead(FSRsensor13);
  value14 = analogRead(FSRsensor14);
  value15 = analogRead(FSRsensor15);

  Serial.print(value0);
  Serial.print(",");
  Serial.print(value1);
  Serial.print(",");
  Serial.print(value2);
  Serial.print(",");
  Serial.print(value3);
  Serial.print(",");
  Serial.print(value4);
  Serial.print(",");
  Serial.print(value5);
  Serial.print(",");
  Serial.print(value6);
  Serial.print(",");
  Serial.print(value7);
  Serial.print(",");
  Serial.print(value8);
  Serial.print(",");

  Serial.print(value9);
  Serial.print(",");
  Serial.print(value10);
  Serial.print(",");
  Serial.print(value11);
  Serial.print(",");
  Serial.print(value12);
  Serial.print(",");
  Serial.print(value13);
  Serial.print(",");
  Serial.print(value14);
  Serial.print(",");
  Serial.println(value15);
 
  delay(5000);
}
