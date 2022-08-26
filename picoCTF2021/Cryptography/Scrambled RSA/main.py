from pwn import *


def remove_former(to_remove, text):
    for remove_me in to_remove:
        text = text.replace(remove_me, "")
    return text


conn = connect("mercury.picoctf.net", 58251)
conn.recvuntil(b"flag:", drop=True)
cflag = conn.recvline().decode().replace("\n", "")

alphabet = string.ascii_lowercase + string.digits + "}_"
to_remove = []
flag = "picoCTF{"

# make list of letters in flag
print("add known")
for i in range(1, len(flag) + 1):
    conn.sendafter(b"I will encrypt whatever you give me: ", flag[:i] + "\n")
    conn.recvuntil(b"Here you go: ", drop=True)
    ans = remove_former(to_remove, conn.recvline().decode().replace("\n", ""))
    to_remove.append(ans)

# test further letters
print("add new")
while flag[-1] != "}":
    for letter in alphabet:
        conn.sendafter(b"I will encrypt whatever you give me: ", flag + letter + "\n")
        conn.recvuntil(b"Here you go: ", drop=True)
        ans = remove_former(to_remove, conn.recvline().decode().replace("\n", ""))

        if ans in cflag:
            flag += letter
            to_remove.append(ans)
            print(flag)
            break

conn.close()
print(flag)
