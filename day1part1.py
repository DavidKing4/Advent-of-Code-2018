from sys import stdin

total = 0
for i in stdin:
	if i[0] == "+":
		total += int(i[1:])
	if i[0] == "-":
		total -= int(i[1:])

print(total)