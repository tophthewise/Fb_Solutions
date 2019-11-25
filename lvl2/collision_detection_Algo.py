def answer(s):
	slist = list(s)
	salutes = 0
	for i in range(len(slist)):
		if slist[i] == '<':
			salutes += slist[:i].count('>')
		if slist[i] == '>':
			salutes += slist[i:].count('<')
	print(salutes)
s = "--->-><-><-->-"

answer(s)
