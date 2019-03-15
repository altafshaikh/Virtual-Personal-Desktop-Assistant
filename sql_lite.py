import sqlite3

class Connection():
	
	#create database if not exixts
	def connect(self):
		conn = sqlite3.connect('sqlite.db')
		if conn:
			print("Opened database successfully")
			return conn
		else:
			print("Error in opening the Database"+conn)


	#create table
	def create_table(self,conn):
		conn.execute('''CREATE TABLE if not exists PATHS
				 (ID INT PRIMARY KEY  NOT NULL,
				 COMMAND        TEXT    NOT NULL,
				 AUDIO_PATH     TEXT     NOT NULL
				 );''')
	
		print("Table Pass")
		return True
		
	#insert values into tabels
	def insert(self,cmd,path,conn):
		query = "INSERT INTO PATHS (COMMAND,AUDIO_PATH) \
			VALUES 1,%s,%s" % (cmd,path)
		
		conn.execute(query)	
		conn.commit()
		print("Records Inserted successfully")
		


	def select(self,cmd,conn):
		query = "SELECT ID, COMMAND, AUDIO_PATH from PATHS where COMMAND = '%s'" % (cmd)
		print(query)
		cursor = conn.execute()
		print(cursor)
		path=[]
		if cursor :
			for row in cursor:
				print("ID = ", row[0])
				print("Command = ", row[1])
				print("Audio PAth = ", row[2], "\n")
			path = row[2]
			print("Operation done successfully")
			return path[0]
		else:
			return path

	def update(self,conn):
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

	def delete(self,conn):
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

	def drop(self,conn):
		dropTableStatement = "DROP TABLE COMPANY"

		conn.execute(dropTableStatement)
		print("Drop table successfully")

	def close(self,conn):
		conn.close()

	#create_table()
	#insert()
	#select()
	#update()
	#delete()
	#drop()

