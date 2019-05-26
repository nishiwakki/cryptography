import math
import random

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

birthday = 401

for var in range(0, 30):

    p_candidates = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
    q_candidates = [151, 157, 163, 167, 173, 179, 181, 191, 193, 197]

    p = random.choice(p_candidates)
    q = random.choice(q_candidates)

    N = p * q

    L = lcm(p - 1, q - 1)

    E = random.randrange(2, L)

    while math.gcd(E, L) != 1:
        E = random.randrange(2, L)

    for i in range(2, L):
        if (E * i) % L == 1:
            D = i
            break

    cipher = pow(birthday, E) % N
    decipher = pow(cipher, D) % N

    print("{0} -> {1} -> {2}".format(birthday, cipher, decipher))
    #print("(p, q, N, L, E, D)=({0}, {1}, {2}, {3}, {4}, {5})".format(p, q, N, L, E, D))
