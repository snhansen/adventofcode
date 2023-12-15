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
        val %= 256
    return val

# Part 1
print(sum(map(get_val, steps)))
 
# Part 2 
boxes = defaultdict(dict)

for step in steps:
    label = re.findall("(\w+)[=-]", step)[0]
    oper = re.findall("[=-]", step)[0]
    box = get_val(label)
    if oper == "=":
        n = re.findall("\d+", step)[0]
        boxes[box][label] = int(n)
    elif oper == "-":
        if label in boxes[box]:
            boxes[box].pop(label)   


  
print(
    sum(
        (box + 1)*(slot + 1)*focal 
        for box in boxes.keys()
        for slot, (_, focal) in enumerate(boxes[box].items())
    )
)