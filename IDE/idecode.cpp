#include<Arduino.h>
int x1=0, x2=0;
int A,B,C,D,Y;
void setup()
{
  pinMode(13,OUTPUT);

}

void loop() {
  digitalRead(x1);
  digitalRead(x2);
  A=(x1&&x2);
  B=(A&&x1);
  C=(A&&x2);
  D=(B&&C);
  Y=(D);
  digitalWrite(13,Y);
  delay(500);

}
