# Easy Peasy

## Description
A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) nc mercury.picoctf.net 58913 otp.py

## Hints
- Maybe there's a way to make this a 2x pad.

## Solution
The encryption is an `XOR` or `^` in python. 
This encryption is easy to invert when one of the two participants is known. 
It is again an `XOR` operation.
Therefore, if we can use the part, which encrypted the flag, again with something we 
know the key can be calculated.

Within the `otp.py` we see, that the key has a length of 50000 and is reused after this length.
Furthermore, can we calculate the original length of the flag and thus know how many chars are needed to restart the key.

Afterwards we ask the server to encrypt some 'A' (with length of the flag) and recalculate the key.
Using this key we can decrypt the flag.

This is done in `main.py`.
The flag reads:

```picoCTF{35ecb423b3b43472c35cc2f41011c6d2}```