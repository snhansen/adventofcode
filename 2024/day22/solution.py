from collections import defaultdict

with open("input") as f:
    inp = f.read().strip()

secrets = list(map(int, inp.split("\n")))


def process(n):
    res = n * 64
    n = res ^ n
    n = n % 16777216
    res = n // 32
    n = res ^ n
    n = n % 16777216
    res = n * 2048
    n = res ^ n
    n = n % 16777216
    return n


# Part 1
bananas_ls = []
changes_ls = []
ans_pt1 = 0

for secret in secrets:
    temp = [int(str(secret)[-1])]
    for _ in range(2000):
        secret = process(secret)
        temp.append(int(str(secret)[-1]))
    ans_pt1 += secret
    bananas_ls.append(temp)
    changes_ls.append([x - y for x, y in zip(temp[1:], temp)])

print(ans_pt1)

# Part 2
price = defaultdict(int)

for bananas, changes in zip(bananas_ls, changes_ls):
    seen = set()
    for i in range(len(bananas_ls[0])):
        seq = tuple(changes[i:(i + 4)])
        if seq in seen:
            continue
        if len(seq) < 4:
            continue
        seen.add(seq)
        price[seq] += bananas[i + 4]

print(max(price.values()))