import cherrypy
class user(object):
	def __init__(self,id, name, email, password, gender):
		self.id = id
		self.name = name
		self.email = email
		self.password = password
		self.gender = gender
	def save(self):
		cur = cherrypy.request.cur
		if self.id:
			cur.execute("UPDATE user SET name=%s, email=%s, password=%s, gender=%s where id=%s",(self.name,self.email,self.password,self.gender,self.id))
		else:
			cur.execute("INSERT INTO user(name,email,password,gender) VALUES(%s,%s,%s,%s)",(self.name,self.email,self.password,self.gender))
			self.id=cur.lastrowid
	@staticmethod
	def byid(id):
		cur = cherrypy.request.cur
		cur.execute("SELECT id,name,email,password,gender FROM user WHERE id = %s",(id,))
		res = cur.fetchall()
		if res:
			return user(*res[0])
		return None
	@staticmethod
	def byemail(email):
		cur = cherrypy.request.cur
		cur.execute("SELECT id,name,email,password,gender FROM user where email = %s",(email,))
		res = cur.fetchall()
		if res:
			return user(*res[0])
		return None
