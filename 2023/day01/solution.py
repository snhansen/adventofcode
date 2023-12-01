import re

with open("input") as f:
    inp = f.read().split()

# Part 1
res = 0
for line in inp:
    num = re.findall("[0-9]", line)
    val = int(num[0]+num[-1])
    res += val
    
print(res)

# Part 2
numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
numbers_all = list(numbers.keys()) + list(numbers.values())

def find_first(s):
    for i in range(len(s)):
        for num in numbers_all:
            if s[i:(i+len(num))] == num:
                if num in numbers.keys():
                    num = numbers[num]
                return num


def find_last(s):
    s = s[::-1]
    for i in range(len(s)):
        for num in numbers_all:
            if s[i:(i+len(num))] == num[::-1]:
                if num in numbers.keys():
                    num = numbers[num]
                return num


res = 0
for line in inp:
    res += int(find_first(line) + find_last(line))
print(res)