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
query='CREATE DATABASE if not exists practiceall'
cursor.execute(query)
#using the databases
cursor.execute('use practice')

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



# #inserting sinle single cganges rows of data

# try:
#    data=('suresh','sureshsh@gmail.com','PFS','2025-02-06')
#    insertdata="""insert into students (name,email,course,joined_date) values(%s,%s,%s,%s)"""
#    cursor.execute(insertdata,data)
#    print("inserted")
# except:
#   print("something went wrong")


# #insert multiple rows at a time
# try:
#    data=[("shannu",'shannu@gmail.com','PFS',"2025-05-06"),
#          ('Tharun','tharun@gmail.com',"PFS",'2025-05-06'),
#          ('sharanya','sharanya2gmail.com','PFS',"2025-05-06")]
#    insertquery="""insert into students (name,email,course,joined_date) values (%s,%s,%s,%s)"""
#    cursor.executemany(insertquery,data)
# except:
#    print("something went wrong")


#using functions given of this

# def insertSingleRow(data):
#   try:

#      insertquery="""insert into students (name,email,course,joined_date) values (%s,%s,%s,%s)"""
#      cursor.executemany(insertquery,data)
#   except:
#    print("something went wrong")
# insertSingleRow([("shanmukh",'shanmukh@gmail.com','PFS',"2025-05-06"),
#          ('Tharunn','tharunn@gmail.com',"PFS",'2025-05-06'),
#          ('saranya','saranya2gmail.com','PFS',"2025-05-06")])


# # #getting all records from table
# def getrecords():
#    try:
#       query='select * from students'
#       cursor.execute(query)
#       result=cursor.fetchall()
#       print(result)
#    except:
#       print("error occurred")
# getrecords()  

# #getting all records from one by one using for loop

# def getrecords():
#    try:
#       query='select * from students'
#       cursor.execute(query)
#       result=cursor.fetchall()
#       for i in result:
#          print(i)
#    except:
#       print("error occurred")
# getrecords()

# #using where condition and get records

# def getstudentsByCourse(course_name):
#    try:
#       query="select * from students where course= %s "
#       cursor.execute(query,(course_name,))
#       result=cursor.fetchall()
#     #   print(result)
#       for i in result:
#          print(i)
#    except:
#       print("something went wrong")
# getstudentsByCourse("DS")
      
#update record with new email
def Update(email):
   try:
      line=" update students set email=%s where email='harish@gmail.com'"
      cursor.execute(line,(email,))
      result=cursor.fetchall()
      for x in result:
         print(x)
   except:
      print("not updated")
Update("shannu@gmail.com")

#delete record  by email
# def delete(email):
#    try:
#       line="delete from students where email=%s"
#       cursor.execute(line,(email,))
#       result=cursor.fetchall()
#       for x in result:
#          print(x)
#    except:
#       print("not deleted")
# delete("shannu@gmail.com")


# #delete multiple records by course
# def delete(course):
#    try:
#       line="delete from students where course=%s"
#       cursor.execute(line,(course,))
#       result=cursor.fetchall()
#       for x in result:
#          print(x)
#    except:
#       print("not deleted")
# delete("DS")



#we want to commit and close of conn
conn.commit()
cursor.close()
conn.close()