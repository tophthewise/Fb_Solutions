import numpy as np
def solution(n,b):
	#take in number 
	#convert to string 
	num = str(n)
	# take in base as constant 
	base = int(b)
	#using new numString create length for other calculation
	length = len(num)
	old_num = 0
	nums = {n:0}
	total_duplicates = []
	while nums[num]<3:
		x = list(num)
		y = list(num)
		y.sort()
		x.sort(reverse = True)
		x= "".join(x)
		y= "".join(y)
		if b == 10:
			z = int(x) - int(y)
		else:
			x = int(x,b)
			y = int(y,b)
			z = x - y
		z = np.base_repr(z,b)
		old_num = int(num)
		if len(z)< length:
			pad = length - len(z)
			z = int(z,b)
			z = np.base_repr(z,b, padding = pad)
		num = z
		if num in nums:
			nums[num]+=1
		else:
			nums[num] = 1
	for i in nums:
		if nums[i]>1:
			total_duplicates.append(i)
	return len(total_duplicates)

