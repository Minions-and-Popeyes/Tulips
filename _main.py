#coding:utf-8
import cherrypy
import mysql.connector as mysql
from datetime import datetime as d

class Controller(object):
	@cherrypy.expose
	def signup_first(self):
		return """<html>
				<body>
		        <form action="/signup_second" method="post">
		        	<input type="text" name="boy_name" placeholder="姓名"/>
		        	<input type="text" name="boy_address" placeholder="邮箱"/>
		        	<input type="password" name="boy_password" placeholder="密码"/>

		        	<input type="text" name="girl_name" placeholder="姓名"/>
		        	<input type="text" name="girl_address" placeholder="邮箱"/>
		        	<input type="password" name="girl_password" placeholder="密码"/>

		        	<input type="submit" value="登记"/>

		        </form>
				</body>
				</html>"""


	@cherrypy.expose
	def signup_second(self,boy_name,boy_address,boy_password,girl_name,girl_address,girl_password):
 		try:
	 		conn = mysql.connect(user='tulips',password='GottLoveFee',host='localhost',database='Tulips')
	 		cur = conn.cursor()
	 		cur.execute(" INSERT INTO user(name,email,password) values(%s,%s,%s) ", (boy_name,boy_address,boy_password) )
	 		cur.execute(" select last_insert_id()")
	 		boyid = cur.fetchall()[0][0]
	 		cur.execute(" INSERT INTO user(name,email,password) values(%s,%s,%s)",(girl_name,girl_address,girl_password))
	 		cur.execute(" select last_insert_id()")
	 		girlid = cur.fetchall()[0][0]
	 		cur.execute(" INSERT INTO couple(boy,girl,date) values(%s,%s,%s)",(boyid,girlid,d.now()) )
	 		conn.commit()
	 	except Exception as e:
	 		return "Signup Failed" + e.message
	 	return "Signup Successfully"

cherrypy.quickstart(Controller())
