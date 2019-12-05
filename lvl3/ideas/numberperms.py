from itertools import permutations
def solution(n):
	def permspernum(total,nums):
		numbers = []
		if total%2>0:
			halfway= total/2
			x = halfway +1 
			y = halfway - 1
			numbers.append((total%2,x,y))
			for i in range(1,y,-1):
				halfway++
			 	while y > 0:
					x = halfway +1
					y = halfway -1 
					if sum(halfway,x,y) == n:
						numbers.append((halfway,x,y))
					


