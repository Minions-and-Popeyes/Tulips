import mysql.connector as mysql
import dal
import datetime
from Models.Entities.user import user
from Models.Entities.couple import couple


def getSQLConnection():
	return mysql.connect(user='tulips',password='GottLoveFee',host='162.105.80.126',database='Tulips')

def signup(boy_name,boy_address,boy_password,girl_name,girl_address,girl_password):
	conn = getSQLConnection()
	cur = conn.cursor()
	boy = user(None,boy_name,boy_address,boy_password,1)
	boy.save(cur)
	girl = user(None,girl_name,girl_address,girl_password,0)
	girl.save(cur)
	c = couple(None, boy.id ,girl.id,datetime.datetime.now())
	c.save(cur)
	conn.commit()


def login(person_email,person_password):
	conn = getSQLConnection()
	cur = conn.cursor()
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



def inbox(email):
	conn = getSQLConnection()
	cur = conn.cursor()
	timenow=datetime.datetime.now()
	user_id=dal.person_id(cur,email)
	return dal.inbox(cur,user_id,timenow)


def outbox(email):
	conn = getSQLConnection()
	cur = conn.cursor()
	user_id=dal.person_id(cur,email)
	return dal.outbox(cur,user_id)


def letters_write(email,begin_time,end_time,content):
	conn = getSQLConnection()
	cur = conn.cursor()
	user_id = dal.person_id(cur,email)
	change_time = datetime.datetime.now()
	person_gender = dal.person_gender(cur,email)
	couple_id = dal.couple(cur,user_id,person_gender)
	peer_id = dal.peer(cur,person_gender,couple_id)
	dal.letters_write(cur,user_id,peer_id,begin_time,end_time,content,change_time)
	conn.commit()




def unread_letters_count(email):
	conn = getSQLConnection()
	cur = conn.cursor()
	user_id = dal.person_id(cur,email)
	return dal.unread_letters_count(cur,user_id)



def new_chat(email,content):
	conn = getSQLConnection()
	cur = conn.cursor()
	user_id = dal.person_id(cur,email)
	time = datetime.datetime.now()
	person_gender = dal.person_gender(cur,email)
	couple_id = dal.couple(cur,user_id,person_gender)
	peer_id = dal.peer(cur,person_gender,couple_id)
	dal.new_chat(cur,user_id,peer_id,time,content)
	conn.commit()


def previous_chat(email,skip,top):
	conn = getSQLConnection()
	cur = conn.cursor()
	user_id = dal.person_id(cur,email)
	person_gender = dal.person_gender(cur,email)
	couple_id = dal.couple(cur,user_id,person_gender)
	peer_id = dal.peer(cur,person_gender,couple_id)
	return dal.previous_chat(cur,peer_id,user_id,skip,top)














