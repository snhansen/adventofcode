with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

# Part 1
def is_nice_string(s):
    vowels = 'aeiou'
    if any(x in s for x in ['ab', 'cd', 'pq', 'xy']):
        return False
    
    nice1, nice2 = False, False
    
    count = 0
    for v in vowels:
        count += s.count(v)
        if count >= 3:
            nice1 = True
            break
        
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            nice2 = True
            break
        
    return nice1 and nice2      
 
print(sum([is_nice_string(s) for s in inp]))

# Part 2
def req1(s):
    for i in range(len(s)-1):
        if s.count(s[i:i+2]) >= 2:
            return True
    return False
        
def req2(s):
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            return True
    
    return False

print(sum([req1(s) and req2(s) for s in inp]))
            