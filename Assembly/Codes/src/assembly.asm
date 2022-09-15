.include "/home/honey/m328Pdef.inc"
ldi r30, 0b00100000 ;identifying output pin 13
out DDRB,r30
ldi r16, 0b11110011  ;identifying input pins 2,3
out DDRD,r16          ;declaring pins as input
ldi r16,0b11111011   ;giving input
out PortD,r16
ldi r17,0b00000001
ldi r18,0b00000001

AND r17,r16    ;r17=x1
LSR r16
AND r18,r16    ;r18=x2

mov r0,r17    ;r0=x1
AND r0,r18    ;r0=x1&&x2

mov r1,r0    ;r1=x1&&x2
AND r1,r17    ;r1=A&&x1

mov r2,r0    ;r2=x1&&x2
AND r2,r18  ;r2=A&&x2

mov r3,r1    ;r3=A&&x1
AND r3,r2    ;r3=B&&C

mov r30,r3         ;r30=0000000Y
LSL r30               ;r30=000000Y0
LSL r30               ;r30=00000Y00
LSL r30               ;r30=0000Y000
LSL r30               ;r30=000Y0000
LSL r30               ;r30=00Y00000
out PortB,r30

Start:
rjmp Start
