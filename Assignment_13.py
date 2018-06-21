
#Question 1
print("\n\nQ1.\n")



a = 3
if a<4 :
    try:
        a = a/(a-3)

    except ZeroDivisionError:
        print("ERROR : ZeroDivisionError\nCannot divide my zero! value of a remains unchanged :",end=' ')

    else:
        print("Succesful updated value:",end=' ')

    finally:
        print(a)



#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+



#Question 2
print("\n\nQ2.\n")
l=[1,2,3]

try:
    print(l[3])
    
except IndexError:
    print("ERROR: IndexError\nPlease do remember list has only 3 elements , 0-2 index")
    

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+



#Question 3
print("\n\nQ3.\n")

try:
    raise NameError("Hi there")  # Raise Error displaying Hi there

except NameError:
    print("An exception")
 #   raise # Raises a user defined error : NameError


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+



#Question 4
print("\n\nQ4.\n")

def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)

# Driver program to test above function
AbyB(2.0, 3.0)      #5.0/-1.0 prints c , ie , -5.0
AbyB(3.0, 3.0)      #a-b becomes 0 thus , handled by ZeroDivisionError



#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+



#Question 5
print("\n\nQ5.\n")

try:
    import kuchhbhi

except ImportError:                             
    print("Matlab kuchh bhi import karoge?")     

try:
    y = int(input("\nEnter number(or dont , for a exception): "))
    
except ValueError:
    print("Oh well , someone failed bad ")

else:
    print("Error handling me error avoid kar dia? ....wah.")

try:
    print(l[3]) #acessing previously made list of 3 elements

except IndexError:
    print("\nAgain , index out of bounds error :( ")

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+



#Question 6
print("\n\nQ6.\n")

class AgeTooSmallError(Exception):          #creates a user defined error
    pass

try:
    age = int(input("Enter a legal age(above or equal to 18): "))
    while age<18 :
        raise AgeTooSmallError              #raises the error we defined

except AgeTooSmallError:
    while age<18 :
        age = int(input("\n\nERROR , age too small, enter again : "))

except ValueError:
    print("\n Ab ye galat daal dia na")             #if non number values are inputted

finally:
    print("\nThat wasnt so hard , was it? :P")
    
    


    
#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

