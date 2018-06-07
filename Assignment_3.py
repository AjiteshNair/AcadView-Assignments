
#Question 1
#Enter space to split the inputs
print("\n\nQ1.\n")
a = [x for x in input(" Enter the list(space seperated) : ").strip().split()]
print("\nYour list is : ",a)



#Question 2
print("\n\nQ2.\n")
b = ['google','apple','facebook','microsoft','tesla'] 
print("List before adding : ",a)
print("\n List after adding : ",a+b)



#Question 3
print("\n\nQ3.\n")
a = [1,2,3,4,1,1,5,6,2,4,2,2,3,5,1]
print("\n Consider the given list: ",a)
ch = int(input(" Count occurence of? : "))
print(" %d is occuring %d times"%(ch,a.count(ch)))



#Question 4
print("\n\nQ4.\n")
print("Before sorting ",a)
a.sort()
print("After sorting",a)



#Question 5
print("\n\nQ5.\n")
a = [1,2,5,8,9]
b = [2,3,4,7,9]
print("The list are",a," and ",b)
c = a+b
c.sort()
print(" After merging ",c)



#Question 6
print("\n\nQ6.\n")
"""
#traversing occurs as last in first out in stack , ie, reverse
#traversing occurs FIFO in queue , same as the we input in the list
"""
a = [int(x) for x in input(" Enter the list(space seperated) : ").strip().split()]
print("\n STACK in traversal order : ",a[::-1])        #incrementing by -1 , by default reversing
print("\n QUEUE in traversal order : ",a)              #exactly the way it was entered FIFO



#Question 7
print("\n\nQ7.\n")
a = [int(x) for x in input(" Enter the list(space seperated) : ").strip().split()]
even,odd=0,0
for item in a:
    if item%2==0:
        even+=1
    else:
        odd+=1
print("\n Number of Evens is %d and odds is %d "%(even,odd))
