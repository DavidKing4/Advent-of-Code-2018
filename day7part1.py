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

ready = []
do = True
while ready != [] or do:
	do = False

	for i in parts:
		if i.dependsOn == []:
			ready.append(i)
			parts.remove(i)

	if ready != []:
		ready.sort(key = partCommparitor)
		print(ready[0].letter)
		for i in ready[0].onDepends:
			i.dependsOn.remove(ready[0])
		del ready[0]
		do = True