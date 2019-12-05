
def solution(n):
	def count_stairs(arr,total):
		staircases = {}
		return recurring(arr,total,len(arr)-1,staircases)
	def recurring(arr,total,index,staircases):
		print("Index :"+ str(index))
		print("Total :" + str(total))
		staircase = str(total)+"|"+str(index)
		if staircase in staircases:
			return staircases[staircase]
		if total == 0:
			return 1
		elif total<0:
			return 0
		elif index<0:
			return 0
		elif total < arr[index]:
			will_return =  recurring(arr,total,index-1,staircases)
		else:
			will_return =  recurring(arr,total - arr[index],index-1,staircases) + recurring(arr,total,index-1,staircases)
		staircases[staircase] = will_return
		return will_return

	total_bricks = n
	bricks = []
	for i in range(total_bricks):
		bricks.append(i)
	return count_stairs(bricks,total_bricks)

a = solution(200)
print(a)