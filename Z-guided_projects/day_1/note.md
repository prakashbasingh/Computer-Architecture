Number Bases
---------------------

Its the "language" that a number is written down in.

Douze == twelve
1100 == 12

base 2: binary ( 0 and 1)
base 8: octal (rarely used) ( 0 - 7)
base 10: decimal ( what we know from grade school, regular boring ol numbers) ( 0 - 9)
base 16: hexadecimal, "hex" ( 0 - 9 and A - F)
base 64: base 64


base 10 (decimal)
=========================
base 10 = 0 - 9

+-----1000's place -- 10^3
|+----100's place --- 10^2
||+---10's place ---- 10^1
|||+--1's place ----- 10^0
||||
abcd
12345
1 2 3 4  
| | | | 
| | | | 
| | | |------> 4 *    1 =          4
| | |--------> 3 *   10 =         30
| |----------> 2 *  100 =        200
|------------> 1 * 1000 =       1000
---------------------------------------
total-------------------------->1234
or 
1 * 1000 + 2 * 100 + 3 * 10 + 4 * 1 = 1234

base 2 (binary digit also known as "bit")
============================================
base 2 = 0 & 1

+-----8'th place -- 2^3
|+----4'th place -- 2^2
||+---2'nd place -- 2^1
|||+--1'st place -- 2^0
||||
abcd
0011 which is 3 in decimal
0 0 1 1  
| | | | 
| | | | 
| | | |------> 1 *  1 =       1
| | |--------> 1 *  2 =       2
| |----------> 0 *  4 =       0
|------------> 0 *  8 =       0
---------------------------------------
total-----------------------> 3
or 
0 * 8 + 0 * 4 + 1 * 2 + 1 * 1 = 3 decimal

========================================
some more terminology
---------------------
8 bits = "bytes"
4 bits = "nybble"
1024 bites = 1 kilobytes
===================

to specify the base in code: need to put prefix 
-------
prefix
-------
[none] --------> decimal
0b ------------> binary
0x ------------> hex
0o ------------> octal

11000 just a number in decimal
0b11000 is 24 in binary
0x11000 is 10 in hex
==============================================================
#ffff00 it is a hex code this means yellow
hex code has 0 -9 and A - F
ffff00 --->
red      green    blue
ff       ff       00        hex     base 10    (it has three bites but third bite has value zero)
255      255      0         decimal base 16
11111111 11111111 00000000  binary  base 2
--------
  byte 
lower the base more the digit numbers to represent any number
====================================================================================
hex and binary has xome similarities
ff and 11111111

binary hex
0000   1
0001   2
0010   3
0011   4
0100   5
0101   6
0111   7
1000   8
1001   9
1010   A
1011   B
1100   C
1101   D
1110   E
1111   F

0B00101010 = 0X???
           = 0x2A

