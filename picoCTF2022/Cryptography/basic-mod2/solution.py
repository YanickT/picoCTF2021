import string

s = string.ascii_uppercase + string.digits + "_"

with open("message.txt", "r") as doc:
    line = doc.readline()

numbers = [int(e) for e in line.split(" ")[:-1]]
inverses = []
c = 41

for a in numbers:
    for b in range(c - 1):
        if (a * b) % c == 1:
            inverses.append(b)
            break

print("picoCTF{" + "".join([s[i - 1] for i in inverses]) + "}")
