# Inova Fitness SDS011 PM2.5 Sensor Python Parser

http://www.inovafitness.com/en/a/chanpinzhongxin/95.html

## Serial Interface

Bit rate: 9600  
Data bit: 8
Parity bit: None
Stop bit: 1
Frequency: 1hz

0. Message Header `0xAA`
1. Commander No `0xC0`
2. DATA 1 - PM2.5 Low byte
3. DATA 2 - PM2.5 High byte
4. DATA 3 - PM10 Low byte
5. DATA 4 - PM10 High byte
6. DATA 5 - ID byte 1
7. DATA 6 - ID byte 2
8. Checksum
9. Message tail `0xAB`

Checksum = `DATA1 + DATA2 + ... + DATA6`

## Cable Spec

Yellow - 5V
Green - GND
Blue - RX
Purple - TX
