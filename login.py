#coding=utf-8
def login_view():
	return u"""<html>
			  <body>
			  <form action="/login_second" method="post">
			  	<input type=text name="person_email"  placeholder="邮箱"/>
			  	<input type=password name="person_password" placeholder="密码">

			  	<input type=submit value="登陆">
			  </form>
			  </body>
				</html>
	"""
