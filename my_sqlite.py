import sqlite3
			
	#create table
def create_table():
	conn = sqlite3.connect('sqlite.db')
	conn.execute('''CREATE TABLE if NOT EXISTS PATHS
			 (ID INT PRIMARY KEY  NOT NULL,
			 COMMAND        TEXT    NOT NULL,
			 AUDIO_PATH     TEXT     NOT NULL
			 );''')
	
	print("Table created")
	conn.commit()
	conn.close()
	return True
		
#insert values into tabels
def insert(cmd,path):
	conn = sqlite3.connect('sqlite.db')
	
	
	conn.execute("INSERT INTO PATHS (ID,COMMAND,AUDIO_PATH) \
		VALUES (%s,%s,%s)" % (1,cmd,path))	
	
	print("Records Inserted successfully")
	conn.commit()
	conn.close()
	return True


def select(cmd):
	conn = sqlite3.connect('sqlite.db')
	query = "SELECT ID, COMMAND, AUDIO_PATH from PATHS"
	cursor = conn.execute(query)
	print(cursor)
	path=[]
	if cursor :
		print("cursor")
		for row in cursor:
			print(row)
			if row[1]==cmd:
				print("ID = ", row[0])
				print("Command = ", row[1])
				print("Audio PAth = ", row[2], "\n")
				break;
		path = row[2]
		print("Operation done successfully")
		conn.commit()
		conn.close()
		return path[0]
	else:
		conn.commit()
		conn.close()
		return path

def update():
	conn = sqlite3.connect('sqlite.db')
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
	conn.commit()
	conn.close()

def delete():
	conn = sqlite3.connect('sqlite.db')
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
	conn.commit()
	conn.close()

def drop():
	conn = sqlite3.connect('sqlite.db')
	dropTableStatement = "DROP TABLE COMPANY"

	conn.execute(dropTableStatement)
	print("Drop table successfully")
	conn.commit()
	conn.close()

create_table()
insert("hello","/root/Desktop/Jarvis/audio")