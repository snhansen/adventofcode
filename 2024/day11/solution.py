from functools import cache

with open("input") as f:
    inp = f.read().strip()

stones = list(map(int, inp.split(" ")))


@cache
def get_no_stones(stone, n):
    if n == 0:
        return 1
    if stone == 0:
        res = get_no_stones(1, n - 1)
    elif len(s:= str(stone)) % 2 == 0:
        mid = len(s) // 2
        res = get_no_stones(int(s[:mid]), n - 1) + get_no_stones(int(s[mid:]), n - 1)
    else:
        res = get_no_stones(stone*2024, n - 1)
    return res


# Part 1
print(sum(get_no_stones(stone, 25) for stone in stones))

# Part 2
print(sum(get_no_stones(stone, 75) for stone in stones))