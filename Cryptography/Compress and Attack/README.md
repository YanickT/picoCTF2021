# Compress and Attack

## Description
Your goal is to find the flag. compress_and_attack.py nc mercury.picoctf.net 29858.

## Hints
- The flag only contains uppercase and lowercase letters, underscores, and braces (curly brackets).

## Solution
As the name of the challenge suggests, it is possible to use compression to obtain the flag.
The attack is called CRIME and described at this article: https://en.wikipedia.org/wiki/CRIME

Using the `main.py` script we get the flag:

```picoCTF{sheriff_you_solved_the_crime}```