import time
import math
import os
import datetime
from datetime import date

#Question 1
print("\n\nQ1.\n")
print("Time tuple is a tuple which contains 9 attributes in sequence , namely , year , month , date , hour , minute , seconds , day , day of year , DST")

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

#Question 2
print("\n\nQ2.\n")
print("Formatted time is: ",time.asctime())

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

#Question 3
print("\n\nQ3.\n")
print("Month is :",time.ctime()[4:7],"and the month number is:",time.gmtime()[1])

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

#Question 4
print("\n\nQ4.\n")
print("It is ",time.ctime()[:4],", day ",time.gmtime()[6]+1," of the week")

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

#Question 5
print("\n\nQ5.\n")

print("Todays Date is :",time.gmtime()[2])


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

#Question 6
print("\n\nQ6.\n")
print("Local Time is %d : %d : %d"%(time.localtime()[3],time.localtime()[4],time.localtime()[5]) ) #printing components of tuple time individually

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+



#Question 7
print("\n\nQ7.\n")
num = int(input("Enter number:"))
print("Factorial is : ",math.factorial(num)) 

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

#Question 8
print("\n\nQ8.\n")
print("Enter 2 space seperated numbers to find gcd : ",end='')
x,y = [int(num) for num in input().strip().split()]                 #creating a list and feeding values to x and y
print("GCD is : ",math.gcd(x,y))

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

#Question 9
print("\n\nQ9.\n")
print("The current Directory is :",os.getcwd())
print("\n\nThe User environment is : ",os.environ)

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
