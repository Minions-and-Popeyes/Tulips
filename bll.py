import mysql.connector as mysql
import dal
import datetime

def getSQLConnection():
	return mysql.connect(user='tulips',password='GottLoveFee',host='localhost',database='Tulips')


def signup(boy_name,boy_address,boy_password,girl_name,girl_address,girl_password):
	conn = getSQLConnection();
	cur = conn.cursor()
	boy = dal.add_user(cur,boy_name,boy_password,boy_address)
	girl = dal.add_user(cur,girl_name,girl_password,girl_address)
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

def add_lovebookitem(person_email,content):
	conn = getSQLConnection()
	cur = conn.cursor()
	uid = dal.user_id_email(person_email)
	dal.add_lovebookitem(content,datetime.datetime.now(),uid)
	conn.commit()

