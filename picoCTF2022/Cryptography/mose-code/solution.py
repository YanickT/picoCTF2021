import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

inv_morse_dict = {MORSE_CODE_DICT[key]: key for key in MORSE_CODE_DICT}

samplerate, data = wavfile.read('morse_chal.wav')

data_ = np.where(np.abs(np.diff(data) + np.abs(data[:-1]) / np.max(data[:-1])) > 0, 1, 0)

parts = []
old = 0
state = True
temp = []
pauses = []
for i, d in enumerate(data_):
    if d == 0 and state:
        state = False
        temp.append(i - old)
        old = i
    elif d != 0 and not state:
        state = True
        if 30000 > i - old > 10000:
            parts.append(temp)
            temp = []
        elif i - old > 30000:
            parts.append(temp)
            temp = []
            pauses.append(len(parts))
        old = i

parts.append(temp)
parts[0][0] += 1
morse = [inv_morse_dict["".join(["." if e == 4411 else "-" for e in part])] for part in parts]

for pause in pauses:
    morse[pause] = "_" + morse[pause]

print("picoCTF{" + "".join(morse).lower() + "}")

