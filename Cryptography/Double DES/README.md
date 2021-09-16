# Double DES

## Description
I wanted an encryption service that's more secure than regular DES, but not as slow as 3DES... The flag is not in standard format. nc mercury.picoctf.net 29980 ddes.py
## Hints
- How large is the keyspace?

## Solution
Connecting to the server we get:
```
Here is the flag:
7cc5b18a36a7969fde9e22768279b843e62b1d7abe17aadaf0808c7c71808ba812a73554ba95558c
What data would you like to encrypt?
```
A suitable attack is described at https://en.wikipedia.org/wiki/Meet-in-the-middle_attack.
We therefore need a pair of cipher- and plaintext.
Since the server asks we encrypt `12345678` and get `40c4128676bd800b`.

Now we use `main.py` to crack the chiper.
And get the flag:


```45d6631b0c4d52b801a0fa7f6d3bda3c```
