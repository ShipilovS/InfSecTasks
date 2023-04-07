# https://ru.frwiki.wiki/wiki/G%C3%A9n%C3%A9rateur_congruentiel_lin%C3%A9aire

import numpy as np
import matplotlib.pyplot as plt

m = 663608941
c = 16
p = 2**32
u_0 = 3

N = 10001

def X(x, m, c, p):
    # print(f"{x}*{m}({x*m}) + {c})({x*m + c}) % m === {(x*m + c) % p}")
    return (x*m + c) % p


def lehmer_generator(u_0, m, c, p):
    u_i = [u_0]
    R = [u_0 / p]
    temp = X(u_i[-1], m, c, p)
    while (len(np.unique(u_i)) < 10000) and (len(np.unique(u_i)) == len(u_i)): 
    # while temp not in u_i:
        R.append(temp / p)
        u_i.append(temp)
        temp = X(u_i[-1], m, c, p)
    return u_i, R

def length_test(m, c, p):
    for u_0 in range(1000):
        u_values, r_values = lehmer_generator(u_0, m, c, p)
        # print(f"При u_0 = {u_0} len(u_values) = {len(u_values)}")


# print(seeds)
# print(R)
print(f"\n\n")
u_values, r_values = lehmer_generator(u_0, m, c, p)
# print(f"u_values = {u_values}({len(u_values)})")
# print(f"r_values = {r_values}")
# print(f"u_values = {len(u_values)}")
# print(f"r_values = {len(r_values)}")
# print(f"len(u_values) = {len(u_values)}")

# length_test(m, c, p)

fig, ax = plt.subplots()
# plt.bar([i for i in range(len(r_values))], r_values)
# plt.show()

def pi_test(r_values):
    number = 0
    for i in range(len(r_values) // 2):
        r = np.sqrt(r_values[2*i-1]**2 + r_values[2*i]**2)
        if r < 1:
            number += 1
    return 8 * number / len(r_values)

pi_value = pi_test(r_values)
print(pi_value)

print("Проверки на равномерность распределения")
m = np.sum(r_values) / len(r_values)
print(f"Матожидание = {m} (должно быть примерно = 0.5)")
print(f"Дисперсия = {np.var(r_values)} (должно быть примерно = 0.0833)")
print(f"ср квадр отклонение = {np.std(r_values)} (должно быть примерно = 0.2887)")