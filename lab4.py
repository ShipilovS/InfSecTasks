import numpy as np

def get_factor(n):
    x_fixed = 2
    cycle_size = 2
    x = 2
    factor = 1
    while factor == 1:
        for count in range(cycle_size):
            if factor > 1: 
                break
            x = (x * x + 1) % n
            factor = np.gcd(x - x_fixed, n)
        cycle_size *= 2
        x_fixed = x
    return factor

def factorization(n):
    factors = []
    while n > 1:
        next = get_factor(n)
        factors.append(next)
        n //= next
    return factors

def phi(p, q):
    return str( (p - 1)*(q - 1))


def gcd_extended(a, b):
    if a == 0 :
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def decrypt(cipher, d, n):
    step = len(str(n))
    res = ''
    for i in range(0, len(str(cipher)), len(str(n))):
        block = cipher[i:i+step]
        decrypted_text = pow(int(block), int(d), int(n))
        print(decrypted_text)
        res += str(decrypted_text)
    return res


def encrypt(plaintext, e, n):
    # Размерность блоков должна быть одинаковая
    step = len(str(n)) - 1
    res = ''
    for i in range(0, len(str(plaintext)), len(str(n)) - 1):
        block = plaintext[i:i+step]
        encrypted_text = pow(int(block), int(e), int(n))
        print(f"pow({block}, {e}, {n}) = {encrypted_text}")

        print(encrypted_text)
        res += str(encrypted_text)
    return res

n = '517758144238469'
e = '15931'
c = '419529693641281414842251130008422950947927526'

# from wolfram math
if len(factorization(int(n))) == 2:
    p, q = factorization(int(n))
    print(p, q)
else:
    raise Exception('len def factorization > 2')
phi_value = phi(p, q)
d = gcd_extended(int(e), int(phi_value))[1]
print(f"d = {d}")
print(f"phi_value = {phi_value}")

step = len(str(n))
res = decrypt(c, d, n)
    
res_text = ''
for i in range(0, len(res), 2):
    print(f"{res[i:i+2]} - {chr(int(res[i:i+2]))}")
    symbol = chr(int(res[i:i+2]))
    res_text += symbol
    
print(f"Text = {res_text}")


msg = 'ZNANIIA    ETO   SILA'
msg_text = ''
for sym in msg:
    msg_text += str(ord(sym))

print(msg_text)


enc_msg = encrypt(msg_text, e, n)
print(f"enc_msg = {enc_msg}")
print(f"c = {c}")

res_text = ''
for i in range(0, len(enc_msg), 2):
    symbol = chr(int(enc_msg[i:i+2]))
    res_text += symbol
print(f"res_text = {res_text}")