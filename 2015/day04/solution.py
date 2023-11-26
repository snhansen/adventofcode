import hashlib 

inp = 'bgvyzdsv'

# Part 1
i = 1
while True:
    if hashlib.md5((inp+str(i)).encode()).hexdigest()[0:5] == '00000':
        break
    i += 1

# Part 2
while True:
    if hashlib.md5((inp+str(i)).encode()).hexdigest()[0:6] == '000000':
        break
    i += 1