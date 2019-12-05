from itertools import combinations, chain
from functools import lru_cache
	
@lru_cache(maxsize = 20)
def sum_to_n(n):
    from operator import sub
    b, mid, e = [0], list(range(1, n)), [n]
    splits = (d for i in range(n) for d in combinations(mid, i)) 
    return (list(map(sub, chain(s, e), chain(b, s))) for s in splits)

@lru_cache(maxsize = 1000)
def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)

def duplicate_and_lengthCheck(n):
    for i in n:
    	if n.count(i)>1 or len(n)<2:
    		return False
    return True 


Total_staircases = {}
a = []
b=[]
for k in range(4,21):
	for l in range(1,k+1):
		b.append(l)
	for j in range(1,k+1):
		a.append(j)
	print(b)
	for i in subset_sum(b,20):
		if duplicate_and_lengthCheck(i):
			i.sort()
			Total_staircases[str(i)] = str(i)
	print(len(Total_staircases))



