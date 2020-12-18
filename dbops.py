import sqlite3

def insert_into_tasks_table(task):
	sql_insert_query="""
	INSERT INTO todolist(taskname,complete) VALUES('%s',%s)
	"""% (task,0)
	execute_query(sql_insert_query)

def select_statement():
	sql_select_query="""
	SELECT taskname FROM todolist WHERE complete=0 """
	result=execute_query(sql_select_query).fetchall()
	results=[]
	for i in result:
		results.append(i[0])
	return results
	
def update_task(old_task, new_task):
	sql_update="""UPDATE todolist  SET taskname='%s'WHERE taskname='%s'""" %(new_task,old_task)
	res = execute_query(sql_update).fetchall()

	

def mark_task_as_complete(task):
	sql_update_query="""UPDATE todolist SET complete= 1 WHERE taskname='%s' AND complete=0 """% (task)
	execute_query(sql_update_query) 

def execute_query(sql_query):
	with sqlite3.connect("todo") as conn:
		cur= conn.cursor()
		result = cur.execute(sql_query)
		conn.commit()
	return result

