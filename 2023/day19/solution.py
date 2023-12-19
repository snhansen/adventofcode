from copy import deepcopy

with open("input") as f:
    inp = f.read().strip()

inp1, inp2 = inp.split("\n\n")

ratings = []
for line in inp2.split("\n"):
    d = {}
    for nums in line[1:-1].split(","):
        c, n = nums.split("=")
        d[c] = int(n)
    ratings.append(d)


workflows = {}
for line in inp1.split("\n"):
    name, s = line[:-1].split("{")
    parts = s.split(",")
    rules = {c: [1, 4000] for c in ["x", "m", "a", "s"]}
    outs = []
    for part in parts:
        if ":" in part:
            cond, to = part.split(":")
            var = cond[0]
            symbol = cond[1]
            n = int(cond[2:])
            new_rules = deepcopy(rules)
            if symbol == "<":
                new_rules[var][1] = min(new_rules[var][1], n-1)
                rules[var][0] = max(rules[var][0], n)
            elif symbol == ">":
                new_rules[var][0] = max(new_rules[var][0], n+1)
                rules[var][1] = min(rules[var][1], n)
            outs.append((to, new_rules))
        else:
            outs.append((part, rules))
    workflows[name] = outs


def combine_rules(rules1, rules2):
    if not rules1:
        return rules2
    rules = {}
    for var in ["x", "m", "a", "s"]:
        lower = max(rules1[var][0], rules2[var][0])
        upper = min(rules1[var][1], rules2[var][1])
        if upper < lower:
            return None
        rules[var] = [lower, upper]
    return rules


paths = [("in", {})]
while (any(node not in ["A", "R"] for node, _ in paths)):
    new_paths = []
    for in_, rules in paths:
        if in_ in ["A", "R"]:
            new_paths.append((in_, rules))
            continue
        for new_out, new_rules in workflows[in_]:
            combined_rules = combine_rules(rules, new_rules)
            if combined_rules is not None:
                new_paths.append((new_out, combined_rules))
        paths = new_paths

# Part 1
ans = 0
for rating in ratings:
    for out, rules in paths:
        cont = False
        if all((rules[c][0] <= v) and (v <= rules[c][1]) for c, v in rating.items()):
            if out == "A":
                ans += sum(rating.values())
            break

print(ans)

# Part 2
ans = 0
for out, rules in paths:
    if out == "A":
        subans = 1
        for lower, upper in rules.values():
            subans *= (upper-lower+1)
        ans += subans

print(ans)