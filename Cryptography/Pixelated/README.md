# Pixelated

## Description
I have these 2 images, can you make a flag out of them? scrambled1.png scrambled2.png
## Hints
- https://en.wikipedia.org/wiki/Visual_cryptography
- Think of different ways you can "stack" images

## Solution

Checking the RBG values of both pictures we realized many values would add up to `[255, 255, 255]`.
This is quite interesting since it is the code for withe.
Using main.py we added both images and received the flag:

```picoCTF{7188864c}```