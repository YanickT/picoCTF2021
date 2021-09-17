from pwn import *


conn = connect("mercury.picoctf.net", 2671)
conn.recvuntil(b"n:", drop=True)
n = int(conn.recvline())
conn.recvuntil(b"e:", drop=True)
e = int(conn.recvline())
conn.recvuntil(b"ciphertext:", drop=True)
cflag = int(conn.recvline())

conn.sendafter(b"Give me ciphertext to decrypt: ", str((cflag * pow(2, e, n)) % n) + "\n")
conn.recvuntil(b"Here you go: ", drop=True)
plain = int(conn.recvline())
conn.close()

result = plain // 2

print(bytes.fromhex(hex(result)[2:]).decode('ascii'))