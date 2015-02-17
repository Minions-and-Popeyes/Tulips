# -*- coding: utf-8 -*-
def signup_view():
	return u"""<html>
				<body>
		        <form action="/signup_second" method="post">
		        	<input type="text" name="boy_name" placeholder="姓名"/>
		        	<input type="text" name="boy_address" placeholder="邮箱"/>
		        	<input type="password" name="boy_password" placeholder="密码"/>

		        	<input type="text" name="girl_name" placeholder="姓名"/>
		        	<input type="text" name="girl_address" placeholder="邮箱"/>
		        	<input type="password" name="girl_password" placeholder="密码"/>

		        	<input type="submit" value="完成"/>

		        </form>
				</body>
				</html>"""





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



import math
import datetime

def lovebook_view(data,together_date):
	s = """ <html> <body>
							 
		"""
	days=math.ceil((datetime.datetime.now()-together_date).total_seconds()/1000/3600/24)
	s+="<div>"+str(days)+"</div>"

	for a in data:
		s += "<div>"+str(a[3])+"</div>"
		s += "<div>"+str(a[1])+"</div>"
		s += "<div>"+str(a[2])+"</div>"
	s+="""
		<form action="/love_book_second" id="usrform">
			<input type="submit">
		</form>

		<textarea name="new_content" form="usrform"> A Book Only Belongs to Your Twos </textarea>

	</body></html>"""
	return s

	


def letters_inbox_view(data):
	s = """<html><body>
		"""

	for a in data:
		s += "<div>" + "可看的时间段为：" + str(a[0]) + " -- " +str(a[1])+ "</div>"
		s += "<div>" + str(a[2]) +"</div>"
		if a[3]==0 :
			s += "<div>" + "未读" +"</div>"
		else:
			s += "<div>" + "已读" +"</div>"


	s+="""</body></html>
		"""
	return s





def letters_outbox_view(data):
	s = """<html><body>
		"""

	for a in data:
		s += "<div>" + "可看的时间段为：" + str(a[1]) + " -- " +str(a[2])+ "</div>"
		s += "<div>" + "修改时间为：" + str(a[6]) + "</div>"
		s += "<div>" + str(a[3]) +"</div>"
		if a[7]==0 :
			s += "<div>" + "对方还没有看" +"</div>"
		else:
			s += "<div>" + "对方已经看过啦  阅读时间为 ： " + str(a[8])+"</div>"


	s+="""</body></html>
		"""
	return s









