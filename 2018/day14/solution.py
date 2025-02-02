class Recipe:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


inp = 580741
a = Recipe(3)
b = Recipe(7)
a.next = b
a.prev = b
b.next = a
b.prev = a
last_six = [a.value, b.value]
target = [int(v) for v in str(inp)]
first = a
last = b

n = 0
stop = False
while True:
    for v in str(a.value + b.value):
        new_recipe = Recipe(int(v))
        new_recipe.prev = last
        new_recipe.next = first
        first.prev = new_recipe
        last.next = new_recipe
        last = new_recipe
        last_six.append(int(v))
        last_six = last_six[-6:]
        n += 1
        if last_six == target:
            print(n - 4)
            stop = True
    for _ in range(1 + a.value):
        a = a.next
    for _ in range(1 + b.value):
        b = b.next
    if stop:
        break
    if n == inp + 8:
        res = ""
        cur = last
        for _ in range(10):
            res += str(cur.value)
            cur = cur.prev
        print(res[::-1])