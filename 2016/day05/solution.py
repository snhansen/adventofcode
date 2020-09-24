import hashlib 

inp = 'ugkcyxxp'

pw1 = ''
pw2 = [None]*8
i = 0
while True:
    hash = hashlib.md5((inp+str(i)).encode()).hexdigest()
    if hash[0:5] == '00000':
        if len(pw1)<8:
            pw1 += hash[5]
        if hash[5].isnumeric() and 0<=int(hash[5])<=7 and not pw2[int(hash[5])]:
            pw2[int(hash[5])] = hash[6]
    if len([x for x in pw2 if x]) == 8:
        break
    i += 1

print(pw1)
print(''.join(pw2))