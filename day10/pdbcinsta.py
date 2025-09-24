import mysql.connector
#connection
try:
 conn=mysql.connector.connect(
    user='root',
    host='localhost',
    password='Nani@123',
    port=3306
)
 print("connection successfully")
except:
 print("something went wrong")

cursor=conn.cursor()
#create table
query='create database if not exists insta'
cursor.execute(query)

cursor.execute('use insta')
#columns
table="""create table if not exists instagram (
user_number int auto_increment primary key,user_id int unique,password varchar(100),email varchar(100),no_of_posts int,no_of_likes int,no_of_comments int
)"""

cursor.execute(table)
# #add column
# column='alter table instagram add name varchar(100) after user_number'
# column='alter table instagram add followers int after user_id'
# cursor.execute(column)

# #insering values
# try:
#  data=[("nani",123,'nani@123','nani@gmail.com',10,1000,100),
#       ("shannu",1234,'shannu@123','shannu@gmail.com',100,10000,50),
#       ("tharun",121,'tharun@123','@gmatharunil.com',60,6000,20),
#       ("naveen",11223,'naveen@123','naveen@gmail.com',1,5,6),
#        ("sathi",12390,'sathi@123','sathi@gmail.com',1000,1000,1000),
#        ("shanmukh",246,'shanmukh@123','shanmukh@gmail.com',56,1600,180),
#        ("prash",12315,'prash@123','prash@gmail.com',52,6565,2626)]
#  insert="""insert into instagram (name,user_id,password,email,no_of_posts,no_of_likes,no_of_comments) values (%s,%s,%s,%s,%s,%s,%s)"""
#  cursor.executemany(insert,data)
#  print("inserting")
# except:
#  print("not inserting")


# #update name by id
# def updatename(new_name,email):
#   try:
#    query="""update instagram set name=%s where email=%s"""
#    cursor.execute(query,(new_name,email))
   
 
#   except:
#    print("not updated")
# updatename("shannuu","shannu@gmail.com")

# #update 2 records
# def likespostsbyid(new_likes,new_posts,user_id):
#    try:
#      query="""update instagram set no_of_posts=%s,no_of_likes=%s where user_id=%s"""
#      cursor.execute(query,(new_posts,new_likes,user_id))
#      conn.commit()
#      print("update done")
#    except:
#      print('not updated')
# likespostsbyid(200,300,"121")

#getrecods
# query="""select * from instagram where name='shannuu' """
# cursor.execute(query)
# result=cursor.fetchall()
# print(result)


# #insering new column and new values for that
# query="""insert into instagram (followers) values (110),(230),(560),(600)"""
# cursor.execute(query)

# #delete of this by followers
# def deletedfollowers(followers):
#  try:
#   query="""delete from instagram where followers=%s"""
#   cursor.execute(query,(followers,))
#  except:
#   print("not deleted")
# deletedfollowers(560)
#1
#inserting sinlgle column row values
# query="""update instagram set followers=300 where name='shannuu' """

# cursor.execute(query)
#2
# query="""update instagram set followers=500 where name='naveen' """

# cursor.execute(query)
#3
# query="""update instagram set followers=10000 where name='prash' """

# cursor.execute(query)
# #5
# query="""update instagram set followers=3000 where name='sathi' """

# cursor.execute(query)
  
# #modify column name

# try:
#   query="""alter table instagram rename column no_of_likes to likes"""
#   cursor.execute(query)
# except:
#    print("not modified")

# #rename table name
# try:
#  query=""" alter table instagram rename to if instagramm"""
#  cursor.execute(query)
# # except Exception as e:
# #     print("not modified",e) 
# except mysql.connector.errors.ProgrammingError as e:
#    print("not update",e)





conn.commit()
cursor.close()
conn.close()



