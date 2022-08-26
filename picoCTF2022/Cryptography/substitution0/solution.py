import string

with open("message.txt", "r") as doc:
    lines = doc.readlines()

key = lines[0]
key_low = key.lower()

solution = ""
for letter in lines[-1]:
    if letter.isupper():
        i = key.index(letter)
        solution += string.ascii_uppercase[i]
    elif letter.islower():
        i = key_low.index(letter)
        solution += string.ascii_lowercase[i]
    else:
        solution += letter

print(solution)




