# It's Not My Fault 1

## Description
What do you mean RSA with CRT has an attack that's not a fault attack? Connect with nc mercury.picoctf.net 10055. not_my_fault.py

## Hints
None

## Solution
At first, we want to solve the md5 challenge which we solve by a brute force attack.
For the RSA part we implement the attack described at https://bitsdeep.com/posts/attacking-rsa-for-fun-and-ctf-points-part-4/.
Running `main.py` returns the flag:

```picoCTF{1_c4n'7_b3l13v3_17'5_n07_f4ul7_4774ck!!!}```
