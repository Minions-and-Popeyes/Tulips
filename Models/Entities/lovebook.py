import cherrypy

class lovebook(object):
	def __init__(self,id,content,time,user):
		self.id = id
		self.content = content
		self.time = time
		self.user = user

	def save(self):
		cur = cherrypy.request.cur
		if self.id:
			cur.execute("UPDATE love_book SET content = %s, time = %s, user = %s where id = %s",(self.content,self.time,self.user,self.id))
		else:
			cur.execute("INSERT INTO love_book(content,time,user) VALUES(%s,%s,%s)",(self.content,self.time,self.user))
			self.id = cur.lastrowid
	@staticmethod
	def byid(cur,id):
		cur.execute("SELECT id,content,time,user FROM love_book where id = %s",(id,))
		res = cur.fetchall()
		if res:
			return lovebook(*res[0])
		return None
