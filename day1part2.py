from sys import stdin

inputs = []
for i in stdin:
	inputs.append(int(i))

def f(inputs):
	total = 0
	prevTotals = {0}

	while True:
		for i in inputs:
			total += i
			if total in prevTotals:
				print(total)
				return
			prevTotals.add(total)

f(inputs)