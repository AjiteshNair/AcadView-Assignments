
#Question 1
print("\n\nQ1.\n")

#for space seperated inputs:
#x = [int(x) for x in input().strip().split()]
#taking 5 inputs only for sake of simplicity
x = []
for i in range(5):
    x.append(int(input("\n Enter integer number %d : "%(i+1))))

print("\nThe entered numbers are : ",end=''
      )
for item in x:
    print(item,end=" ")




#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+




#Question 2
print("\n\nQ2.\n")
#while(True):         #remove this line's comment at your own risk
    print("Need job for experience ")
    print("Need experience for job ")




#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


   

#Question 3
print("\n\nQ3.\n")
x = [int(x) for x in input("Enter space seperated integers : ").strip().split()]
sq_x = []
for item in x:
    sq_x.append(item*item)
print("The new list is : ",sq_x)



#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+




#Question 4
print("\n\nQ4.\n")
x = [1 , 5.8 , 8.65 , "hello" , 2 , "world" , 2.5 , 131]
#ints = [item for item in x if isinstance(item,int)]
ints = []
floats = []
strings = []
for item in x :
    if type(item) == int:
        ints.append(item)
    if type(item) == float:
        floats.append(item)
    if type(item) == str:
        strings.append(item)
    
print("Ints: ",ints,"\nFloats: ",floats,"\nStrings: ",strings)





#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+




#Question 5
print("\n\nQ5.\n")
even,odd = [],[]
for x in range(1,101,2):
    odd.append(x)
    even.append(x+1)
odd.append(101)
print("ODDS: ",odd)
print("\nEVENS: ",even)





#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+




#Question 6
print("\n\nQ6.\n")
for i in range(4):
    print("* "*(i+1))




#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+




#Question 7
print("\n\nQ7.\n")
d = {'name' : 'Voldemort' , 'title' : 'The "you know who"' , 'power' : 300 }
for x,y in d.items():
    print("Key: ",x," -> Value: ",y)




#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+




#Question 8
print("\n\nQ8.\n")
x = [int(x) for x in input("Enter space seperated integers : ").strip().split()]
search_key = int(input("What to search and destroy?: "))
if search_key in x:
    x.remove(search_key)
    print("Deleted. ")
else:
    print("Key not found")
print("List is :",x)
