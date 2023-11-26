inp = '1113222113'

def look_and_say(x):
    res = []
    l = [0] + [i+1 for i in range(len(x)-1) if x[i] != x[i+1]] + [len(x)]
    for i in range(len(l)-1):
        res.append(len(x[l[i]:l[i+1]]))
        res.append(x[l[i]])
    return ''.join([str(y) for y in res])
 
for _ in range(40):
    inp = look_and_say(inp)
   
print(len(inp))
 
for _ in range(10):
    inp = look_and_say(inp)
 
print(len(inp))