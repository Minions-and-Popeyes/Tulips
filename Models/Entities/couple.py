class couple(object):
	def __init__(self,id,boy,girl,date):
		self.id = id
		self.boy = boy
		self.girl = girl
		self.date = date
	def save(self,cur):
		if self.id:
			cur.execute("UPDATE couple SET boy=%s, girl=%s, date=%s where id=%s",(self.boy,self.girl,self.date,self.id))
		else:
			cur.execute("INSERT INTO couple(boy,girl,date) VALUES(%s,%s,%s)",(self.boy,self.girl,self.date))
			cur.execute("SELECT last_insert_id()")
			self.id = cur.fetchall()[0][0]
	def byid(cur,id):
		cur.execute("SELECT id,boy,girl,date FROM couple where id=%s",(id,))
		res = cur.fetchall()[0]
		return couple(res[0],res[1],res[2],res[3])
	def byuserid(cur,uid):
		cur.execute("SELECT id,boy,girl,date FROM couple where boy=%s or girl=%s",(uid,uid))
		res = cur.fetchall()[0]
		return couple(res[0],res[1],res[2],res[3])