# No Padding, No Problem

## Description
Oracles can be your best friend, they will decrypt anything, except the flag's ciphertext. How will you break it? Connect with nc mercury.picoctf.net 2671.

## Hints
- What can you do with a different pair of ciphertext and plaintext? What if it is not so different after all...

## Solution
We connect to the given port and url and get:
```
n: 79864910700238500469783659951741402313182360600083672177847310660522479441653186505304386379627427350619627215807490218854461408611591023640354990151890474261365785399531700375985936847207961447794100985076709158518164392895251106818162442368138456086727786371418478581505784312366632382957819828692786478897
e: 65537
ciphertext: 31862204409704270709323289244736823267398719800916071299109951942785836590750510250732330754860266707251158838878342119067821852491878083710512813564997814665796454042588971568005035198402584799511809481364098479633580458487443386165147903985808861002102425514406941742937414943874827030692240580908365744612
```
Furthermore, asks the server if it should decrypt something but states, that it won`t decrypt the flag.