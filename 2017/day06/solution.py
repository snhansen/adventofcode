from itertools import count

with open("input") as f:
    inp = f.read().strip()

banks = tuple(map(int, inp.split("	")))


def redestribute(banks):
    banks = list(banks)
    n = len(banks)
    i = min(i for i, x in enumerate(banks) if x == max(banks))
    blocks = banks[i]
    banks[i] = 0
    for j in range(blocks):
        banks[(i + 1 + j) % n] += 1
    return tuple(banks)


seen = {banks: 0}
for c in count():
    banks = redestribute(banks)
    if banks in seen:
        print(c + 1)
        print(c + 1 - seen[banks])
        break
    seen[banks] = c + 1