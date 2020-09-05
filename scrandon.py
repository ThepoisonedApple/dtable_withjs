import mysql.connector
import random
import string

def get_random_string(length):
	letters = string.ascii_lowercase
	result_str = ''.join(random.choice(letters) for i in range(length))
	return result_str

mydb = mysql.connector.connect(
			host='localhost',
			user='root',
			passwd='',
			database='ssltrydb'
)
mydb.connect()
mycursor=mydb.cursor()
for i in range(0,500):
	sql="INSERT INTO denemetablo (rand_int,rand_str) VALUES (%s,%s)"
	val=(random.randint(0,100000),get_random_string(8))
	mycursor.execute(sql,val)
	mydb.commit()