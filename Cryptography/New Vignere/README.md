# New Vignere

## Description
Another slight twist on a classic, see if you can recover the flag. (Wrap with picoCTF{}) ilnipdjheipnenhhedionepegiejmleoehejfcnimdgehimnepedhhfbafmcgdek new_vignere.py

## Hints
- https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Cryptanalysis

## Solution
Using the Kasiski test at https://planetcalc.com/8550/ we find the key length to be a fraction of 27.
The fractions are 1, 3, 9, 27. Since 1 would be a Caeser cipher again and 3 is also very short the guess is 9.

To brute force the flag we use a short trick.
Due to the doubling of letters in the b16_encoding the results, even after the shift, are related.
We exploit this relation and thus determine the key pairwise.
Since the key has an odd length, we get a sweep of one between two key-iterations which we have to care of later.
Therefore, we check at first for all key-pairs in a non-offset computations and save all possible keys.
Later we check each of them to take care of both ways to use the key on pairs.

Since the above explanation is a bit abstract and fast lets do it on the given example:
```
cipher : il ni pd jh ei pn en hh ed io ne pe gi ej ml eo eh ej fc ni md ge hi mn ep ed hh fb af mc gd ek
key pos: 01 23 45 67 80 12 34 56 78 01 23 45 67 80 12 34 56 78 01 23 45 67 80 12 34 56 78 01 23 45 67 80
```
The first letter of the key is involved in the following pairs:
```
cipher : il ei io ej fc hi fb ek
key pos: 01 80 01 80 01 80 01 80
```
It is involved in two different combinations the `01` combination and the `80` combination.
This drift is caused by the odd length of the key, and we ignore the `80` combinations at first and verify them later.
The remaining combinations read:
```
cipher : il io fc fb
key pos: 01 01 01 01
```
We now choose an arbitrary key (or iterate over all possibilities) and at first deshift the pairs.
Lets say we guess the key to be `cd`. The deshift reads:
```
gi gl dp do
```
After the b16_decoding we find:
```
h k ? >
```
But these are not allowed characters for the flag. Therefore, `cd` is not the korrect key.
Lets try `cj` instead:
```
gc gf dj di
b  e  9  8
```
These are allowed an `cj` may be the first two letter of the key. (They actually are :)).

This is done in the `main.py`. The flag reads:

```picoCTF{b7bf6c4d2e3c7715489723f360f8d128}```
