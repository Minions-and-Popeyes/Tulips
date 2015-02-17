#coding=utf-8
import cherrypy
import bll
import view
import string
import datetime

class Controller(object):
	@cherrypy.expose
	def signup_first(self):
		return view.signup.signup_view()


	@cherrypy.expose
	def signup_second(self,boy_name,boy_address,boy_password,girl_name,girl_address,girl_password):
 		try:
	 		bll.signup(boy_name,boy_address,boy_password,girl_name,girl_address,girl_password)
	 	except Exception as e:
	 		return "Signup Failed" + e.message
	 	return "Signup Successfully"



	@cherrypy.expose
	def login_first(self):
		return view.login_view()


	@cherrypy.expose
	def login_second(self,person_email,person_password):		
		if	bll.login(person_email,person_password):
			cherrypy.session['user']=person_email
			return "Login Successfully"
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













	

conf = {
	'/': {
		'tools.sessions.on': True
	}
}
cherrypy.quickstart(Controller(),'/',conf)
