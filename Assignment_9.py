
#Question 1
print("\n\nQ1.\n")

class circle:
    def __init__(self,r):
        self.r = r
        
    def GetArea(self):
        print("Area of the circle is : %.2f"%(3.14 * self.r * self.r))

    def GetCircumference(self):
        print("Circumference of the circle is : %.2f"%(3.14 * self.r * 2))


c = circle(10)
c.GetArea()
c.GetCircumference()


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

#Question 2
print("\n\nQ2.\n")

class Student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        
    def Display(self):
        print("\nName is : %s and roll number is: %d"%(self.name,self.roll_no))


a = Student("Acad",10)
b = Student("Veiw ",33)
c = Student("Assignment ",666)
a.Display()
b.Display()
c.Display()


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

#Question 3
print("\n\nQ3.\n")

class Temperature:
    def __init__(self,temp):
        self.temp = temp
        print("\nTemperature  = ",temp)
        
    def convertFahrenheit(self):
        print(self.temp,"Celcius is equal to ",(1.8*self.temp)+32,"F")
        
    def convertCelsius(self):
        print(self.temp,"Fahrenheit is equal to ",(self.temp-32)/1.8,"C")

a = Temperature(32)
a.convertFahrenheit()
a.convertCelsius()

b = Temperature(-40)
b.convertFahrenheit()
b.convertCelsius()

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


#Question 4
print("\n\nQ4.\n")

class MovieDetails:
    def __init__(self,name,artistname,year,ratings):
        self.name = name
        self.artistname = artistname
        self.year = year
        self.ratings = ratings
        
    def Display(self):
        print("Movie Name: %s\nArtists: %s\nYear: %d\nRating: %.1f"%(self.name,self.artistname,self.year,self.ratings))
        
    def Update(self,name,artistname,year,ratings):
        self.name = name
        self.artistname = artistname
        self.year = year
        self.ratings = ratings
        print("\n\nAfter Updating: ")
        self.Display()

movie = MovieDetails("FREE TO PLAY","DENDI",2014,8.3)
movie.Display()
movie.Update("FREE TO PLAY","DENDI and MIRACLE",2014,9)

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

#Question 5
print("\n\nQ5.\n")

class Expenditure:
    def __init__(self,expend,savings):
        self.expend = expend
        self.savings = savings
        
    def Display(self):
        print("\nExpenditure is : %d and savings are: %d"%(self.expend,self.savings))

    def cal_sal(self):
        self.salary = self.expend + self.savings

    def Salary(self):
        print("Salary is :",self.salary)

person = Expenditure(20000,34567)
person.Display()
person.cal_sal()
person.Salary()

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


