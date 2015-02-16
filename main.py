#coding=utf-8
import cherrypy
import bll
import signup
import login

class Controller(object):
	@cherrypy.expose
	def signup_first(self):
		return signup.signup_view()


	@cherrypy.expose
	def signup_second(self,boy_name,boy_address,boy_password,girl_name,girl_address,girl_password):
 		try:
	 		bll.signup(boy_name,boy_address,boy_password,girl_name,girl_address,girl_password)
	 	except Exception as e:
	 		return "Signup Failed" + e.message
	 	return "Signup Successfully"



	@cherrypy.expose
	def login_first(self):
		return login.login_view()


	@cherrypy.expose
	def login_second(self,person_email,person_password):		
		if	bll.login(person_email,person_password):
			cherrypy.session['user']=person_email
			return "Login Successfully"
		else:
			return "Login Failed"




	@cherrypy.expose
	def love_book(self,year,month,day):
		if not cherrypy.session['user']:
				return "Not Login"
		data = bll.lovebook(cherrypy.session['user'],year,month,day)
		together_date=be_together_date(cherrypy.session['user'])
		return lovebook_view(data,together_date)

	

conf = {
	'/': {
		'tools.sessions.on': True
	}
}
cherrypy.quickstart(Controller(),'/',conf)
