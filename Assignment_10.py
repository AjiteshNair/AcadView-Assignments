
#Question 1
print("\n\nQ1.\n")
class animal():
    def animal_attribute(self,leg):
        self.leg=leg
        print(leg)

class tiger(animal):
    def __init__(self):
        print("object of tiger made!!")

obj=tiger()
obj.animal_attribute(4)  #base class method is called using the child class object

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


#Question 2
print("\n\nQ2.\n")
class A:
    def f(self):
        return self.g()
    def g(self):
        return 'A'
    
class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(),b.f())
#when a.f is encountered , only class a is involved , so only mthod g for classs A will be accessed
#when b.f is called , parnt method is called via the child , so when method f of parent class invokes g , prefece te the g method of class B is given

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


#Question 3
print("\n\nQ3.\n")

class Cop():
    def add(self):
        name=input(("enter name:"))
        self.name=name
        age=input("enter the age:")
        self.age=age
        work=input("enter the work:")
        self.work=work
        exper=input("enter the experience:")
        self.exper=exper
         
    def display(self):
        print("name:%s\nage:%s\nwork:%s\nexperience:%s"%(self.name,self.age,self.work,self.exper))
    
    def update(self):
        name=input(("enter new name:"))
        self.name=name
        age=input("enter the new age:")
        self.age=age
        work=input("enter the new work:")
        self.work=work
        exper=input("enter the new experience:")
        self.exper=exper

class Mission(Cop):
    mission=""
    def add_mission_details(self):
        self.mission=input("Enter the mission name:")
obj=Mission()
obj.add()
obj.display()
n=input("do you want to update?:(Y?N)")
if(n=="y" or n=="Y"):
    obj.update()



#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


#Question 4
print("\n\nQ4.\n")
class Shape():
    def __init__(self,leng,bre):
        self.leng=leng
        self.bre=bre
    def area(self):
        return (self.leng)*(self.bre)
    
class rectangle(Shape):
    def __init__(self,leng,bre):
        self.leng=leng
        self.bre=bre

class square(Shape):
    def __init__(self,leng,bre):
        self.leng=leng
        self.bre=bre

obj1=rectangle(2,3)
print("area of rec:",obj1.area())

obj2=square(5,5)
print("area of square:",obj2.area())

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
