import sqlite3
			
#create table
def create_table():
	conn = sqlite3.connect('sqlite.db')
	conn.execute('''CREATE TABLE if NOT EXISTS PATHS
                        (ID INT PRIMARY KEY  NOT NULL,
			 RESPONSE        TEXT    NOT NULL,
			 AUDIO_PATH     TEXT     NOT NULL
			 );''')
	
	print("Table created")
	conn.commit()
	conn.close()
	return True

		
#insert values into tabels
def insert(cmd,path):
    conn = sqlite3.connect('sqlite.db')
    sql = "INSERT INTO PATHS(ID,RESPONSE,AUDIO_PATH) VALUES(?,?,?)"
    cur = conn.cursor()
    for row in cur.execute("SELECT MAX(ID) FROM PATHS"):
        if row[0] is None:
            n=0
        else:
            n=int(row[0])
    project=(str(n+1),cmd,path);
    cur.execute(sql, project)
    print("Records Inserted successfully")
    conn.commit()
    conn.close()

def select(cmd):
	conn = sqlite3.connect('sqlite.db')
	query = "SELECT ID, RESPONSE, AUDIO_PATH FROM PATHS WHERE RESPONSE= ? "
	cur = conn.cursor()
	cur.execute(query,(cmd,))
	rows=cur.fetchall()
	if rows==[]:
		print("Is not available in table")
	else:
		print("Is available in table")

create_table()
insert(r'hey3',r'C:\Users\pratiksha shetty\Desktop\Jarvis-artificial-intelligence-master\response\no hey3.mp3')
select("hey")