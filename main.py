#coding=utf-8
import cherrypy
import bll
import view
import string
import datetime

class DBTool(cherrypy.Tool):
	def __init__(self):
		cherrypy.Tool.__init__(self,'on_start_resource',self.bind,priority=20)
	def _setup(self):
		cherrypy.Tool._setup(self)
		cherrypy.request.hooks.attach('on_end_resource',self.commit,priority=20)
	def bind(self):
		conn = mysql.connect(user='tulips',password='GottLoveFee',host='162.105.80.126',database='Tulips',pool_name='pool')
		cur = conn.cursor()
		req = cherrypy.request
		req.conn = conn
		req.cur = cur
	def commit(self):
		try:
			cherrypy.request.conn.commit()
		except:
			cherrypy.request.conn.rollback()
			raise
		finally:
			cherrypy.request.cur.close()
			cherrypy.request.conn.close()

def Auth(path):
	if hasattr(cherrypy.request.cookie,email):
		u = user.byemail(email)
		if u:
			cherrypy.request.user = u
			return
	raise cherrypy.HTTPRedirect('/login_first?redirect='+path)

cherrypy.tools.db = DBTool()
cherrypy.tools.require_auth = Auth


class Controller(object):
	@cherrypy.expose('/')
	def index(self):
		unread_count = None
		if cherrypy.session.has_key('user'):
			unread_count = bll.unread_letters_count(cherrypy.session['user'])
		return view.index_view(datetime.datetime.now(),unread_count)

	@cherrypy.expose
	def signup_first(self):
		return view.signup_view()


	@cherrypy.expose
	def signup_second(self,boy_name,boy_address,boy_password,girl_name,girl_address,girl_password):
 		#try:
	 	bll.signup(boy_name,boy_address,boy_password,girl_name,girl_address,girl_password)
	 	#except Exception as e:
	 	#	return "Signup Failed" + e.message
	 	return "Signup Successfully"



	@cherrypy.expose
	def login_first(self):
		return view.login_view()


	@cherrypy.expose
	def login_second(self,person_email,person_password):		
		if	bll.login(person_email,person_password):
			cherrypy.session['user']=person_email
			raise cherrypy.HTTPRedirect('/')
		else:
			return "Login Failed"



	@cherrypy.expose
	def love_book_first(self,year,month,day):
		if not cherrypy.session.has_key('user'):
				return "Not Login"
		year = string.atoi(year)
		month = string.atoi(month)
		day = string.atoi(day)
		data = bll.lovebook(cherrypy.session['user'],year,month,day)
		together_date=bll.be_together_date(cherrypy.session['user'])

		# some other things
		return view.lovebook_view(data,together_date)

	@cherrypy.expose
	def love_book_second(self,new_content):
		if not cherrypy.session.has_key('user'):
				return "Not Login"
		print new_content
		bll.new_lovebook(new_content,cherrypy.session['user'])
		t = datetime.datetime.now()
		raise cherrypy.HTTPRedirect('/love_book_first?year={0}&month={1}&day={2}'.format(t.year,t.month,t.day))

	@cherrypy.expose
	def letters_inbox(self):
		if not cherrypy.session.has_key('user'):
				return "Not Login"
		data = bll.inbox(cherrypy.session['user'])
		return view.letters_inbox_view(data)

	@cherrypy.expose
	def letters_outbox(self):
		if not cherrypy.session.has_key('user'):
				return "Not Login"
		data = bll.outbox(cherrypy.session['user'])
		return view.letters_outbox_view(data)



	@cherrypy.expose
	def letters_write_first(self):
		if not cherrypy.session.has_key('user'):
			return "Not Login"
		return view.letters_write_view()


	@cherrypy.expose
	def letters_write_second(self,begin_time,end_time,new_letter):
		if not cherrypy.session.has_key('user'):
			return "Not Login"
		begin = datetime.datetime.strptime(begin_time,'%Y-%m-%d %H:%M:%S')
		end = datetime.datetime.strptime(end_time,'%Y-%m-%d %H:%M:%S')
		bll.letters_write(cherrypy.session['user'],begin_time,end_time,new_letter)
		raise cherrypy.HTTPRedirect('letters_outbox')




	@cherrypy.expose
	def chat_first(self,page=0):
		if not cherrypy.session.has_key('user'):
			return "Not Login"
		data = bll.previous_chat(cherrypy.session['user'],page*10,10)
		return view.chat_view(data)


	@cherrypy.expose
	def chat_second(self,chat_content):
		if not cherrypy.session.has_key('user'):
			return "Not Login"
		bll.new_chat(cherrypy.session['user'],chat_content)
		raise cherrypy.HTTPRedirect('chat_first')






    
		












	

conf = {
	'/': {
		'tools.sessions.on': True,
		'tools.db.on': True
	}
}
cherrypy.quickstart(Controller(),'/',conf)
