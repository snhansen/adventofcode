import ast

with open("input") as f:
    inp = f.read().strip()

ls = [[ast.literal_eval(y) for y in x.split("\n")] for x in inp.split("\n\n")]

def right_order(ls1, ls2):
    if isinstance(ls1, int) and isinstance(ls2, int):
        if ls1 > ls2:
            return False
        if ls1 < ls2:
            return True
        return None
    if isinstance(ls1, list) and isinstance(ls2, list):
        ls1 = list(ls1)
        ls2 = list(ls2)
        while True:
            if len(ls1) == 0 or len(ls2) == 0:
                return right_order(len(ls1), len(ls2))
            x1, x2 = ls1.pop(0), ls2.pop(0)
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
print(sum(i+1 for i, (ls1, ls2) in enumerate(ls) if right_order(ls1, ls2)))

# Part 2
ls = [ast.literal_eval(y) for x in inp.split("\n\n") for y in x.split("\n")]
div_packets = [[[2]], [[6]]]
ordered_list = [p for p in div_packets]

while ls:
    l1 = ls.pop()
    for i, l2 in enumerate(ordered_list):
        res = right_order(l1, l2)
        if res:
            ordered_list.insert(i, l1)
            break
    if l1 not in ordered_list:
        ordered_list.append(l1)
            
print((ordered_list.index(div_packets[0])+1)*(ordered_list.index(div_packets[1])+1))