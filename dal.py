import mysql.connector as mysql

def add_user(cur,name,password,email):
	cur.execute(" INSERT INTO user(name,email,password) values(%s,%s,%s) ", (name,email,password) )
	cur.execute(" select last_insert_id()")
	return cur.fetchall()[0][0]

def add_couple(cur,boy,girl,date):
	cur.execute(" INSERT INTO couple(boy,girl,date) values(%s,%s,%s)",(boy,girl,date))
	cur.execute(" select last_insert_id()")
	return cur.fetchall()[0][0]



def password(cur,email):
	cur.execute("SELECT password from user WHERE email=%s",(email,))
	return cur.fetchall()[0][0]

