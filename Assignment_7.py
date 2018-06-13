
#Question 1
print("\n\nQ1.\n")

def circle_area(r):         #function to calculate area of r
    return 3.14*r*r         #directly returning the area

r = int(input("Enter Radius: "))
print("The area is : ",circle_area(r))      #displays the area being returned



#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+




#Question 2
print("\n\nQ2.\n")

def perfect(num):
    sums = 0
    for x in range(1,num):      #ruins from 1 to num-1
        if num%x == 0:          #checks for factors in the above range
            sums+=x             #adding factors to sums

    if sums==num:
        print(num,end='  ')     #to keep output in same lin , using end
        
print("Perfect numbers till 1000 are: ",end='')
for num in range(1,1001):       #feeding numbers from 1-1000
    perfect(num)


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+




#Question 3
print("\n\nQ3.\n")
def mult_of12(i=1):         #default parameter , works till you dont give it values
    if i==11:
        return print(" The table above is the answer")
    else:
        print("12 x %d = %d"%(i,12*i))
        i+=1
        mult_of12(i)

mult_of12()     #function call



#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+




#Question 4
print("\n\nQ4.\n")

def pow_of_num(a,b,pow_cal=1):      #function taking base , power and initializing answer
    if b!=0 :                       #till power is not zero
        pow_cal*=a                  #assign 1*base first time , previous*base thereon
        b-=1                        #decrement b
        pow_of_num(a,b,pow_cal)     #pass all values back to cause recursion
        
    else:
        print("Result: ",pow_cal)   
      
a = int(input("Enter base number : "))
b = int(input("Enter its power : "))
pow_of_num(a,b)                             #function call


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+




#Question 5
print("\n\nQ5.\n")

def fact(num):
    if num==0 :
        return 1
    else:
        return num*fact(num-1)
        
a = int(input("Number of inputs?: "))
d = {}

for i in range(0,a):
    num = int(input("Enter number : "))
    d[num] = fact(num)
    
print("Dictionary is: ",d)


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

