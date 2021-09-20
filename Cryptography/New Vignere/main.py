import string


CIPHER = "ilnipdjheipnenhhedionepegiejmleoehejfcnimdgehimnepedhhfbafmcgdek"
FLAG_ALPHA = "abcdef0123456789"
ALPHABET = string.ascii_lowercase[:16]
KEYLENGTH = 9
KEYS = []


def b16_decode(arg):
    return chr(int(f"{ord(arg[0]) - ord('a'):04b}" + f"{ord(arg[1]) - ord('a'):04b}", 2))


def deshift(c, k):
    t1 = ord(c)
    t2 = ord(k)
    return ALPHABET[(t1 - t2 + len(ALPHABET)) % len(ALPHABET)]


def check(key):
    # check here all possible double numbers :).
    # Start with the even ones
    for j in range(0, len(key) - 1, 2):
        to_encrypt = [CIPHER[i:i + 2] for i in range(j, len(CIPHER), KEYLENGTH * (KEYLENGTH % 2 + 1))]
        deshifted = [[deshift(l, key[k + j]) for k, l in enumerate(pair)] for pair in to_encrypt]
        decrypted = [b16_decode(pair) for pair in deshifted]
        if not all([letter in FLAG_ALPHA for letter in decrypted]):
            return False
    return True


def solve(key):
    if len(key) == KEYLENGTH:
        if check(key):
            KEYS.append(key)
            return False
        else:
            return False

    for letter in ALPHABET:
        temp_key = key + letter
        if check(temp_key):
            result = solve(temp_key)
            if result:
                return result
    return False


if __name__ == "__main__":
    for letter in ALPHABET:
        value = solve(letter)

    for key in KEYS:
        deshifted = ""
        for i, letter in enumerate(CIPHER):
            deshifted += deshift(letter, key[i % KEYLENGTH])
        ans = "".join(b16_decode(list(deshifted[i:i + 2])) for i in range(0, len(deshifted), 2))
        if all(e in FLAG_ALPHA for e in ans):
            print(f"picoCTF{{{ans}}}")
            break