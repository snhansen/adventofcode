import hashlib
from collections import deque

passcode = "qzthpkfp"


def get_dirs(path):
    dirs = [-1j, 1j, -1, 1]
    hash_ = hashlib.md5((passcode + path).encode()).hexdigest()
    hash_ = hash_[:4]
    return [dirs[i] for i, c in enumerate(hash_[:4]) if "b" <= c <= "f"]
        

dirs_letter = {1: "R", -1: "L", 1j: "D", -1j: "U"}
first = True
longest_path = 0
q = deque([(0, "")])
seen = set()
while q:
    p, path = q.popleft()
    if (p, path) in seen:
        continue
    if p == 3+3*1j:
        longest_path = max(longest_path, len(path))
        if first:
            print(path)
            first = False
        continue
    seen.add((p, path))
    for dp in get_dirs(path):
        new_p = p + dp
        if not (0 <= new_p.real <= 3 and 0 <= new_p.imag <= 3):
            continue
        q.append((new_p, path + dirs_letter[dp]))

print(longest_path)