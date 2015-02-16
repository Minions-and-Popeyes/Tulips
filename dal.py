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

<<<<<<< HEAD

def person_id(cur,email):
	cur.execute("SELECT id from user WHERE email=%s",(email,))
	return cur.fetchall()[0][0]


def person_gender(cur,email):
	cur.execute("SELECT gender from user WHERE email=%s",(email,))
	return cur.fetchall()[0][0]


def couple(cur,person_id,person_gender):
    if person_gender==1:
    	cur.execute("SELECT id from couple WHERE boy=%s",(person_id,))
    else:
		cur.execute("SELECT id from couple WHERE girl=%s",(person_id,))

	return cur.fetchall()[0][0]



def couple_date(cur,person_id,person_gender):
	if person_gender==1:
		cur.execute("SELECT date from couple WHERE boy=%s",(person_id,))
	else:
		cur.execute("SELECT date from couple WHERE girl=%s",(person_id,))

	return cur.fetchall()[0][0]



def peer(cur,person_gender,couple_id):
	if person_gender==1:
		cur.execute("SELECT girl from couple WHERE id=%s",(couple_id,))
	else:
		cur.execute("SELECT boy from couple WHERE id=%s",(couple_id,))

	return cur.fetchall()[0][0]


def lovebook_items(cur,id1,id2,begin_time,stop_time):
	cur.execute("SELECT * from lovebook WHERE (user=%s or user=%s) and time>=begin_time and date<=stop_time  ORDER BY date desc",(id1,id2))
	return cur.fetchall()





=======
def user_id_email(cur,email):
	cur.execute("SELECT id from user WHERE email=%s",(email,))
	return cur.fetchall()[0][0]

def add_lovebookitem(cur,content,date,uid):
	cur.execute('INSERT INTO lovebook(content,date,user) values(%s,%s,%s)',(content,date,uid))
	cur.execute('select last_insert_id()')
	return cur.fetchall[0][0]
>>>>>>> FETCH_HEAD
