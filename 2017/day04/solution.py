from itertools import combinations

with open("input") as f:
    inp = f.read().strip().split("\n")

passphrases = [line.split(" ") for line in inp]

# Part 1
print(sum(1 for passphrase in passphrases if len(passphrase) == len(set(passphrase))))

# Part 2
ans = 0
for passphrase in passphrases:
    if any(set(word1) == set(word2) for word1, word2 in combinations(passphrase, 2)):
        continue
    ans += 1

print(ans)