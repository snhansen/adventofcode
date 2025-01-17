import re
from collections import defaultdict

with open("input") as f:
    inp = f.read().strip().split("\n")

records = []
for line in inp :
    year, month, day, hour, minute, *rest = list(map(int, re.findall("\d+", line)))
    if "shift" in line:
        event = rest[0]
    elif "asleep" in line:
        event = -1
    elif "wakes" in line:
        event = 0
    records.append((month, day, hour, minute, event))

records = sorted(records)

sleep = defaultdict(list)
for record in records:
    month, day, hour, minute, event = record
    if event > 0:
        cur_id = event
    elif event == -1:
        start_minute = minute
    elif event == 0:
        sleep[cur_id].append((month, day, start_minute, minute - 1))

# Part 1
def days_asleep(id_, n):
    res = 0
    for _, _, start, end in sleep[id_]:
        res += (start <= n <= end)
    return res


max_ = 0
for id_, ranges in sleep.items():
    minutes = sum(end - start + 1 for (_, _, start, end) in ranges)
    if minutes > max_:
        max_ = minutes
        max_id = id_

max_ = 0
for n in range(60):
    val = days_asleep(max_id, n)
    if val > max_:
        max_ = val
        max_minute = n
        
print(max_id*max_minute)
        
# Part 2
max_ = 0
for id_, ranges in sleep.items():
    for n in range(60):
        val = days_asleep(id_, n)
        if val > max_:
            max_ = val
            max_id = id_
            max_minute = n
            
print(max_id*max_minute)