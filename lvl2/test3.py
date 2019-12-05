from itertools import permutations,combinations
def solution(l):
	if(len(l)==0):
		return 0
	else:
		possibles = []
		def perm2Num(E):
			e = list(E)
			temp_e = ""
			for i in e:
				temp_e+=str(i)
			num = int(temp_e)
			return num
		for i in range(1,len(l)+1,1):
			perms1 = permutations(l,i)
			nums1 = list(map(perm2Num,perms1))
			#print(nums1)
			divisbles =[]
			for k in nums1:
				if k%3 == 0:
					divisbles.append(k)
			if len(divisbles) != 0:
				biggest_Num = max(divisbles)
				possibles.append(biggest_Num)
				#print(max(possibles))

		return max(possibles)
A = solution([])
print(A)
