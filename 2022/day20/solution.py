with open("input") as f:
    inp = f.read().strip()


class Item:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None


def solve(part2 = False):
    mult = 811589153 if part2 else 1
    ll = [Item(num*mult) for num in nums] 
    for i, item in enumerate(ll):
        item.next = ll[(i+1)%len(ll)]
        item.prev= ll[(i-1)%len(ll)]
    
    for _ in range(10 if part2 else 1):
        for item in ll:
            moves = item.value % (len(ll)-1)
            if moves == 0:
                continue
            item.prev.next = item.next
            item.next.prev = item.prev
            ins_prev = item.prev
            ins_next = item.next
            for _ in range(moves):
                ins_prev = ins_prev.next
                ins_next = ins_next.next
            ins_prev.next = item
            item.prev = ins_prev
            ins_next.prev = item
            item.next = ins_next


    item = next(p for p in ll if p.value == 0)
    res = 0
    for _ in range(3):
        for _ in range(1000):
            item = item.next
        res += item.value
    return res

nums = list(map(int, inp.split("\n")))

# Part 1
print(solve())

# Part 2
print(solve(True))