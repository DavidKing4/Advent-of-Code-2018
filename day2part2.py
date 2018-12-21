from sys import stdin

inputs = []
for i in stdin:
	inputs.append(i[:-1])

def f(i, j, xs):
	eq = True
	index = 0
	for k in range(len(xs[i])):
		if xs[i][k] != xs[j][k]:
			if eq == True:
				eq = False
				index = k
			else:
				return
	if(eq == False):
		print(xs[i][:index] + xs[i][index + 1:])

for i in range(len(inputs) - 1):
	for j in range(i + 1,len(inputs) - 1):
		f(i,j, inputs)