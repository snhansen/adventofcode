import re
with open("input") as f:
    *raw_shapes, regions = f.read().strip().split("\n\n")

regions = regions.split("\n")
shapes = []
for shape in raw_shapes:
    shapes.append({(x, y) for y, line in enumerate(shape.split()[1:]) for x, c in enumerate(line) if c == "#"})

ans = 0
for region in regions:
    w, l, *ns = list(map(int, re.findall(r"\d+", region)))
    ans += sum(n*len(shape) for n, shape in zip(ns, shapes)) <= w*l
    
print(ans)