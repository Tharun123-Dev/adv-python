
#pdbc connection
import mysql.connector
conn= {
  'user':'root',
  'password':'Nani@123',
  'host':'localhost',
  'port':'3306'
}
try:
  mysql.connector.connect(**conn)
  print('connection successful')
except:
  print("not able to connect")

cursor = conn.cursor()
cursor.execute("sql server")

cursor.close()
conn.close()