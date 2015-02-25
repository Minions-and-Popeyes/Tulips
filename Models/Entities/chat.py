import cherrypy
class chat(object):
	def __init__(self,id,time,content,frm,to):
		self.id = id
		self.time = time
		self.content = content
		self.frm = frm
		self.to = to
	def save(self):
		cur = cherrypy.request.cur
		if self.id:
			cur.execute("UPDATE chat SET time=%s,content=%s,`from`=%s, `to`=%s where id=%s ",(self.time,self.content,self.frm,self.to,self.id))
		else:
			cur.execute("INSERT INTO chat(time,content,`from`,`to`) VALUES(%s,%s,%s,%s)",(self.time,self.content,self.frm,self.to))
			self.id=cur.lastrowid
	@staticmethod
	def byid(cur,id):
		cur = cherrypy.request.cur
		cur.execute("SELECT id,time,content,`from`,`to` FROM chat where id = %s",(self.id,))
		res = cur.fetchall()
		if res:
			return chat(*res[0])
		return None
