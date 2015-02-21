#coding=utf-8
import cherrypy
import bll
import view
import string
import datetime
import mysql.connector as mysql
from Models.Entities.user import user

class DBTool(cherrypy.Tool):
	def __init__(self):
		cherrypy.Tool.__init__(self,'on_start_resource',self.bind,priority=20)
	def _setup(self):
		cherrypy.Tool._setup(self)
		cherrypy.request.hooks.attach('on_end_resource',self.commit,priority=20)
	def bind(self):
		conn = mysql.connect(user='tulips',password='GottLoveFee',host='162.105.80.126',database='Tulips',pool_name='pool')
		cur = conn.cursor()
		cherrypy.request.conn = conn
		cherrypy.request.cur = cur
	def commit(self):
		try:
			cherrypy.request.conn.commit()
		except:
			cherrypy.request.conn.rollback()
			raise
		finally:
			cherrypy.request.conn.close()

def Auth(path=None):
	if cherrypy.request.cookie.has_key('email'):
		u = user.byemail(cherrypy.request.cookie['email'].value)
		if u:
			cherrypy.request.user = u
			return
	if path:
		raise cherrypy.HTTPRedirect('/login_first?redirect='+path)

cherrypy.tools.db = DBTool()
cherrypy.tools.auth = cherrypy.Tool('on_start_resource',Auth,priority=30)



class DBTool(cherrypy.Tool):
	def __init__(self):
		cherrypy.Tool.__init__(self,'on_start_resource',self.bind,priority=20)

	def _setup(self):
		cherrypy.Tool._setup(self,'on_end_resource',self)
	def bind(self):

class Controller(object):
	@cherrypy.expose('/')
	@cherrypy.tools.auth()
	def index(self):
		unread_count = None
		login = False
		if hasattr(cherrypy.request,'user'):
			unread_count = bll.unread_letters_count(cherrypy.request.user)
			login = True
		return view.index_view(datetime.datetime.now(),unread_count,login)

	@cherrypy.expose
	def logout(self):
		cherrypy.response.cookie['email']=''
		cherrypy.response.cookie['email']['max-age']=0
		raise cherrypy.HTTPRedirect('/')

	@cherrypy.expose
	def signup_first(self):
		return view.signup_view()


	@cherrypy.expose
	def signup_second(self,boy_name,boy_address,boy_password,girl_name,girl_address,girl_password):
	 	bll.signup(boy_name,boy_address,boy_password,girl_name,girl_address,girl_password)
	 	raise cherrypy.HTTPRedirect('/login_first')



	@cherrypy.expose
	def login_first(self,failed=0,redirect='/'):
		return view.login_view(failed,redirect)


	@cherrypy.expose
	def login_second(self,person_email,person_password,redirect):		
		if	bll.login(person_email,person_password):
			cherrypy.response.cookie['email']=person_email
			raise cherrypy.HTTPRedirect(redirect)
		raise cherrypy.HTTPRedirect('/login_first?failed=1&redirect='+redirect)

	@cherrypy.expose
	@cherrypy.tools.auth(path='/love_book_first')
	def love_book_first(self,year=None,month=None,day=None):
		if year and month and day:
			year = string.atoi(year)
			month = string.atoi(month)
			day = string.atoi(day)
		else:
			now = datetime.datetime.now()
			year = now.year
			month = now.month
			day = now.day
		data = bll.lovebook_items(cherrypy.request.user,year,month,day)
		together_date=bll.be_together_date(cherrypy.request.user)
		return view.lovebook_view(data,together_date)

	@cherrypy.expose
	@cherrypy.tools.auth(path='/')
	def love_book_second(self,new_content):
		bll.new_lovebook(new_content,cherrypy.request.user)
		t = datetime.datetime.now()

	@cherrypy.expose
	@cherrypy.tools.auth(path='/letters_inbox')
	def letters_inbox(self):
		data = bll.inbox(cherrypy.request.user)
		return view.letters_inbox_view(data)

	@cherrypy.expose
	@cherrypy.tools.auth(path='/letters_outbox')
	def letters_outbox(self):
		data = bll.outbox(cherrypy.request.user)
		return view.letters_outbox_view(data)

	@cherrypy.expose
	@cherrypy.tools.auth(path='/letters_write_first')
	def letters_write_first(self):
		return view.letters_write_view()


	@cherrypy.expose
	@cherrypy.tools.auth(path='/')
	def letters_write_second(self,begin_time,end_time,new_letter):
		begin = datetime.datetime.strptime(begin_time,'%Y-%m-%d %H:%M:%S')
		end = datetime.datetime.strptime(end_time,'%Y-%m-%d %H:%M:%S')
		bll.letters_write(cherrypy.request.user,begin_time,end_time,new_letter)
		raise cherrypy.HTTPRedirect('/letters_outbox')

	@cherrypy.expose
	@cherrypy.tools.auth(path='/chat_first')
	def chat_first(self,page=0):
		data = bll.previous_chat(cherrypy.request.user,page*10,10)
		return view.chat_view(data)


	@cherrypy.expose
	@cherrypy.tools.auth(path='/')
	def chat_second(self,chat_content):
		if not cherrypy.session.has_key('user'):
			return "Not Login"
		bll.new_chat(cherrypy.session['user'],chat_content)
		raise cherrypy.HTTPRedirect('chat_first')


	@cherrypy.expose
	def calendar_first(self):
		if not cherrypy.session.has_key('user'):
			return "Not Login"
		now = datetime.datetime.now()
		year = now.year
		month = now.month
		return view.calendar_view(year,month)



	@cherrypy.expose
	def calendar_second(self):
		if not cherrypy.session.has_key('user'):
			return "Not Login"

		







    
		












		bll.new_chat(cherrypy.request.user,chat_content)
		raise cherrypy.HTTPRedirect('/chat_first')

conf = {
	'/': {
		'tools.sessions.on': True,
		'tools.db.on': True
	}
}
cherrypy.quickstart(Controller(),'/',conf)
