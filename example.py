
import this
outputList = []

for i, character in enumerate(this.s):
	try:
		outputList.append(this.d[character])
	except:
		pass

for char in outputList:
	print char
#print outputList