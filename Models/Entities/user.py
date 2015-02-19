class user(object):
	def __init__(self,id, name, email, password, gender):
		self.id = id
		self.name = name
		self.email = email
		self.password = password
		self.gender = gender
	def save(self,cur):
		if self.id:
			cur.execute("UPDATE user SET name=%s, email=%s, password=%s, gender=%s where id=%s",(self.name,self.email,self.password,self.gender,self.id))
		else:
			cur.execute("INSERT INTO user(name,email,password,gender) VALUES(%s,%s,%s,%s)",(self.name,self.email,self.password,self.gender))
			cur.execute("SELECT last_insert_id()")
			self.id=cur.fetchall()[0][0]
	def byid(cur,id):
		cur.execute("SELECT id,name,email,password,gender FROM user WHERE id = %s",(id,))
		res = cur.fetchall()[0]
		return user(res[0],res[1],res[2],res[3],res[4])
	def byemail(cur,email):
		cur.execute("SELECT id,name,email,password,gender FROM user where email = %s",(email,))
		res = cur.fetchall()[0]
		return user(res[0],res[1],res[2],res[3],res[4])
