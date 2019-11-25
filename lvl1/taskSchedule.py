def answer(data,n):
	tasks = {}
	finalIds = []
	for i in data:
		tasks[i] = data.count(i)
		if tasks[i]<n:
			if i not in finalIds:
				finalIds.append(i)
	print(finalIds)

print("Problem: There are a bunch of minions who work for work for Empress Lambda.")
print("She clocks all the tasks by the minions in a list of their id's")
print("The minions have tasks assigned to them and have a list of when a minion is asked to perform a task")
print("The minions are easily disturbed and give up when asked to perform a task too many times")
print("Empress Lambda would like to know on any given day what work has been done by her minions")
print("compose an algorithm to take in the list of Id's of the minnions who got their work done")
print("we can assume that if a minion is asked too many times,N, that the work will not get done")
print("\n \n")
data = input("Enter list of numbers, with some multiples, here separate them by spaces :")
data = list(map(lambda x: int(x),data.split()))
n = int(input("enter the number of times it takes to frustrate a minion here :"))
print("here is the answer")
answer(data,n)

