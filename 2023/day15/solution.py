import re
from collections import defaultdict

with open("input") as f:
    inp = f.read().strip()

steps = inp.split(",")

def get_val(seq):
    val = 0
    for x in seq:
        val += ord(x)
        val *= 17
        val = val % 256
    return val

# Part 1
print(sum(map(get_val, steps)))
 
# Part 2 
boxes = defaultdict(lambda: defaultdict(list))

for step in steps:
    label = re.findall("(\w+)[=-]", step)[0]
    oper = re.findall("[=-]", step)[0]
    box = get_val(label)
    if oper == "=":
        n = re.findall("\d+", step)[0]
        try:
            i = boxes[box]["label"].index(label)
            boxes[box]["focal"][i] = int(n)
        except ValueError:
            boxes[box]["label"].append(label)
            boxes[box]["focal"].append(int(n))
    elif oper == "-":
        try:
            i = boxes[box]["label"].index(label)
            boxes[box]["label"].pop(i)
            boxes[box]["focal"].pop(i)
        except ValueError:
            pass


ans = 0
for box in range(256):
    if not boxes[box]["label"]:
        continue
    for slot, focal in enumerate(boxes[box]["focal"]):
        ans += (box+1)*(slot+1)*focal

print(ans)     