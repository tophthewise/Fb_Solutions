def solution(l):
    # Your code here
    #first find the highest number in the list
    #remove it from the list and put it first in a string
    #parse string as an int we call num
    #check to see if num is divisble by 3
    #if yes : 
    #check to see if divisble by 3
    #i
    test_string1 = ""
    test_string2 = ""
    test_num  = 0
    list_of_possibilities =[]
    while len(l)>0:
       #gives us index to pop off highest number
        highest_num_index = l.index( int( max(l) ) )
        #pops off highest number
        highest_num = l.pop(highest_num_index)
        
        #adds it to the string
        test_string1 += str(highest_num)
        
        #if our number is divisible by 3 add to the list
        if int(test_string1)%3 == 0:
            list_of_possibilities.append(int(test_string1))
        
    return max(list_of_possibilities)
    
            
        
    
    