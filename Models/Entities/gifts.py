import cherrypy

class gifts(object):
	def __init__(self,id,gift_photo,description,frm,to,date):
		self.id = id
		self.gift_photo =gift_photo
		self.description = description
		self.frm = frm
		self.to = to
		self.date = date
	def save(self):
		cur = cherrypy.request.cur
		if self.id:
			cur.execute("UPDATE gifts SET gift_photo=%s,description=%s,frm=%s,`to`=%s,`date`=%s",(self.gift_photo,self.description,self.frm,self.to,self.date))
		else:
			cur.execute("INSERT INTO gifts(gift_photo,description,frm,`to`,`date`) values(%s,%s,%s,%s,%s)",(self.gift_photo,self.description,self.frm,self.to,self.date))
			self.id=cur.lastrowid
	@staticmethod
	def byid(id):
		cur = cherrypy.request.cur
		cur.execute("SELECT * from gifts where  id = %s",(id,))
		res = cur.fetchall()
		if res:
			return gifts(*res[0])
		return None