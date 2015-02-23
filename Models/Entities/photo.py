import cherrypy
class photo(object):
	def __init__(self,id, content, user):
		self.id = id
		self.content = content
		self.user = user
	def save(self):
		cur = cherrypy.request.cur
		if self.id:
			cur.execute("UPDATE photo SET content=%s, user=%s where id=%s",(self.content,self.user,self.id))
		else:
			cur.execute("INSERT INTO photo(content,user) VALUES(%s,%s)",(self.content,self.user))
			self.id=cur.lastrowid
	@staticmethod
	def byid(id):
		cur = cherrypy.request.cur
		cur.execute("SELECT id,content,user FROM photo WHERE id = %s",(id,))
		res = cur.fetchall()
		if res:
			return photo(*res[0])
		return None
