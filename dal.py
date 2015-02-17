import mysql.connector as mysql

def add_user(cur,name,password,email,gender):
	cur.execute(" INSERT INTO user(name,email,password,gender) values(%s,%s,%s,%s) ", (name,email,password,gender) )
	cur.execute(" select last_insert_id()")
	return cur.fetchall()[0][0]

def add_couple(cur,boy,girl,date):
	cur.execute(" INSERT INTO couple(boy,girl,date) values(%s,%s,%s)",(boy,girl,date))
	cur.execute(" select last_insert_id()")
	return cur.fetchall()[0][0]



def password(cur,email):
	cur.execute("SELECT password from user WHERE email=%s",(email,))
	return cur.fetchall()[0][0]


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
	cur.execute("SELECT * from lovebook WHERE (user=%s or user=%s) and time>=%s and time<=%s  ORDER BY time desc",(id1,id2,begin_time,stop_time))
	return cur.fetchall()


def add_lovebook_items(cur,new_content,change_time,user_id):
	cur.execute("INSERT INTO lovebook(content,time,user) values(%s,%s,%s)",(new_content,change_time,user_id))
	cur.execute("SELECT last_insert_id()")
	return cur.fetchall()[0][0]



def inbox(cur,user_id,timenow):
	cur.execute("SELECT begin_time,end_time,content,is_read from letters WHERE (to=%s) and %s >= begin_time and %s <= end_time ORDER BY id desc",(user_id,timenow,timenow))
	return cur.fetchall()


def letters_is_read(cur,letters_id):
	cur.execute("UPDATE letters SET is_read=1,read_time=%s WHERE id=%s",(letters_id,datetime.datetime.now()))




def outbox(cur,user_id):
	cur.execute("SELECT * from letters WHERE (from=%s) ORDER BY id desc",(user_id,))
	return cur.fetchall()


def letters_write(cur,user_id,begin_time,end_time,content):
	cur.execute("INSERT INTO letters(begin_time,end_time,content,is_read,modified_time) values(%s,%s,%s,%s,%s)",())






