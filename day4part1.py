from sys import stdin

xs = []
guardsTotal = [0 for _ in range(3400)]
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

		guardsTotal[currentGuard] += (awake - sleep)

		for j in range(sleep, awake):
			guardsMinu[currentGuard][j] += 1

maxTime = 0
maxTimePos = 0
for i in range(len(guardsTotal)):
	if guardsTotal[i] > maxTime:
		maxTimePos = i
		maxTime = guardsTotal[i]

maxMinSlept = 0
maxMinSleptPos = 0
for i in range(len(guardsMinu[maxTimePos])):
	if guardsMinu[maxTimePos][i] > maxMinSlept:
		maxMinSleptPos = i
		maxMinSlept = guardsMinu[maxTimePos][i]
print(maxMinSleptPos * maxTimePos)