import ast

with open("input") as f:
    inp = f.read().strip()

ls = [[ast.literal_eval(y) for y in x.split("\n")] for x in inp.split("\n\n")]

def right_order(s1, s2):
    if isinstance(s1, int) and isinstance(s2, int):
        if s1 > s2:
            return False
        if s1 < s2:
            return True
        return None
    if isinstance(s1, list) and isinstance(s2, list):
        s1 = list(s1)
        s2 = list(s2)
        while True:
            if len(s1) == 0 and len(s2) > 0:
                return True
            elif len(s2) == 0 and len(s1) > 0:
                return False
            elif len(s1) == 0 and len(s2) == 0:
                return None
            x1 = s1.pop(0)
            x2 = s2.pop(0)
            if isinstance(x1, int) and isinstance(x2, list):
                x1 = [x1]
            if isinstance(x1, list) and isinstance(x2, int):
                x2 = [x2]
            res = right_order(x1, x2)
            if res is None:
                continue
            else:
                return res
        

# Part 1
print(sum([i+1 for i, (ls1, ls2) in enumerate(ls) if right_order(ls1, ls2)]))

# Part 2
ls = [ast.literal_eval(y) for x in inp.split("\n\n") for y in x.split("\n")]
div_packets = [[[2]], [[6]]]
ordered_list = [p for p in div_packets]

while ls:
    l = ls.pop()
    for i, l2 in enumerate(ordered_list):
        res = right_order(l, l2)
        if res:
            ordered_list.insert(i, l)
            break
    if l not in ordered_list:
        ordered_list.append(l)
            
print((ordered_list.index(div_packets[0])+1)*(ordered_list.index(div_packets[1])+1))