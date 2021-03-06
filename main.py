#coding=utf-8
import cherrypy
import bll
import dal
import view
import string
import datetime
import mysql.connector as mysql
from Models.Entities.user import user
from Models.Entities.couple import couple
from Models.Entities.photo import photo
from Models.Entities.tag import tag
from Models.Entities.link import link


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

class Controller(object):
	@cherrypy.expose('/')
	@cherrypy.tools.auth()
	def index(self):
		unread_count = None
		login = False
		be_together_days = None
		if hasattr(cherrypy.request,'user'):
			unread_count = bll.unread_letters_count(cherrypy.request.user)
			be_together_days = bll.be_together_days(cherrypy.request.user)
			login = True
		return view.index_view(datetime.datetime.now(),unread_count,login,be_together_days)

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
		bll.new_chat(cherrypy.request.user,chat_content)
		raise cherrypy.HTTPRedirect('chat_first')


	@cherrypy.expose
	@cherrypy.tools.auth(path='/calendar_first')
	def calendar_first(self):
		now = datetime.datetime.now()
		year = now.year
		month = now.month
		data = bll.previous_affairs(cherrypy.request.user,year,month)
		data_couple = couple.byuserid(cherrypy.request.user.id)
		return view.calendar_view(data,data_couple,year,month)


	@cherrypy.expose
	@cherrypy.tools.auth(path='/calendar_the_day_affair')
	def calendar_the_day_affair(self,year,month,day):
		date = datetime.datetime(int(year),int(month),int(day),0,0,0)
		s = ''
		for item in bll.the_day_affair(cherrypy.request.user,date):
			s +='from {0} to {1} do {2}'.format(item[2],item[3],item[5])
		return s



	@cherrypy.expose
	@cherrypy.tools.auth(path='/')
	def calendar_second(self,begin_time,end_time,affair):
		begin = datetime.datetime.strptime(begin_time,"%Y-%m-%d %H:%M:%S")
		ed = datetime.datetime.strptime(end_time,"%Y-%m-%d %H:%M:%S")
		bll.new_affair(cherrypy.request.user,begin_time,end_time,affair,0)
		raise cherrypy.HTTPRedirect('/calendar_first')



	@cherrypy.expose
	@cherrypy.tools.auth(path='/gifts_first')
	def gifts_first(self):
		data = bll.previous_gifts(cherrypy.request.user)
		return view.gifts_chain(data)




	@cherrypy.expose
	@cherrypy.tools.auth(path='/')
	def gifts_second(self,myFile,description,year,month,day,who):
		date = datetime.datetime(int(year),int(month),int(day))
		bll.new_gift(cherrypy.request.user,myFile,description,date,who)
		raise cherrypy.HTTPRedirect('/gifts_first')

	
	@cherrypy.expose
	@cherrypy.tools.auth(path='/')
	def photo_library(self,page=0):
		ids = bll.photos(cherrypy.request.user,page*10,10)
		return view.photo_library(ids)

	def testupload(self):
		return """
        <html><body>
            <h2>Upload a file</h2>
            <form action="/upload_photo" method="post" enctype="multipart/form-data">
            filename: <input type="file" name="photo" /><br />
            <input type="submit" />
            </form>
            <h2>Download a file</h2>
            <a href='download'>This one</a>
        </body></html>
        """

	@cherrypy.expose
	@cherrypy.tools.auth(path='/')
	def photo(self,id,height=None,width=None):
		if height:
			height = int(height)
		if width:
			width = int(width)
		content = bll.image_string_content(cherrypy.request.user,id,width,height)
		cherrypy.response.headers['Content-Type']='image/png'
		return content

	@cherrypy.expose
	@cherrypy.tools.auth(path='/')
	def upload_photo(self,photo):
		i = dal.upload_image(cherrypy.request.user,photo)
		raise cherrypy.HTTPRedirect('/photo_library'.format(i))



	@cherrypy.expose
	@cherrypy.tools.auth(path='diary')
	def diary_first(self):
		return view.diary_view()



	@cherrypy.expose
	@cherrypy.tools.auth(path='/')
	def diary_second(self,content,permission=None,year=None,month=None,day=None):
		if year and month and day and permission:
			year = string.atoi(year)
			month = string.atoi(month)
			day = string.atoi(day)
			permission = permission
		else:
			now = datetime.datetime.now()
			year = now.year
			month = now.month
			day = now.day
			permission = None
		time = datetime.datetime(int(year),int(month),int(day))
		bll.new_diary(cherrypy.request.user,time,content,permission)
		raise cherrypy.HTTPRedirect('/')


	@cherrypy.expose
	@cherrypy.tools.auth(path='/diary_previous_peer')
	def diary_previous_peer(self):
		data = bll.previous_diary_peer(cherrypy.request.user)
		return view.previous_diary_peer(data)



	@cherrypy.expose
	@cherrypy.tools.auth(path='/diary_previous_me')
	def diary_previous_me(self):
		data = bll.previous_diary_me(cherrypy.request.user)
		return view.previous_diary_me(data)

	@cherrypy.expose
	@cherrypy.tools.auth(path='/links')
	def links(self,page=0):
		data = bll.links(cherrypy.request.user,page*10,10)
		tags = tag.all_tags()
		return view.links(data,tags)

	@cherrypy.expose
	@cherrypy.tools.auth(path='/')
	def add_link(self,link,desc,tags):
		bll.add_link(cherrypy.request.user,link,desc,map(int,tags))
		raise cherrypy.HTTPRedirect('/links')


import os
cwd = os.getcwd()

conf = {
	'/': {
		'tools.sessions.on': True,
		'tools.db.on': True
	},
	'/static' :{
		'tools.staticdir.on': True,
		'tools.staticdir.dir': '{0}/static'.format(cwd),
		'tools.db.on': False
	},
	'/favicon.ico' : {
		'tools.staticfile.on': True,
		'tools.staticfile.filename': '{0}/static/favicon.ico'.format(cwd),
		'tools.db.on': False
	}

}
cherrypy.quickstart(Controller(),'/',conf)
