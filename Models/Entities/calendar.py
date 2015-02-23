import cherrypy

class calendar(object):
	def __init__(self,id,user,begin_time,end_time,affair,is_whole_day):
		self.id = id
		self.user = user
		self.begin_time = begin_time
		self.end_time = end_time
		self.affair = affair
		self.is_whole_day = is_whole_day
	def save(self):
		cur = cherrypy.request.cur
		if self.id:
			if self.is_whole_day==1:
				cur.execute("UPDATE calendar SET user=%s, begin_time=%s, end_time=%s, content=%s,is_whole_day=%s where id=%s",(self.user,0,24,self.affair,1,self.id))
			else:
				cur.execute("UPDATE calendar SET user=%s, begin_time=%s, end_time=%s, content=%s,is_whole_day=%s where id=%s",(self.user, self.begin_time,self.end_time,self.affair,0,self.id))

		else:
			if self.is_whole_day==1:
				cur.execute("INSERT INTO calendar(user,begin_time,end_time,content,is_whole_day) values(%s,0,24,%s,1)",(self.user, self.affair,))
			if self.is_whole_day==0:
				cur.execute("INSERT INTO calendar(user,begin_time,end_time,content,is_whole_day) values(%s,%s,%s,%s,0)",(self.user, self.begin_time,self.end_time,self.affair))
			self.id=cur.lastrowid
	@staticmethod
	def byid(id):
		cur = cherrypy.request.cur
		cur.execute("SELECT * from calendar where id = %s",(id,))
		res = cur.fetchall()
		if res:
			return calendar(*res[0])
		return None