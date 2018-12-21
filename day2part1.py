from sys import stdin

inputs = []
for i in stdin:
	inputs.append(i[:-1])

twosThrees = [0, 0]
for i in inputs:
	a = [0]*26

	for j in i:
		a[ord(j) - 97] += 1

	if 2 in a:
		twosThrees[0] += 1

	if 3 in a:
		twosThrees[1] += 1

print(twosThrees[0]*twosThrees[1])