import _thread
import time

#Question 1

print("\n\nQ1.\n")
# Define a function for the thread
def print_msg( threadName):
    time.sleep(5)
    print ("%s displays 'hello world'" % ( threadName ))

# Create two threads as follows
try:
   _thread.start_new_thread( print_msg, ("Thread-1",) )

except:
   print ("Error: unable to start thread")

while 1:
   pass



#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+



#Question 2
print("\n\nQ2.\n")
def print_time( threadName, delay):
   count = 0
   while count < 10:
      time.sleep(delay)
      count += 1
      print ("%d" % (count) )
# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 1 ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass





#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+





#Question 3
print("\n\nQ3.\n")
list_a = [4,6,7,11,9]

def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      print ("%s : %d" % (threadName,list_a[count]) )
      count += 1
# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("The list items are", 2 ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass



#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+



#Question 4
print("\n\nQ4.\n")

def fact( threadName, num):
   fact = 1
   while num!=0:
      time.sleep(1)
      fact *= num
      num-=1
      print ("%s  %d" % (threadName,fact) )

      
try:
   _thread.start_new_thread( fact, ("Calculating...", 5 ) )
   
except:
   print ("Error: unable to start thread")

while 1:
   pass

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


