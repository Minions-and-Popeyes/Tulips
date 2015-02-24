import mysql.connector as mysql
import dal
import datetime
from Models.Entities.user import user
from Models.Entities.couple import couple
from Models.Entities.lovebook import lovebook
from Models.Entities.chat import chat
from Models.Entities.letter import letter
from Models.Entities.calendar import calendar
from Models.Entities.gifts import gifts

def signup(boy_name,boy_address,boy_password,girl_name,girl_address,girl_password):
	boy = user(None,boy_name,boy_address,boy_password,1)
	boy.save()
	girl = user(None,girl_name,girl_address,girl_password,0)
	girl.save()
	c = couple(None, boy.id ,girl.id,datetime.datetime.now())
	c.save()

def login(person_email,person_password):
	u = user.byemail(person_email)
	if u and person_password==u.password:
		return True
	else: 
		return False



def lovebook_items(u,year,month,day):
	c = couple.byuserid(u.id)
	begin_time = datetime.datetime(year,month,day,0,0,0)
	stop_time = datetime.datetime(year,month,day,23,59,59)
	return dal.lovebook_items(c.boy,c.girl,begin_time,stop_time)


def new_lovebook(new_content,u):
	change_time = datetime.datetime.now()
	lb = lovebook(None,new_content,change_time,u.id)
	lb.save()


def be_together_date(u):
	c = couple.byuserid(u.id)
	return c.date



def inbox(u):
	timenow=datetime.datetime.now()
	return dal.inbox(u.id,timenow)


def outbox(u):
	return dal.outbox(u.id)


def letters_write(u,begin_time,end_time,content):
	c = couple.byuserid(u.id)
	if c.boy==u.id:
		peer = c.girl
	else:
		peer = c.boy
	change_time = datetime.datetime.now()
	l = letter(None,begin_time,end_time,content,u.id,peer,change_time,0,None)
	l.save()

def unread_letters_count(u):
	return dal.unread_letters_count(u.id)

def new_chat(u,content):
	time = datetime.datetime.now()
	c = couple.byuserid(u.id)
	if c.boy==u.id:
		peer = c.girl
	else:
		peer = c.boy
	ch = chat(None,time,content,u.id,peer)
	ch.save()

def previous_chat(u,skip,top):
	c = couple.byuserid(u.id)
	if c.boy==u.id:
		peer = c.girl
	else:
		peer = c.boy
	return dal.previous_chat(peer,u.id,skip,top)



def new_affair(u,begin_time,end_time,affair,is_whole_day):
	ca = calendar(None,u.id,begin_time,end_time,affair,is_whole_day)
	ca.save()


def previous_affairs(u,year,month):
	c = couple.byuserid(u.id)
	if c.boy==u.id:
		peer = c.girl
	else:
		peer = c.boy
	st = datetime.datetime(year,month,1,0,0,0)
	if month == 12:
		ed = datetime.datetime(year+1,1,1,0,0,0)
	else:
		ed = datetime.datetime(year,month+1,1,0,0,0)
	return dal.affairs_in_range(u.id,peer,st,ed)


def the_day_affair(u,date):
	c = couple.byuserid(u.id)
	if c.boy==u.id:
		peer = c.girl
	else:
		peer = c.boy
	ed = date + datetime.timedelta(1)
	return dal.affairs_in_range(u.id,peer,date,ed)

def be_together_days(u):
	c = couple.byuserid(u.id)
	return datetime.datetime.now()-c.date


def image(u,photo_id):
	p = photo.byid(photo_id)
	c = couple.byuserid(u.id)
	if p and p.user != c.boy and p.user!=c.girl:
		p = None
	return p


def new_gift(u,myFile,description,date,who):
	pid = dal.uploadImage(u,myFile)
	c = couple.byuserid(u.id)
	if c.boy==u.id:
		peer = c.girl
	else:
		peer = c.boy
	if who==TA:
		g = gifts(None,pid,description,peer,u.id,date)
	else:
		g = gifts(None,pid,description,u.id,peer,date)
	g.save()



def previous_gifts(u):
	return dal.previous_gifts(u.id)



def new_diary(u,time,content,permission):
	if permission==None:
		d = diary(None,time,content,u.id,0)
	else:
		d = diary(None,time,content,u.id,1)
	d.save()



























