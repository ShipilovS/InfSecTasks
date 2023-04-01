import math
import numpy as np

# chr(number)

def phi(p, q):
    return str( (p - 1)*(q - 1))


def gcd_extended(a, b):
    if a == 0 :
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def parse(string):

    pass

n = '565570077646207'
e = '12341'
c = '277140870674302260217431481485329310844916399448964498705119'

# 

# p = 2431967
# q = 193707721

# from wolfram math
p = 1546379
q = 365738333
phi_value = phi(p, q)
d = gcd_extended(int(e), int(phi_value))[1]

step = len(str(n))
res = ''
for i in range(0, len(str(c)), len(str(n))):
    block = c[i:i+step]
    decrypt = pow(int(block), int(d), int(n))
    print(decrypt)
    res += str(decrypt)
    
res_text = ''
for i in range(0, len(res), 2):
    print(f"{res[i:i+2]} - {chr(int(res[i:i+2]))}")
    symbol = chr(int(res[i:i+2]))
    res_text += symbol
    
print(f"Text = {res_text}")