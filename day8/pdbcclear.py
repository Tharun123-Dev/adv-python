import mysql.connector

##connection purpose
try:
    #we want to mentioned separate variable
    conn= mysql.connector.connect(
        user="root",
        password="Nani@123",
        host="localhost",
        port=3306
    )
    print("connection Succesfully")
except:
    print("not able to connect")
#it will helps to execute the sql queries in python
cursor=conn.cursor()

#first of all we want to create database/schema >>if once run created then again want error so use if not exist
query='CREATE DATABASE if not exists 10000coderr'
cursor.execute(query)
#using the databases
cursor.execute('use 10000coders')

#create a table
# try:
#  create_table="""create table if not exists students(
#  id INT AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(100),EMAIL(100),COURSE VARCHAR(100),JOINED_DATE DATE
#  )"""
#  #execute the table
#  cursor.execute(create_table)
# except:
#    print("something went wrong")

#creating a table with error if exists

try:
 create_table="""create table if not exists students(
 id INT AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(100),EMAIL varchar(100),COURSE VARCHAR(100),JOINED_DATE DATE
 )"""
 #execute the table
 cursor.execute(create_table)
 print("connection succesfully for table created")
except mysql.connector.errors.ProgrammingError as e:
   print(e)

# #inserting data into a table
# try:
#    insertdata="""insert into students values (1,'tharun','tharun@gmail.com,'PFS','2025-06-03')"""
#    cursor.execute(insertdata)
# except:
#    print("somthing went wrong")

#inserting multiple rows of data


# try:
   data=(1,'harish','harish@gmail.com','PFS','2025-02-06')
   inserdata="""insert into students (name,email,course,joined_date) values(%s,%s,%s,%s)"""
   cursor.execute(inserdata,data)
# except:
#    print("something went wrong")



#we want to commit and close of conn
conn.commit()
cursor.close()
conn.close()