
#Question 1
print("\n\nQ1.\n")
a = int(input("Enter year : "))
if a%4==0:
    print("It is a LEAP year")
else:
    print("It is NOT a leap year")
        


#Question 2
print("\n\nQ2.\n")
a = int(input("Enter length : "))
b = int(input("Enter breadth : "))
if a==b :
    print(" It is a square ")
else:
    print("It is a rectangle")




#Question 3
print("\n\nQ3.\n")
a = [int(x) for x in input("Enter ages(space seperated): ").strip().split()]
print("The oldest is: %d and the youngest is %d"%(max(a),min(a)))




#Question 4
print("\n\nQ4.\n")
a = int(input("Enter points scored: "))
if a>200 or a<1 :
    print("INVALID AMOUNT OF POINTS")
    
elif a<51 :
    print(" Sorry , no prize this time ")
    
elif a<151:
    print("Congratulations! You won a Wooden Dog!")

elif a<181:
    print("Congratulations! You won a Book!")

else:
    print("Congratulations! You won Chocolates!")



#Question 5
print("\n\nQ5.\n")
cost = int(input("Enter cost: "))
qty = int(input("Enter quantity : "))
total = qty*cost
if total>1000 :
    print("You're eligible for 10% discount")
    print("Total amount is %d but you only have to pay %.2f"%(total,total*0.9))

else:
    print("Your total would be %d "
          %(total))

print("Have a nice day :)")
