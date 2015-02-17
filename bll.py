import mysql.connector as mysql
import dal
import datetime

def getSQLConnection():
	return mysql.connect(user='tulips',password='GottLoveFee',host='localhost',database='Tulips')

def signup(boy_name,boy_address,boy_password,girl_name,girl_address,girl_password):
	conn = getSQLConnection()
	cur = conn.cursor()
	boy = dal.add_user(cur,boy_name,boy_password,boy_address,1)
	girl = dal.add_user(cur,girl_name,girl_password,girl_address,0)
	dal.add_couple(cur,boy,girl,datetime.datetime.now())
	conn.commit()


def login(person_email,person_password):
	conn = getSQLConnection()
	cur = conn.cursor()
	print repr(person_password),"====",repr(str(dal.password(cur,person_email).decode('utf-8')))
	if str(person_password)==str(dal.password(cur,person_email).decode('utf-8')):
		return True
	else: 
		return False



def lovebook(person1_email,year,month,day):
	conn = getSQLConnection()
	cur = conn.cursor()
	id1=dal.person_id(cur,person1_email)
	gender1=dal.person_gender(cur,person1_email)
	couple_id=dal.couple(cur,id1,gender1)
	id2=dal.peer(cur,gender1,couple_id)
	begin_time = datetime.datetime(year,month,day,0,0,0)
	stop_time = datetime.datetime(year,month,day,23,59,59)
	return dal.lovebook_items(cur,id1,id2,begin_time,stop_time)


def new_lovebook(new_content,email):
	conn = getSQLConnection()
	cur = conn.cursor()
	user_id = dal.person_id(cur,email)
	change_time = datetime.datetime.now()
	dal.add_lovebook_items(cur,new_content,change_time,user_id)
	conn.commit()


def be_together_date(person1_email):
	conn = getSQLConnection()
	cur = conn.cursor()
	id1=dal.person_id(cur,person1_email)
	gender1=dal.person_gender(cur,person1_email)
	date=dal.couple_date(cur,id1,gender1)
	return date



