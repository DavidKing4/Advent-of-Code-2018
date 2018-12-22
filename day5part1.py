s = input()

i = 1
while i < len(s):
	if s[i - 1].swapcase() == s[i]:
		s = s[:i - 1] + s[i + 1:]
		i -= 1 if i == 1 else 2
	i += 1

print(len(s))