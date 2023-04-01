# https://ru.frwiki.wiki/wiki/G%C3%A9n%C3%A9rateur_congruentiel_lin%C3%A9aire

import numpy as np
import matplotlib.pyplot as plt

m = 509
c = 16
p = 229
u_0 = 12

N = 10001

def X(x, m, c, p):
    # print(f"{x}*{m}({x*m}) + {c})({x*m + c}) % m === {(x*m + c) % p}")
    return (x*m + c) % p


def lehmer_generator(u_0, m, c, p):
    R = [u_0 / p]
    u_i = [u_0]
    while (len(np.unique(u_i)) < 10000) and (len(np.unique(u_i)) == len(u_i)): 
        temp = X(u_i[-1], m, c, p)
        R.append(temp / p)
        u_i.append(temp)
    return u_i, R

def length_test(m, c, p):
    for u_0 in range(10):
        u_values, r_values = lehmer_generator(u_0, m, c, p)
        print(f"При u_0 = {u_0} len(u_values) = {len(u_values)}")


# print(seeds)
# print(R)
print(f"\n\n")
# u_values, r_values = lehmer_generator(u_0, m, c, p)
# print(f"len(u_values) = {len(u_values)}")

length_test(m, c, p)

fig, ax = plt.subplots()
# plt.plot(r_values)
# plt.show()

