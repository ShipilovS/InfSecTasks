# https://ru.frwiki.wiki/wiki/G%C3%A9n%C3%A9rateur_congruentiel_lin%C3%A9aire

import numpy as np

m = 25
c = 16
p = 256

N = 33

def X(x, m, c, p):
    print(f"{x}*{m}({x*m}) + {c})({x*m + c}) % m === {(x*m + c) % p}")
    return (x*m + c) % p


start_seed = 125
R = [start_seed / p]
seeds = [start_seed]
for i in range(N):
    start_seed = X(start_seed, m, c, p)
    print(start_seed)
    R.append(start_seed / p)
    seeds.append(start_seed)

print(seeds)
print(R)
print(len(seeds))
print(len(np.unique(seeds)))