import MySQLdb

#Question 1
print("\n\nQ1.\n")

db = MySQLdb.connect("localhost","testuser","test123","TESTDB")#opening database to work on

cursor = db.cursor()        #preparing object for cursor method

sql = """CREATE TABLE BOOKS(
         BOOK_ID INT PK,
         TITLE_ID INT PK,
         LOCATION VARCHAR(30),
         GENRE VARCHAR(20))"""

cursor.execute(sql)         #executing the sql command

sql = """CREATE TABLE TITLES(
         TITLE VARCHAR(20),
         TITLE_ID INT PK,
         ISBN VARCHAR(30),
         PUBLISHER_ID INT PK,
         PUBLICATION_YEAR NUMBER(4))"""

cursor.execute(sql)

sql = """CREATE TABLE PUBLISHERS(
         PUBLISHER_ID INT PK,
         NAME VARCHAR(20),
         STREET_ADDR VARCHAR(20),
         SUITE_NO INT PK,
         ZIP_CODE INT )"""

cursor.execute(sql)

sql = """CREATE TABLE ZIPCODES(
         ZIP_CODE INT ,
         CITY VARCHAR(20),
         STATE VARCHAR(20))"""

cursor.execute(sql)

sql = """CREATE TABLE AUTHOR(
         AUTHOR_ID INT PK,
         FIRST_NAME VARCHAR(20),
         MIDDLE_NAME VARCAHR(20),
         LAST_NAME VARCHAR(20))"""

cursor.execute(sql)


db.close()      #properly exiting the database
     

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


#Question 2
print("\n\nQ2.\n")

db = MySQLdb.connect("localhost","testuser","test123","TESTDB")

cursor = db.cursor()

sql = """ INSERT INTO BOOKS VALUES(1,101,"UNITED KINGDOM","THRILLER")"""

try:
    cursor.execute(sql)     #if insertion fails to occur
    db.commit()
except:
    db.rollback()       #if error occurs , rollback to safe point

#Same way to enter values in other tables as well

db.close()

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


#Question 3
print("\n\nQ3.\n")

db = MySQLdb.connect("localhost","testuser","test123","TESTDB")

cursor = db.cursor()

sql = """UPDATE BOOKS SET LOCATION = "AMERICA"
                                 WHERE BOOK_ID = 1"""

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

