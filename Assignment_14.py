
#Question 1
print("\n\nQ1.\n")

with open('Assignment_14.txt') as file:
    line =  file.readlines()        #reading lines from the file
from_end = line[::-1]               #reversing the read items

no_of_lines = int(input("How many lines from end?: "))  #lines to read from end
print(from_end[no_of_lines::-1])        #going back from the input , in the reversed list


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+



#Question 2
print("\n\nQ2.\n")

collection = []                                 #to store the words
with open("Assignment_14.txt") as file:
    data = file.readlines()                 #store lines of file as lists
    for line in data:                       #accesssing each line
        words = line.split()                #splitting the list
        collection += words                 #adding items to the collection list

key = input("What to search for ? : ")      #what to search

print("Word '%s' is occurring %d times "%(key,collection.count(key)))


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


#Question 3
print("\n\nQ3.\n")

with open('Assignment_14.txt') as file, open('Assignment_14_copy.txt','w') as file_copy:
    for line in file:       #copy line by line from one file to the other
        file_copy.write(line)
        
print("Copied to file named Assignment_14_copy.txt ")

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+



#Question 4
print("\n\nQ4.\n")

with open('Assignment_14.txt') as file1, open('Assignment_14_copy.txt') as file2:
    for line1,line2 in zip(file1, file2):           #zip used for unpacking the files
        print(line1+line2)                  #taking one line fom both of the files
        
#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+



#Question 5
print("\n\nQ5.\n")
import random               #for using random functions

with open('Assignment_14_random.txt','w') as file:
    for x in range(10):
        file.write(str(random.randint(1,10000))+" ")    #storing 10 random numbers in the file ,  ranginin from 1 to 10000

print("File Created !")

with open('Assignment_14_random.txt') as file , open('Assignment_14_randomsort.txt','w') as file_sort:
    for line in file:
        str_numbers = line.split()      #taking str type numbers from the list
        random_num=[]                   #making a list to store random int type 
        for num in str_numbers:         #loop to help make str as int
            random_num.append(int(num))
        random_num.sort()               #to sort the numbers , now as ints
        
        file_sort.write(str(random_num))    #to write it in ta different file

print("Numbers Sorted !")

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


