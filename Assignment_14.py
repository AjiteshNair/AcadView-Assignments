
#Question 1
print("\n\nQ1.\n")




#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+



#Question 2
print("\n\nQ2.\n")

collection = []
with open("Assignment_14.txt") as file:
    data = file.readlines() 
    for line in data: 
        words = line.split()
        collection += words

key = input("What to search for ? : ")

print("Word '%s' is occurring %d times "%(key,collection.count(key)))


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


#Question 3
print("\n\nQ3.\n")

with open('Assignment_14.txt') as file, open('Assignment_14_copy.txt','w') as file_copy:
    for line in file:
        file_copy.write(line)
        
print("Copied to file named Assignment_14_copy.txt ")

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+



#Question 4
print("\n\nQ4.\n")

with open('Assignment_14.txt') as file1, open('Assignment_14_copy.txt') as file2:
    for line1,line2 in zip(file1, file2):
        print(line1+line2)
        
#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+



#Question 5
print("\n\nQ5.\n")
import random

with open('Assignment_14_random.txt','w') as file:
    for x in range(10):
        file.write(str(random.randint(1,10000))+" ")

print("File Created !")

with open('Assignment_14_random.txt') as file , open('Assignment_14_randomsort.txt','w') as file_sort:
    for line in file:
        str_numbers = line.split()
        random_num=[]
        for num in str_numbers:
            random_num.append(int(num))
        random_num.sort()
        
        file_sort.write(str(random_num))

print("Numbers Sorted !")

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


