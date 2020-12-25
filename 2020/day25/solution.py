card_pub = 13233401
door_pub = 6552760

val = 1
count = 0
i = 0
while True:
    val = val*7 % 20201227
    i += 1
    if val == card_pub:
        card_loop = i
        count += 1
    elif val == door_pub:
        door_loop = i
        count += 1
    if count == 2:
        break

val = 1
for i in range(card_loop):
    val = val*door_pub % 20201227

print(val)