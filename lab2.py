# OFB(Output Feedback) CFB(Cipher Feedback) реализовать

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
KEY = hex(random.getrandbits(SIZE_OF_BLOCK))
# KEY = '0x96EA704CFB1CF672'
F32 = '0xFFFFFFFF'
print(KEY)
message = ['0x123456789ABCDEF0', '0x123456789ABCDEF0', '0x1FBA85C953ABCFD0', '0x1FBA85C953ABCFD0']
# инициализационный вектор
IV = '0x18FD47203C7A23BC'
# число блоков в исходном сообщении
B = len(message)
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
    lev_b = ctypes.c_uint32((convert_from_hex_to_decimal(msg) >> 32) & convert_from_hex_to_decimal(F32)).value
    prav_b = ctypes.c_uint32(convert_from_hex_to_decimal(msg) & convert_from_hex_to_decimal(F32)).value
    for i in range(ROUNDS):
        K_i = Ki(i)
        lev_i = lev_b
        prav_i = prav_b ^ F(lev_b, K_i)

        if (i != ROUNDS - 1):
            lev_b = prav_i 
            prav_b = lev_i
        else:
            lev_b = lev_i
            prav_b = prav_i

    shifroblok = lev_b
    # Преобразование в uint64
    shifroblok = ctypes.c_uint64((shifroblok << 32) | (prav_b & convert_from_hex_to_decimal(F32))).value
    return shifroblok

def decoding(e_msg):
    lev_b   = ctypes.c_uint32((convert_from_hex_to_decimal(e_msg) >> 32) & convert_from_hex_to_decimal(F32)).value
    prav_b  = ctypes.c_uint32(convert_from_hex_to_decimal(e_msg) & convert_from_hex_to_decimal(F32)).value
    for i in range(ROUNDS - 1, -1, -1):
        K_i = Ki(i)
        lev_i = lev_b
        prav_i = prav_b ^ F(lev_b, K_i)

        if (i != 0):
            lev_b = prav_i 
            prav_b = lev_i
        else:
            lev_b = lev_i
            prav_b = prav_i

    shifroblok = lev_b
    # Преобразование в uint64
    shifroblok = ctypes.c_uint64((shifroblok << 32) | (prav_b & convert_from_hex_to_decimal(F32))).value
    return shifroblok

# ======

# Шифрование в режиме CBC
def encodingCBC(msg):
    """
    msg - list of hex values
    """
    msg_cbc = []
    # шифрование первого блока (xor'ится с IV перед шифрованием)
    block = ctypes.c_uint64(convert_from_hex_to_decimal(msg[0]) ^ convert_from_hex_to_decimal(IV)).value
    msg_cbc.append(encoding(convert_to_hex(block)))
    print(f"зашифрованный первый блок -> {msg_cbc[0]}({convert_to_hex(int(msg_cbc[0]))})")

    # Каждый последующий блок перед шифрованием xor'ится с предыдущим зашифрованным блоком
    for i in range(1, B):
        # xor с предыдущим зашифрованным
        block = ctypes.c_uint64(convert_from_hex_to_decimal(msg[i]) ^ msg_cbc[i-1]).value

        # # шифруем блок
        msg_cbc.append(encoding(convert_to_hex(int(block))))
        print(f"зашифрованный {i} блок -> {msg_cbc[i]}({convert_to_hex(int(msg_cbc[i]))})")

    return msg_cbc

# Дешифрование в режиме CBC
def decodingCBC(e_msg):
    dec_cbc = []
    # Расшифровка в режиме CBC
    msg_b = decoding(convert_to_hex(e_msg[0]))
    msg_b ^= convert_from_hex_to_decimal(IV)
    dec_cbc.append(msg_b)
    print(f"Расшифрованный первый блок = {msg_b}({convert_to_hex(int(e_msg[0]))})")
    for i in range(1, B):
        msg_b = decoding(convert_to_hex(e_msg[i]))
        msg_b ^= e_msg[i-1]
        dec_cbc.append(msg_b)
        print(f"Расшифрованный {i} блок -> {msg_b}({convert_to_hex(int(msg_b))})")
    return dec_cbc

print(f"message = {message}")

# Шифрование в режиме CFB
def encodingCFB(msg):
    encrypted_array = []
    block = IV
    block = encoding(block)
    plaintext = convert_from_hex_to_decimal(msg[0])
    ciphertext = plaintext ^ block
    encrypted_array.append(ciphertext)

    for i in range(1, B):
        block = ctypes.c_uint64(encoding(convert_to_hex(encrypted_array[i-1]))).value
        plaintext = convert_from_hex_to_decimal(msg[i])
        block ^= plaintext
        encrypted_array.append(block)
        pass
    return encrypted_array

# Дешифрование в режиме CFB
def decodingCFB(e_msg):
    decrypted_array = []
    block = IV
    block = encoding(block)
    ciphertext = e_msg[0]
    plaintext = ciphertext ^ block
    decrypted_array.append(plaintext)
    for i in range(1, B):
        block = encoding(convert_to_hex(e_msg[i-1])) # кодируем шифроблок!
        ciphertext = e_msg[i]
        block ^= ciphertext
        decrypted_array.append(block)
    return decrypted_array

def encodingECB(msg):
    encrypted_array = []
    for i in range(B):
        block = ctypes.c_uint64(encoding(msg[i])).value
        encrypted_array.append(block)
    return encrypted_array

def decodingECB(e_msg):
    decrypted_array = []
    for i in range(B):
        block = ctypes.c_uint64(decoding(convert_to_hex(e_msg[i]))).value
        decrypted_array.append(block)
    return decrypted_array

print(f"\n\n====Cipher Block Chaining")
array_e_msg = encodingCBC(message)
print(f"array_e_msg hex's = {list(map(lambda x: convert_to_hex(x), array_e_msg))}\n")

array_d_msg = decodingCBC(array_e_msg)
print(f"array_e_msg hex's = {list(map(lambda x: convert_to_hex(x), array_d_msg))}")


print(f"\n\n====Cipher Feedback")
array_e_msg_cfb = encodingCFB(message)
print(f"array_e_msg_cfb hex's = {list(map(lambda x: convert_to_hex(x), array_e_msg_cfb))}")

array_d_msg_cfb = decodingCFB(array_e_msg_cfb)
print(f"array_d_msg_cfb hex's = {list(map(lambda x: convert_to_hex(x), array_d_msg_cfb))}")


print(f"\n\n====Electronic Codebook")
array_e_ecb_msg = encodingECB(message)
print(f"array_d_ecb_msg hex's = {list(map(lambda x: convert_to_hex(x), array_e_ecb_msg))}")

array_d_ecb_msg = decodingECB(array_e_ecb_msg)
print(f"array_d_ecb_msg hex's = {list(map(lambda x: convert_to_hex(x), array_d_ecb_msg))}")

