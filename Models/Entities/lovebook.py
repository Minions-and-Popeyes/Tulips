class love_book(object):
	def __init__(self,id,content,time,user):
		self.id = id
		self.content = content
		self.time = time
		self.user = user

	def save(self,cur):
		if id:
			cur.execute("UPDATE love_book SET content = %s, time = %s, user = %s where id = %s",(self.content,self.time,self.user,self.id))
		else:
			cur.execute("INSERT INTO love_book(content,time,user) VALUES(%s,%s,%s)",(self.content,self.time,self.user))
			cur.execute("SELECT last_insert_id()")
			self.id = cur.fetchall()[0][0]
	def byid(cur,id):
		cur.execute("SELECT id,content,time,user FROM love_book where id = %s",(id,))
		res = cur.fetchall()[0]
		return love_book(res[0],res[1],res[2],res[3])
