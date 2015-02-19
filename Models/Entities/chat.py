class chat(object):
	def __init__(self,id,time,content,from,to):
		self.id = id
		self.time = time
		self.content = content
		self.from = from
		self.to = to
	def save(self,cur):
		if self.id:
			cur.execute("UPDATE chat SET time=%s,content=%s,`from`=%s, `to`=%s where id=%s ",(self.time,self.content,self.from,self.to,self.id))
		else:
			cur.execute("INSERT INTO chat(time,content,`from`,`to`) VALUES(%s,%s,%s,%s)",(self.time,self.content,self.from,self.to))
			cur.execute("SELECT last_insert_id()")
			self.id=cur.fetchall()[0][0]
	def byid(cur,id):
		cur.execute("SELECT id,time,content,from,to FROM chat where id = %s",(id,))
		res = cur.fetchall()[0]
		return chat(res[0],res[1],res[2],res[3],res[4])
