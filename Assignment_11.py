import _thread
import time

#Question 1

print("\n\nQ1.\n")
def print_msg( threadName):         #takes thread name as a parameter
    time.sleep(5)                   #lets the thread sleep for 5 seconds
    print ("%s displays 'hello world'" % ( threadName ))

try:
   _thread.start_new_thread( print_msg, ("Thread-1",) )# creates a thread Thread-1 and passes it to funtion print_msg

except:
   print ("Error: unable to start thread")

time.sleep(7)   #sleeping for 7 seconds until tthe next thread executes6


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+



#Question 2
print("\n\nQ2.\n")
def count_10( threadName, delay):   #takes in thread name and delay
   count = 0
   while count < 10:        #counts till 9
      time.sleep(delay)     #delay of 1 sec in between
      count += 1            #increments till 10
      print ("%d" % (count) )
try:
   _thread.start_new_thread( count_10, ("Thread-1", 1 ) )# creates a thread Thread-1 and 1 which is passed to funtion count_10
except:
   print ("Error: unable to start thread")

time.sleep(12)      # again putting on sleep until the next thread arrives



#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+





#Question 3
print("\n\nQ3.\n")
list_a = [4,6,7,11,9]

def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      print ("%s : %d" % (threadName,list_a[count]) )       #displayes thraed name and the lists items
      count += 1
      
try:
   _thread.start_new_thread( print_time, ("The list items are", 2 ) )   # passes the string name and the delay values
   
except:
   print ("Error: unable to start thread")

time.sleep(22)  #sleeping till this thread ends


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+



#Question 4
print("\n\nQ4.\n")

def fact( threadName, num):         #funtion taking thread name and num as parameters
   fact = 1
   while num!=0:                    #logic for facotrial
      time.sleep(1)
      fact *= num
      num-=1
      print ("%s  %d" % (threadName,fact) )     #printing the calculated values hand to hand

      
try:
   _thread.start_new_thread( fact, ("Calculating...", 5 ) )     #passing thraed name and number of which factoiral i to be calculated
   
except:
   print ("Error: unable to start thread")


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


