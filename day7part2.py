from sys import stdin

xs = []
for i in stdin:
	xs.append((i.split()[1],i.split()[7]))

class Part:
	def __init__(self, letter):
		self.letter = letter
		self.dependsOn = []
		self.onDepends = []

	def link(self, part):
		self.dependsOn.append(part)
		part.onDepends.append(self)

def partCommparitor(part):
	return(part.letter)

parts = []
for i in range(26):
	parts.append(Part(chr(i + 65)))

for i in xs:
	parts[ord(i[1])-65].link(parts[ord(i[0])-65])

workers = [0]*5
workingOn = [0]*5
time = 0
ready = []

while ready != [] or not all(w == 0 for w in workers) or not all(w == 0 for w in workingOn) or parts != []:

	for i in parts:
		if i.dependsOn == []:
			ready.append(i)
			parts.remove(i)

	if ready != []:
		ready.sort(key = partCommparitor)

		for i in range(len(workers)):
			if ready != [] and workers[i] == 0:
				workers[i] = ord(ready[0].letter) - 4
				workingOn[i] = ready[0]
				del ready[0]

	for i in parts:
		if i.dependsOn == []:
			ready.append(i)
			parts.remove(i)

	for i in range(len(workers)):
		if workers[i] != 0:
			workers[i] -= 1
			if workers[i] == 0:
				for j in workingOn[i].onDepends:
					j.dependsOn.remove(workingOn[i])
				workingOn[i] = 0

	for i in parts:
		if i.dependsOn == []:
			ready.append(i)
			parts.remove(i)
				
	time += 1

print(time)