#include <avr/io.h>
#include<stdbool.h>
#include <util/delay.h>
void sevenseg(int);
int main (void)
{
  bool x1=0,x2=1;
  bool a,b,c,d,y;
  while(1)
  {
     DDRD   =0b00100000;
     a=(x1&&x2);
     b=(x1&&a);
     c=(x2&&a);
     d=(b&&c);
     y=(d);
     PORTD|=(y<<4);
  }
  return 0;
}
