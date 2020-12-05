with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

def partition(s, n):
	lower = 0
	upper = n
	for c in s:
		length = upper-lower+1
		if c in ['F', 'L']:
			upper = int(upper - length/2)
		elif c in ['B', 'R']:
			lower = int(lower + length/2)
	return lower

def get_seat(s):
	return partition(s[0:7], 127), partition(s[7:10], 7)

# Part 1
seats = [get_seat(s)[0]*8+get_seat(s)[1] for s in inp]
print(max(seats))

# Part 2
open_seats = list(set(i for i in range(max(seats)+1)) - set(seats))
for i in open_seats:
	if i + 1 not in open_seats and i - 1 not in open_seats:
		print(i)