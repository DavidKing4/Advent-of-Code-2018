from sys import stdin

fabric = [[0 for _ in range(1000)] for _ in range(1000)]
count = 0

for i in stdin:
	x = int(i.split()[2].split(',')[0])
	y = int(i.split()[2].split(',')[1][:-1])
	w = int(i.split()[3].split('x')[0])
	h = int(i.split()[3].split('x')[1])

	for j in range(w):
		for k in range(h):
			if fabric[x + j][y + k] == 0:
				fabric[x + j][y + k] = 1
			elif fabric[x + j][y + k] == 1:
				count += 1
				fabric[x + j][y + k] = 2

print(count)