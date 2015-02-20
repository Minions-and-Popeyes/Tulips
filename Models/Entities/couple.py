import cherrypy

class couple(object):
	def __init__(self,id,boy,girl,date):
		self.id = id
		self.boy = boy
		self.girl = girl
		self.date = date
	def save(self):
		cur = cherrypy.request.cur
		if self.id:
			cur.execute("UPDATE couple SET boy=%s, girl=%s, date=%s where id=%s",(self.boy,self.girl,self.date,self.id))
		else:
			cur.execute("INSERT INTO couple(boy,girl,date) VALUES(%s,%s,%s)",(self.boy,self.girl,self.date))
			self.id = cur.lastrowid
	@staticmethod
	def byid(id):
		cur = cherrypy.request.cur
		cur.execute("SELECT id,boy,girl,date FROM couple where id=%s",(id,))
		res = cur.fetchall()
		if res:
			return couple(*res[0])
		return None
	@staticmethod
	def byuserid(uid):
		cur = cherrypy.request.cur
		cur.execute("SELECT id,boy,girl,date FROM couple where boy=%s or girl=%s",(uid,uid))
		res = cur.fetchall()
		if res:
			return couple(*res[0])
		return None