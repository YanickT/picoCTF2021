from Crypto.Cipher import DES
import binascii
import multiprocessing


CORES = multiprocessing.cpu_count()


CFLAG = binascii.unhexlify("7cc5b18a36a7969fde9e22768279b843e62b1d7abe17aadaf0808c7c71808ba812a73554ba95558c")
PLAIN = binascii.unhexlify("12345678") + b"    "
CHIPER = binascii.unhexlify("40c4128676bd800b")


def crypt(key):
    key = (f"{key:06}  ").encode()
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(PLAIN), key


def decrypt(key):
    key = (f"{key:06}  ").encode()
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.decrypt(CHIPER), key


if __name__ == "__main__":
    with multiprocessing.Pool(CORES) as p:
        result = p.map(crypt, range(int(1e6)))
    cplain_key = dict(result)

    with multiprocessing.Pool(CORES) as p:
        result = p.map(decrypt, range(int(1e6)))
    dchip_key = dict(result)

    intersect = cplain_key.keys() & dchip_key.keys()
    first_round = intersect.pop()
    key1 = cplain_key[first_round]
    key2 = dchip_key[first_round]

    first_decrypt = DES.new(key2, DES.MODE_ECB)
    middle_flag = first_decrypt.decrypt(CFLAG)
    sec_decrypt = DES.new(key1, DES.MODE_ECB)
    flag = sec_decrypt.decrypt(middle_flag).decode()
    print(flag)
