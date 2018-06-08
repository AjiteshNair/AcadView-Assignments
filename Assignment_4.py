#Question 1
print("\n\nQ1.\n")
a = (1 , 3.6 , True , "string")
print(a)
print("Length of the tuple is: ",len(a))



#Question 2
a = (54,7,23,65,28,17,1,45)
print("\n\nQ2.\n")
print("The tuple is : ",a)
print("The largest is %d and smallest is %d"%(max(a),min(a)))



#Question 3
print("\n\nQ3.\n")
a = (1,2,3,4,5)
print("Tuple is : ",a)
mult = 1
for item in a:
    mult *= item
print("The multiplication of all the elements is: ",mult)



#Question 4         SETS
print("\n\nQ4.\n")
a = {1,3,5,6,7}
b = {2,5,7,8}
print("Sets are ",a," and ",b)
print("Difference is : ",a-b)
print("Intersection is ",a&b)



#Question 5
print("\n\nQ5. \n")

keyz = [x for x in input("Enter name of the student(space seperated) :").strip().split()]
valuez = [int(x) for x in input("Enter marks(space seperated) :").strip().split()]
record = {}
i = 0
for item in keyz:
    record[item] = valuez[i]
    i+=1
print("The entered dict is ",record)

#Question 6
print("\n\nQ6.\n")
sorted_x = sorted(record, key=record.get)
print("Sorted dictionary is : ",sorted_x)



#Question 7
print("\n\nQ7.\n")
word = "MISSISSIPPI"

ans = {}
for letter in word:
    ans[letter] = word.count(letter)
print(word," has occurance amount as ",ans)
