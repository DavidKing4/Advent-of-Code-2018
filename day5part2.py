s = [input()]*26

for i in range(len(s)):
	s[i] = s[i].replace(chr(i + 65), '')
	s[i] = s[i].replace(chr(i + 97), '')

mini = 50_000
for i in s:
	j = 1
	while j < len(i):
		if i[j - 1].swapcase() == i[j]:
			i = i[:j - 1] + i[j + 1:]
			j -= 1 if j == 1 else 2
		j += 1

	if len(i) < mini: mini = len(i)

print(mini)