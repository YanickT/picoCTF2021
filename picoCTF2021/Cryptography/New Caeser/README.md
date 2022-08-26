# New Caeser

## Description
We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil new_caesar.py

## Hints
- How does the cipher work if the alphabet isn't 26 letters?
- Even though the letters are split up, the same paradigms still apply

## Solution
We simply check the `new_caeser.py` and write a reverse script.
In one of the possible solutions a well known phrase appears, and it turns out to be the flag:

```picoCTF{et_tu?_431db62c5618cd75f1d0b83832b67b46}```
