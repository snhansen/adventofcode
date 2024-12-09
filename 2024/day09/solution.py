from collections import deque

with open("input") as f:
    inp = f.read().strip()


filesys = []
for i, n in enumerate(inp):
    id_ = i//2 if i%2 == 0 else None
    filesys.append((id_, int(n), i%2 != 0)) #(id, length, free)


# Part 1
q = deque(filesys)
res = []
while q:
    id1, n1, free1 = q.popleft() 
    if free1:
        if not q:
            continue
        id2, n2, free2 = q.pop()
        if free2:
            q.appendleft((id1, n1, free1))
            continue
        if n2 < n1:
            res.append((id2, n2))
            q.appendleft((None, n1-n2, True))
        elif n2 > n1:
            res.append((id2, n1))
            q.append((id2, n2-n1, False))
        else:
            res.append((id2, n2))
    else:
        res.append((id1, n1))
        

ans, i = 0, 0
for id_, n in res:
    for _ in range(n):
        if id_ is not None:
            ans += id_*i
        i += 1
print(ans)


# Part 2
max_id = max(id_ for id_, _, _ in filesys if id_ is not None)
cur_id = max_id

while cur_id > 0:
    for pos1, (id1, n1, free1) in enumerate(filesys):
        if id1 == cur_id:
            break
    for pos2, (id2, n2, free2) in enumerate(filesys):
        if pos2 == pos1:
            break
        if not free2:
            continue
        if n1 <= n2:
            filesys = filesys[:pos2] + [(id1, n1, free1)] + [(None, n2-n1, True)] + filesys[(pos2+1):pos1] + [(None, n1, True)] + filesys[(pos1+1):]
            break

    cur_id -= 1

ans, i = 0, 0
for id_, n, _ in filesys:
    for _ in range(n):
        if id_ is not None:
            ans += id_*i
        i += 1

print(ans)