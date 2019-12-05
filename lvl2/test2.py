from itertools import permutations
def solution(l):
	perms = permutations(l)
	possibles = []
	def perm2Num(E):
		e = list(E)
		temp_e = ""
		for i in e:
			temp_e+=str(i)
		num = int(temp_e)
		return num
	nums = list(map(perm2Num,perms))
	for i in range(len(l),0,-1):
		perms1 = permutations(l,i)
		nums1 = list(map(perm2Num,perms1))

		print(nums)
		divisbles =[]
	for k in nums1:
			#print(type(k))
			#print(k%3==0)
		if k%3 == 0:
			divisbles.append(k)
	if len(divisbles) != 0:
		biggest_Num = max(divisbles)
		possibles.append(biggest_Num)
	else:
		possibles = 0
			#print(biggest_Num)
	#print(max(possibles))
	return max(possibles)
solution([3,1,4,1])
