with open('input') as f:
    inp = [x.strip('\n') for x in f.readlines()]

obj1 = [x.split(')')[1] for x in inp]
obj2 = [x.split(')')[0] for x in inp]


def total_no_elem(x):
    return sum(len(elem) for elem in x)


x = 0
orbit_chain = []

for i, obj in enumerate(obj1):
    orbit_chain.append([obj])
    obj_to_match = obj
    while True:
        for j in range(len(obj2)):
            if obj1[j] == obj_to_match:
                orbit_chain[i].append(obj2[j])
                obj_to_match = obj2[j]
                break
        if total_no_elem(orbit_chain) == x:
            break
        else:
            x = total_no_elem(orbit_chain)

# Part 1
print(total_no_elem(orbit_chain) - len(orbit_chain))

# Part 2
me = [x for x in orbit_chain if x[0] == 'YOU'][0]
santa = [x for x in orbit_chain if x[0] == 'SAN'][0]

for obj in me:
    if obj in santa:
        common_obj = obj
        break

print(santa.index(common_obj) + me.index(common_obj) - 2)
