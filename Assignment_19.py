import numpy as np

#Question 1
print("\n\nQ1.\n")

a = np.random.rand(10,1)

print(a)
print(a.shape)

print("Mean : ",np.mean(a))


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


#Question 2
print("\n\nQ2.\n")

a = np.random.rand(20,1)

print(a)
print(a.shape)

print("Standard Deviation: ",np.std(a))

print("Variance : ",np.var(a))

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


#Question 3
print("\n\nQ3.\n")

A = np.random.rand(10,20)
print(A)
print(A.shape)

B = np.random.rand(20,25)
print(B)
print(B.shape)

ans = np.dot(A,B)

print("\nDot product of A and B: \n",ans)

print("\n Sum of the new matrix : ", np.sum(ans))

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


#Question 4
print("\n\nQ4.\n")

A = np.random.rand(10,1)

def change(x):
    return 1 / (1 + np.exp(-x)) 

print(A)
print(A.shape)

updated = change(A) 

print("\nAfter updation: \n",updated)

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

