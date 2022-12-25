with open("input") as f:
    inp = f.read().strip()

d = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
d2 = {2: "2", 1: "1", 0: "0", -1: "-", -2: "="}

def convert_to_base10(s):
    res = 0
    base = 1
    for x in s[::-1]:
        res += d[x]*base
        base *= 5
    return res

res_base10 = sum(map(convert_to_base10, inp.split("\n")))

res = ""
while res_base10 > 0:
    rem = res_base10%5
    rem = ((rem+2)%5) -2
    res += d2[rem]
    res_base10 = (res_base10-rem) // 5

print(res[::-1])