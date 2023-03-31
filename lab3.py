# https://ru.frwiki.wiki/wiki/G%C3%A9n%C3%A9rateur_congruentiel_lin%C3%A9aire

import numpy as np
import matplotlib.pyplot as plt

m = 509
c = 16
p = 24551

N = 10001

def X(x, m, c, p):
    print(f"{x}*{m}({x*m}) + {c})({x*m + c}) % m === {(x*m + c) % p}")
    return (x*m + c) % p


start_seed = 125
R = [start_seed / p]
seeds = [start_seed]
for i in range(N):
    if len(np.unique(seeds)) != len(seeds):
        print(start_seed)
        break
    start_seed = X(start_seed, m, c, p)
    R.append(start_seed / p)
    seeds.append(start_seed)


# print(seeds)
# print(R)
print(f"\n\n")
print(len(seeds))
print(len(np.unique(seeds)))
fig, ax = plt.subplots()
plt.plot(R)
plt.show()