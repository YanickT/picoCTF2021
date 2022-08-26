FLAG = "lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil"


def b16_decrypt(enc):
    plain = ""
    for i in range(0, len(enc), 2):
        number = int(f"{ord(enc[i]) - ord('a'):04b}{ord(enc[i + 1]) - ord('a'):04b}", 2)
        plain += chr(number)
    return plain


def shift(c, k):
    t1 = ord(c) - ord("a")
    return chr((t1 - k) % 16 + ord("a"))


for i in range(16):
    flag = "".join([shift(c, i) for c in FLAG])
    print(f"picoCTF{{{b16_decrypt(flag)}}}")
