# Mind your Ps and Qs

## Description
In RSA, a small e value can be problematic, but what about N? Can you decrypt this? values.

## Hints
Bits are expensive, I used only a little bit over 100 to save money

## Solution
Since we know `n = p * q` and n is considered small we simply try to get the prime numbers p and q.
These can be checked at http://factordb.com.
We find:
p = 2159947535959146091116171018558446546179 
q = 658558036833541874645521278345168572231473

having p and q we can calculate the necessary values and finally decipher the text.
The calculation is done in `main.py` and the flag reads:


`picoCTF{sma11_N_n0_g0od_00264570}`
