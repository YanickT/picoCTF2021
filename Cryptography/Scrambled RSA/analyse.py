import matplotlib.pyplot as plt
from pwn import *
import string
import pickle
import numpy as np


def get():
    conn = connect("mercury.picoctf.net", 58251)
    alphabet = string.ascii_lowercase
    variantss = []
    for i in range(1, 6):
        variants = []
        print(i)
        for j in range(100):
            try:
                conn.sendafter(b"I will encrypt whatever you give me: ", alphabet[:i] + "\n")
                conn.recvuntil(b"Here you go: ", drop=True)
                ans = conn.recvline()
                if ans not in variants:
                    variants.append(ans)
            except Exception as error:
                print(error)
                pass
        variantss.append(variants)
    conn.close()

    with open("variants.txt", "wb") as doc:
        pickle.dump(variantss, doc)


def load():
    with open("variants.txt", "rb") as doc:
        variants = pickle.load(doc)
    return variants


if __name__ == "__main__":
    # get()
    variants = load()

    f = lambda x: np.prod([i for i in range(1, x + 1)])
    plt.plot(list(range(len(variants))), [len(e) for e in variants], "x", label="data")
    plt.plot(list(range(len(variants))), [f(i + 1) for i in range(len(variants))], label="Faculty")
    plt.xlabel("letters")
    plt.ylabel("variants")
    plt.legend()
    plt.grid()
    plt.show()

    lengths = [all([len(var) == len(var_letter[0]) for var in var_letter]) for var_letter in variants]
    print(f"same length: {all(lengths)}")

    lengths = [len(var_letter[0]) for var_letter in variants]
    print(f"lengths: {lengths}")

    diffs = [lengths[i + 1] - lengths[i] for i in range(len(lengths) - 1)]
    print(f"diffs: {diffs}")

    last_variants = [variants[0][0].replace(b"\n", b"")]
    equals = []
    states = []
    for i in range(1, len(variants)):
        states.append(all(last_variants[-1] in variant for variant in variants[i]))
        candidates = []
        for variant in variants[i]:
            for kill in last_variants:
                variant = variant.replace(kill, b"")
            candidates.append(variant)

        equals.append(all([candidates[0] == candidate for candidate in candidates]))
        last_variants.append(candidates[0].replace(b"\n", b""))
    print(states)
    print(equals)
