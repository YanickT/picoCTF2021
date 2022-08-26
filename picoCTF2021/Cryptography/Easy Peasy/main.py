import socket

KEY_LEN = 50000

# connect to server and get flag (encrypted)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
s.connect(("mercury.picoctf.net", 58913))
s.recv(1024)
flag = s.recv(1024).split(b"\n")[1].decode()

# send a string with length 50000 - flag_length and ignore the result
flag_length = len(flag) // 2
rest_length = KEY_LEN - flag_length
string = "A" * rest_length + "\n"
s.send(string.encode())
while True:
    try:
        s.recv(1024)
    except:
        break

# send a string of 'A's which matches the length of the flag
string = "A" * flag_length + "\n"
s.send(string.encode())
key = s.recv(1024).decode().split("\n")[1]
s.close()
print(key)

# decrypt the key
pairs = [key[i:i + 2] for i in range(0, len(key), 2)]
values = [int(value, 16) for value in pairs]
key = [value ^ ord("A") for value in values]
print(key)

# use the key to decrypt the flag
pairs = [int(flag[i:i + 2], 16) for i in range(0, len(flag), 2)]
flag = [flag ^ key_ for flag, key_ in zip(pairs, key)]
flag = "".join([chr(value) for value in flag])
print(f"picoCTF{{{flag}}}")