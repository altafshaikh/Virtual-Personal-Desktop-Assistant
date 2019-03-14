import sqlite3

def connection():
	#create database if not exixts
	conn = sqlite3.connect('sqlite.db')

	print("Opened database successfully")

#create table
def crete_table():
	conn.execute('''CREATE TABLE COMPANY
			 (ID INT PRIMARY KEY     NOT NULL,
			 NAME           TEXT    NOT NULL,
			 AGE            INT     NOT NULL,
			 ADDRESS        CHAR(50),
			 SALARY         REAL);''')

	print("Table created successfully")

#insert values into tabels
def insert():
	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
		VALUES (1, 'Paul', 32, 'California', 20000.00 )")

	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
		VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
		VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
		VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

	conn.commit()
	print("Records created successfully")

def select():
	cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
	if cursor:
		print("Hello")
	for row in cursor:
		print("ID = ", row[0])
		print("NAME = ", row[1])
		print("ADDRESS = ", row[2])
		print("SALARY = ", row[3], "\n")

	print("Operation done successfully")

def update():
	conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
	conn.commit
	print("Total number of rows updated :", conn.total_changes)

	cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
	for row in cursor:
   		print("ID = ", row[0])
   		print("NAME = ", row[1])
   		print("ADDRESS = ", row[2])
   		print("SALARY = ", row[3], "\n")

	print("Operation done successfully")

def delete():
	#conn.execute("DELETE from COMPANY where ID = 2;")
	conn.execute("DELETE from COMPANY")
	conn.commit()
	print("Total number of rows deleted :", conn.total_changes)

	cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
	for row in cursor:
   		print("ID = ", row[0])
   		print("NAME = ", row[1])
   		print("ADDRESS = ", row[2])
   		print("SALARY = ", row[3], "\n")

	print("Operation done successfully")

def drop():
	dropTableStatement = "DROP TABLE COMPANY"

	conn.execute(dropTableStatement)
	print("Drop table successfully")

#crete_table()
#insert()
#select()
#update()
#delete()
#drop()

conn.close()