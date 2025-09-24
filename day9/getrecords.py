
# import mysql.connector
# from getrecords import getLimitedRecords

# ##connection purpose
# try:
#     #we want to mentioned separate variable
#     conn= mysql.connector.connect(
#         user="root",
#         password="Nani@123",
#         host="localhost",
#         port=3306
#     )
#     print("connection Succesfully")
# except:
#     print("not able to connect")
# #it will helps to execute the sql queries in python
# cursor=conn.cursor()

# # #fetch limited record
# def getLimitedRecords(limit):
#    try:
#       cursor.execute('use pdbcsql')
#       query="""select * from students limit %s"""
#       cursor.execute(query,(limit,))
#       result=cursor.fetchall()

#     #   print(result)
#       for i in result:
#          print(i)
#    except:
#       print("something went wrong")
#    finally:
#       print("task completed")
# getLimitedRecords(int(input("enter a number: ")))



# #we want to commit and close of conn
# conn.commit()
# cursor.close()
# conn.close()



import mysql.connector

## Connection
try:
    conn = mysql.connector.connect(
        user="root",
        password="Nani@123",
        host="localhost",
        port=3306,
        database="pdbcsql"  # you can directly connect to the database
    )
    print("Connection successful")
except mysql.connector.Error as e:
    print("Not able to connect:", e)
    exit()  # stop execution if connection fails

# Cursor to execute queries
cursor = conn.cursor()

# Fetch limited records
def getLimitedRecords(limit):
    try:
        query = "SELECT * FROM students LIMIT %s"
        cursor.execute(query, (limit,))
        result = cursor.fetchall()
        
        for row in result:
            print(row)
    except mysql.connector.Error as e:
        print("Something went wrong:", e)
    finally:
        print("Task completed")

# Call function
getLimitedRecords(int(input("Enter a number: ")))

# Commit (if needed) and close connection
conn.commit()
cursor.close()
conn.close()

