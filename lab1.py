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
ROUNDS=8
alphabet = string.ascii_letters + string.digits
# KEY = ''.join(secrets.choice(alphabet) for i in range(SIZE_OF_BLOCK))
# KEY = random.getrandbits(SIZE_OF_BLOCK)
msg='0x123456789ABCDEF0'
# KEY = hex(random.getrandbits(SIZE_OF_BLOCK))
KEY = '0x96EA704CFB1CF672'
F32 = '0xFFFFFFFF'
# binascii.unhexlify(KEY[2:])
# bin(int(KEY, 16))
# int(bin(int(hex_value, 16)), 2)
print(KEY)

def convert_from_hex_to_decimal(value):
    return int(bin(int(value, 16)), 2)

def convert_to_hex(value):
    return hex(value)

def convert_from_decimal_to_bin(value):
    return bin(value)

def convert_from_decimal_to_bin32(value):
    return bin(value >> 32)

# func
def binary(value):
    return bin(value)[2:]

# Циклический сдвиг вправо
def ROR(x, n, bits=32):
    mask = (2**n) - 1
    mask_bits = x & mask
    return (x >> n) | (mask_bits << (bits - n))

# Циклический сдвиг влево
def ROL(x, n, bits=32):
    return ROR(x, bits - n, bits)

def vlevo(x, t):
    return ctypes.c_uint32((x << t) | (x >> (32 - t))).value

def vpravo32(x, t, bits=32):
    return ctypes.c_uint32((x >> t) | (x << (32 - t))).value

def vpravo64(x, t):
    return ctypes.c_uint64((x >> t) | (x << (64 - t))).value

def F(L : int, K : int):
    f1 = vlevo(L, 9)
    f2 = ctypes.c_uint32(vpravo32(K, 11) | L).value
    print(f"f1 = {f1}")
    print(f"f2 = {f2}")
    return f1 ^ f2

def Ki(i):
    binary_value = vpravo64(convert_from_hex_to_decimal(KEY), 8*i) # с 0b + 32 бита или [2:34]
    return binary_value
# ==

def encoding(msg):
    # msg = msg.replace('0x', '')
    # len_msg = len(msg) // 2
    # lev_b   = convert_from_hex_to_decimal(msg[:len_msg])

    lev_b   = ctypes.c_uint32((convert_from_hex_to_decimal(msg) >> 32) & convert_from_hex_to_decimal(F32)).value
    prav_b  = ctypes.c_uint32(convert_from_hex_to_decimal(msg) & convert_from_hex_to_decimal(F32)).value
    # assert len(lev_b) == len(prav_b) # !
    for i in range(ROUNDS):
        K_i = Ki(i)
        lev_i = lev_b
        print(f"ki = #{K_i}")
        prav_i = prav_b ^ F(lev_b, K_i)
        print(f"IN lev_b \t= {lev_b}({hex(lev_b)})")
        print(f"IN prav_b \t= {prav_b}({hex(prav_b)})\n")

        if (i != ROUNDS - 1):
            print('YES')
            lev_b = prav_i 
            prav_b = lev_i
        else:
            print('NO')
            lev_b = lev_i
            prav_b = prav_i
        print(f"OUT lev_b \t= {lev_b}({hex(lev_b)})")
        print(f"OUT prav_b \t= {prav_b}({hex(prav_b)})\n")
    shifroblok = lev_b
    shifroblok = ctypes.c_uint32((shifroblok << 32) | (prav_b & convert_from_hex_to_decimal(F32))).value
    return shifroblok

# 9F9618D584EE35B6 - шифровка

def decoding(e_msg):
    lev_b   = ctypes.c_uint32((convert_from_hex_to_decimal(e_msg) >> 32) & convert_from_hex_to_decimal(F32)).value
    prav_b  = ctypes.c_uint32(convert_from_hex_to_decimal(e_msg) & convert_from_hex_to_decimal(F32)).value
    for i in range(ROUNDS - 1, -1, -1):
        K_i = Ki(i)
        lev_i = lev_b
        print(f"FKI = {K_i}")
        prav_i = prav_b ^ F(lev_b, K_i)

        if (i != 0):
            # print('YES')
            lev_b = prav_i 
            prav_b = lev_i
        else:
            # print('NO')
            lev_b = lev_i
            prav_b = prav_i
    shifroblok = lev_b
    shifroblok = ctypes.c_uint32((shifroblok << 32) | (prav_b & convert_from_hex_to_decimal(F32))).value
    return shifroblok

e_msg = encoding(msg)
print(f"e_msg = {e_msg}({convert_to_hex(int(e_msg))})")

d_msg = decoding(convert_to_hex(int(e_msg)))
print(f"d_msg = {d_msg}({convert_to_hex(int(d_msg))})")


