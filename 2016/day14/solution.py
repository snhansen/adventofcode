import hashlib
import re
from functools import cache

inp = "ngcjuoqr"

@cache
def hash_pt1(i):
    return hashlib.md5((inp + str(i)).encode()).hexdigest()


@cache
def hash_pt2(i):
    to_hash = inp + str(i)
    for _ in range(2017):
        res = hashlib.md5(to_hash.encode()).hexdigest()
        to_hash = res
    return res


def solve(part2 = False):
    hash_fct = hash_pt2 if part2 else hash_pt1
    i = 0
    n_key = 0
    while True:
        three_peat = re.search(r"(.)\1{2,}",hash_fct(i))
        if three_peat:
            char = three_peat.group()[0]
            for j in range(i + 1, i + 1001):
                if re.search(fr"{re.escape(char)}{{5,}}", hash_fct(j)):
                    n_key += 1
                    break
        if n_key == 64:
            return i
        i += 1
        

# Part 1
print(solve())

# Part 2
print(solve(True))