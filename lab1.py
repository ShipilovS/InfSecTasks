# функция генерации ключей делаем сами
# ~ Not
# ^ XOR
# | Or
# & And
import ctypes
import string
import secrets
import random
import binascii
# ENV
b = 6
SIZE_OF_BLOCK=2**b
ROUNDS=2
alphabet = string.ascii_letters + string.digits
# KEY = ''.join(secrets.choice(alphabet) for i in range(SIZE_OF_BLOCK))
# KEY = random.getrandbits(SIZE_OF_BLOCK)
msg='0x123456789ABCDEF0'
KEY = hex(random.getrandbits(SIZE_OF_BLOCK))
# KEY = '0x96EA704CFB1CF672'
F32 = '0xFFFFFFFF'
# binascii.unhexlify(KEY[2:])
# bin(int(KEY, 16))
# int(bin(int(hex_value, 16)), 2)
print(KEY)

# func
def convert_from_hex_to_decimal(value):
    return int(bin(int(value, 16)), 2)

def convert_to_hex(value):
    return hex(value)

def convert_from_decimal_to_bin(value):
    return bin(value)

def vlevo(x, t):
    return ctypes.c_uint32((x << t) | (x >> (32 - t))).value

def vpravo32(x, t):
    return ctypes.c_uint32((x >> t) | (x << (32 - t))).value

def vpravo64(x, t):
    return ctypes.c_uint64((x >> t) | (x << (64 - t))).value

def F(L : int, K : int):
    f1 = vlevo(L, 9)
    f2 = vpravo32(K, 11) | L
    return f1 ^ f2

def Ki(i):
    # Преобразование в uint32
    value = ctypes.c_uint32(vpravo64(convert_from_hex_to_decimal(KEY), 8*i)).value # или 3*i ?
    return value

def encoding(msg):
    lev_b   = ctypes.c_uint32((convert_from_hex_to_decimal(msg) >> 32) & convert_from_hex_to_decimal(F32)).value
    prav_b  = ctypes.c_uint32(convert_from_hex_to_decimal(msg) & convert_from_hex_to_decimal(F32)).value
    for i in range(ROUNDS):
        print(f"Encoding")
        print(f"\n================")
        print(f"Round = {i}")
        K_i = Ki(i)
        lev_i = lev_b
        prav_i = prav_b ^ F(lev_b, K_i)
        print(f"IN lev_b  \t = {lev_b}({hex(lev_b)})")
        print(f"IN prav_b \t = {prav_b}({hex(prav_b)})\n")

        if (i != ROUNDS - 1):
            lev_b = prav_i 
            prav_b = lev_i
        else:
            lev_b = lev_i
            prav_b = prav_i
        print(f"OUT lev_b  \t = {lev_b}({hex(lev_b)})")
        print(f"OUT prav_b \t = {prav_b}({hex(prav_b)})")

    shifroblok = lev_b
    # Преобразование в uint64
    shifroblok = ctypes.c_uint64((shifroblok << 32) | (prav_b & convert_from_hex_to_decimal(F32))).value
    return shifroblok

def decoding(e_msg):
    print(f"\nDecoding")
    lev_b   = ctypes.c_uint32((convert_from_hex_to_decimal(e_msg) >> 32) & convert_from_hex_to_decimal(F32)).value
    prav_b  = ctypes.c_uint32(convert_from_hex_to_decimal(e_msg) & convert_from_hex_to_decimal(F32)).value
    for i in range(ROUNDS - 1, -1, -1):
        print(f"================")
        print(f"Round = {i}")
        K_i = Ki(i)
        lev_i = lev_b
        prav_i = prav_b ^ F(lev_b, K_i)
        print(f"IN lev_b  \t = {lev_b}({hex(lev_b)})")
        print(f"IN prav_b \t = {prav_b}({hex(prav_b)})\n")

        if (i != 0):
            lev_b = prav_i 
            prav_b = lev_i
        else:
            lev_b = lev_i
            prav_b = prav_i
        print(f"OUT lev_b  \t = {lev_b}({hex(lev_b)})")
        print(f"OUT prav_b \t = {prav_b}({hex(prav_b)})")

    shifroblok = lev_b
    # Преобразование в uint64
    shifroblok = ctypes.c_uint64((shifroblok << 32) | (prav_b & convert_from_hex_to_decimal(F32))).value
    return shifroblok

e_msg = encoding(msg)
print(f"e_msg = {e_msg}({convert_to_hex(int(e_msg))})")

d_msg = decoding(convert_to_hex(int(e_msg)))
print(f"d_msg = {d_msg}({convert_to_hex(int(d_msg))})")


