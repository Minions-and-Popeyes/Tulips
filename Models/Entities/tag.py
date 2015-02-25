import cherrypy
class tag(object):
	def __init__(self,id,tag):
		self.id=id
		self.tag=tag

	@staticmethod
	def byid(id):
		cur = cherrypy.request.cur
		cur.execute("SELECT * FROM tag where id=%s",(self.id,))
		res = cur.fetchall()
		if res:
			return tag(*res[0])
		return None

	@staticmethod
	def all_tags():
		cur=cherrypy.request.cur
		cur.execute("SELECT * from tag");
		return {item[0]:tag(*item) for item in cur.fetchall()}