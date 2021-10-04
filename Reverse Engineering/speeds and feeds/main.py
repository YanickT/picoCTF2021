import numpy as np
import re
import skimage.draw as draw
import matplotlib.pyplot as plt
from pwn import *


def get_instructions():
    conn = connect("mercury.picoctf.net", 16524, timeout=5)
    with open("instructions.txt", "w") as doc:
        while True:
            try:
                line = conn.recvline().decode()
                doc.write(line)
            except:
                break
        conn.close()


# get_instructions()
pattern = re.compile("\w[-]?\d*[.]?\d*")
image = np.ones((2500, 250))


def update_pos(position, x=None, y=None, z=None):
    new_position = [0, 0, 0]
    new_position[0] = int(round(x * 10, 0)) + 10 if x is not None else position[0]
    new_position[1] = int(round(y * 10, 0)) + 10 if y is not None else position[1]
    new_position[2] = z if z is not None else position[2]
    return new_position


def g1(position, x=None, y=None, z=None):
    end_pos = update_pos(position, x, y, z)
    if z is None:
        rs, cs, _ = draw.line_aa(position[0], position[1], end_pos[0], end_pos[1])
        image[rs, cs] = position[2]
    return end_pos


commands = {"G0": update_pos, "G1": g1}

with open("instructions.txt", "r") as doc:
    position = [0, 0, 0]
    for n, instruction in enumerate(doc):
        if n == 0:
            continue
        command, coords = instruction[:2], instruction[2:]
        coords = {coord[0].lower(): float(coord[1:]) for coord in pattern.findall(coords)}
        position = commands[command](position, **coords)

plt.imshow(np.rot90(image))
plt.colorbar()
plt.show()
