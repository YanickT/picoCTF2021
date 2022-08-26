# Mini RSA

## Description
What happens if you have a small exponent? There is a twist though, we padded the plaintext so that (M ** e) is just barely larger than N. Let's decrypt this: ciphertext

## Hints
- RSA tutorial
- How could having too small of an e affect the security of this key?
- Make sure you don't lose precision, the numbers are pretty big (besides the e value)
- You shouldn't have to make too many guesses
- pico is in the flag, but not at the beginning

## Solution
We exploit that m**e is not that much bigger than N, which means we can brutforce the original message.
Using `main.py` we get:


```picoCTF{e_sh0u1d_b3_lArg3r_aef7377d}```