def solution(l):
	templist = []
	r = l
	p = l
	counter = {}
	def parseInt(x):
		return int(x)
	def perms(n,l):
		def parseInt(x):
			return int(x)
		num_perms= []
		for t in range(len(l)):
			counter[l[t]] = l.count(l[t])
			#this statement below needs to be redone and thought out carefully
			if n%10 != l[t]:
				num_perms.append(str(n)+str(l[t]))
			
		return list(num_perms)
	




	n = r.pop(p.index(max(l)));
	templist = perms(n,p)
	temp = map(parseInt,templist)
	templist = list(temp)
	print(templist)
	templist2 =[]
	q = p
	s = p

	for i in templist:
		templist2 += perms(i,r)
	#print(templist2)
# pop from s to give the new list based on the i Index/object then repeat the perms using i and s 
	temp2 = map(parseInt,templist2)
	templist2 = list(temp2)
	templist3 = []
	print(s)
	print(templist2)
	s.pop(s.index(templist2[0]%10))
	for i in range(len(templist2)):
		templist3+=perms(templist2[i],s)
	print(templist3)
solution([3,1,4,1])