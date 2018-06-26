import MySQLdb

#Question 1
print("\n\nQ1.\n")

db = MySQLdb.connect("localhost","testuser","test123","TESTDB")

cursor = db.cursor()

sql = """CREATE TABLE BOOKS(
         BOOK_ID INT PK,
         TITLE_ID INT PK,
         LOCATION VARCHAR(30),
         GENRE VARCHAR(20))"""

cursor.execute(sql)

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


db.close()
     

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


#Question 2
print("\n\nQ2.\n")

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


#Question 3
print("\n\nQ3.\n")

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

