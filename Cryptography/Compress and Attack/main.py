from pwn import *
import string


ALPHABET = string.ascii_lowercase + "_}"


flag = "picoCTF{"
conn = connect("mercury.picoctf.net", 29858)


def get_length(msg):
    conn.sendlineafter("Enter your text to be encrypted: ", msg)
    conn.recvline()  # nonce
    conn.recvline()  # encrypted_text
    return int(conn.recvline().decode().replace("\n", ""))  # length


while True:
    length = get_length(flag + "0")
    for letter in ALPHABET:
        if get_length(flag + letter) < length:
            flag += letter
            print(f"{flag}")
            break

    if letter == "}":
        break

conn.close()