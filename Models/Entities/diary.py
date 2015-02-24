import cherrypy

class diary(object):
	def __init__(self,id,time,content,user,permission):
		self.id = id
		self.time = time
		self.content = content
		self.user = user
		self.permission = permission
	def save(self):
		cur = cherrypy.request.cur
		if self.id:
			cur.execute("UPDATE diary SET time=%s,content=%s,user=%s,permission=%s",(self.time,self.content,self.user,self.permission))
		else:
			cur.execute("INSERT INTO diary(time,content,user,permission) values(%s,%s,%s,%s)",(self.time,self.content,self.user,self.permission))
			self.id=cur.lastrowid
	@staticmethod
	def byid(id):
		cur = cherrypy.request.cur
		cur.execute("SELECT * from diary where  id = %s",(id,))
		res = cur.fetchall()
		if res:
			return diary(*res[0])
		return None