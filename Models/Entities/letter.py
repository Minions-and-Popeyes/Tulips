import cherrypy

class letter(object):
	def __init__(self,id,begin_time,end_time,content,frm,to,modified_time,is_read,read_time):
		self.id = id
		self.begin_time = begin_time
		self.end_time = end_time
		self.content = content
		self.frm = frm
		self.to = to
		self.modified_time = modified_time
		self.is_read = is_read
		self.read_time = read_time
	def save(self):
		cur = cherrypy.request.cur
		if self.id:
			cur.execute("UPDATE letters SET begin_time=%s, end_time=%s, content=%s,`from`=%s, `to`=%s, modified_time=%s, is_read=%s, read_time=%s",(self.begin_time,self.end_time,self.content,self.frm,self.to,self.modified_time,self.is_read,self.read_time))
		else:
			cur.execute("INSERT INTO letters(begin_time,end_time,content,`from`,`to`,modified_time,is_read) values(%s,%s,%s,%s,%s,%s,0)",(self.begin_time,self.end_time,self.content,self.frm,self.to,self.modified_time))
			self.id=cur.lastrowid
	@staticmethod
	def byid(id):
		cur = cherrypy.request.cur
		cur.execute("SELECT id,begin_time,end_time,content,`from`,`to`,modified_time,is_read,read_time from letters where id = %s",(id,))
		res = cur.fetchall()
		if res:
			return letters(*res[0])
		return None