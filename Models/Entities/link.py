import cherrypy
import tag
class link(object):
	def __init__(self,id,link,user,desc,time,tags=[]):
		self.id = id
		self.link = link
		self.user = user
		self.desc = desc
		self.time = time
		self.tags = tags
	def _update_tags(self):
		cur = cherrypy.request.cur
		cur.execute("DELETE FROM link_tag WHERE link=%s",(self.id,))
		for tag in self.tags:
			cur.execute("INSERT INTO link_tag(link,tag) VALUES(%s,%s)",(self.id,tag))
	def _read_tags(self):
		cur = cherrypy.request.cur
		cur.execute("SELECT tag from link_tag where link=%s",(self.id,))
		self.tags = [item[0] for item in cur.fetchall()]
	def save(self):
		cur = cherrypy.request.cur
		if self.id:
			cur.execute("UPDATE link SET link=%s,user=%s,`desc`=%s, time=%s where id=%s ",(self.link,self.user,self.desc,self.time,self.id))
		else:
			cur.execute("INSERT INTO link(link,user,`desc`,time) VALUES(%s,%s,%s,%s)",(self.link,self.user,self.desc,self.time))
			self.id=cur.lastrowid
		self._update_tags()
	@staticmethod
	def byid(id):
		cur = cherrypy.request.cur
		cur.execute("SELECT * FROM link where id = %s",(id,))
		res = cur.fetchall()
		if res:
			obj = link(*res[0])
			obj._read_tags()
			return obj
		return None
