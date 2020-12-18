import sqlite3

def create_table():
	sql_query="""
	CREATE TABLE todolist(
	id INTEGER PRIMARY KEY,
	taskname TEXT,
	complete BOOLEAN);
	"""
	with sqlite3.connect("todo") as conn:
		cur= conn.cursor()
		cur.execute(sql_query)
		conn.commit()

if __name__ == '__main__':
	create_table()
