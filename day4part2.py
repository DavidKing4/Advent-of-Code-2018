from sys import stdin

xs = []
guardsMinu = [[0 for _ in range(60)] for _ in range(3400)]

for i in stdin:
	xs.append(i.split())

def timeSort(x):
	return(int(x[0].split('-')[1] + x[0].split('-')[2] + x[1].split(':')[0] + x[1].split(':')[1][:-1])) #keke

xs.sort(key = timeSort)

for i in range(len(xs)):
	if xs[i][2] == "Guard":
		currentGuard = int(xs[i][3][1:])
	elif xs[i][2] == "falls":
		sleep = int(xs[i][1].split(':')[0] + xs[i][1].split(':')[1][:-1])
		awake = int(xs[i + 1][1].split(':')[0] + xs[i + 1][1].split(':')[1][:-1])

		for j in range(sleep, awake):
			guardsMinu[currentGuard][j] += 1

guard = 0
minu = 0
minuMax = 0
for i in range(3400):
	for j in range(60):
		if guardsMinu[i][j] > minuMax:
			minuMax = guardsMinu[i][j]
			minu = j
			guard = i

print(minu*guard)