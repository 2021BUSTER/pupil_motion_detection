int FSRsensor0 = A0;
int FSRsensor1 = A1;
int FSRsensor2 = A2;
int FSRsensor3 = A3;
int FSRsensor4 = A4;
int FSRsensor5 = A5;
int FSRsensor6 = A6;
int FSRsensor7 = A7;
int FSRsensor8 = A8;

int value0 = 0;
int value1 = 0;
int value2 = 0;
int value3 = 0;
int value4 = 0;
int value5 = 0;
int value6 = 0;
int value7 = 0;
int value8 = 0;

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
  Serial.println(value8);

  delay(5000);
}
