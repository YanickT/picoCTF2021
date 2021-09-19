import hashlib
from functools import partial
import multiprocessing
import numpy as np
from pwn import *


CORES = multiprocessing.cpu_count()


def worker(dp, m, n, e):
    # print(dp)
    res = np.gcd(m - pow(m, e * dp, n), n)
    if res != 1:
        return res


if __name__ == "__main__":
    conn = connect("mercury.picoctf.net", 10055)
    line = conn.recvline().decode()
    string = line.split('"')[1]
    end = line.split(": ")[1].replace("\n", "")

    # solve hash
    add = 0
    print("start")
    while True:
        md5_hash = str(hashlib.md5((string + str(add)).encode("utf-8")).hexdigest())
        if md5_hash[-6:] == end:
            print("found")
            break
        add += 1
    conn.send(string + str(add) + "\n")
    conn.recvuntil(b"Public Modulus :  ")
    n = int(conn.recvline().decode())
    conn.recvuntil(b"Clue :  ")
    e = int(conn.recvline().decode())

    m = 1234567890
    with multiprocessing.Pool(CORES) as p:
        for value in p.imap(partial(worker, m=m, e=e, n=n), range(1 << 20), chunksize=10_000):
            if value is not None:
                print(value)
                q = n // value
                conn.send(str(q + value) + "\n")
                print(conn.recv())
                conn.close()
                exit()

