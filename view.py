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
		s += "<div>"+str(a[3])+"</div><br />"
		s += '<img src="'+str(a[1])+'" /><br />'
		s += "<div>"+str(a[2])+"</div><br />"
	s+=u"""
			<canvas id="c" width="240" height="400" onmousedown="doMouseDown(event)" onmousemove="doMouseMove(event)" onmouseup="doMouseUp(event)" ></canvas>
			<input type="button" onclick="submit()" value="写好啦" />
			<script>
			var started = false
			var canvas = document.getElementById("c");  
			var tempContext = canvas.getContext("2d");

			function getPointOnCanvas(canvas, x, y) {  
			    var bbox = canvas.getBoundingClientRect();  
			    return { x: x - bbox.left * (canvas.width  / bbox.width),  
			            y: y - bbox.top  * (canvas.height / bbox.height)  
			            };  
			} 
			function doMouseDown(event) {  
			    var x = event.pageX;  
			    var y = event.pageY;  
			    var canvas = event.target;  
			    var loc = getPointOnCanvas(canvas, x, y);  
			    console.log("mouse down at point( x:" + loc.x + ", y:" + loc.y + ")");  
			    tempContext.beginPath();  
			    tempContext.moveTo(loc.x, loc.y);  
			    started = true;  
			}  
			  
			function doMouseMove(event) {  
			    var x = event.pageX;  
			    var y = event.pageY;  
			    var canvas = event.target;  
			    var loc = getPointOnCanvas(canvas, x, y);  
			    if (started) {  
			        tempContext.lineTo(loc.x, loc.y);  
			        tempContext.stroke();  
			    }  
			}  
			  
			function doMouseUp(event) {  
			    console.log("mouse up now");  
			    if (started) {  
			        doMouseMove(event);  
			        started = false;  
			    }  
			}  

			function submit() {
				xmlhttp = new XMLHttpRequest()
				xmlhttp.onreadystatechange = function () {
					if(xmlhttp.readystate==4 && xmlhttp.status==200){
						alter('添加Love Book成功')
						location.reload()
					}
				}
				xmlhttp.open("POST",'/love_book_second',true)
				xmlhttp.setRequestHeader('Content-type','application/x-www-form-urlencoded')
				xmlhttp.send('new_content='+encodeURIComponent(canvas.toDataURL()))
			}
		</script>
	</body></html>"""
	return s

	


def letters_inbox_view(data):
	s = u"""<html><body>
		"""

	for a in data:
		s += "<div>" + u"可看的时间段为：" + str(a[0]) + " -- " +str(a[1])+ "</div>"
		s += "<div>" + str(a[2]) +"</div>"
		if a[3]==0 :
			s += "<div>" + u"未读" +"</div>"
		else:
			s += "<div>" + u"已读" +"</div>"


	s+="""</body></html>
		"""
	return s





def letters_outbox_view(data):
	s = u"""<html><body>
		"""

	for a in data:
		s += "<div>" + u"可看的时间段为：" + str(a[1]) + " -- " +str(a[2])+ "</div>"
		s += "<div>" + u"修改时间为：" + str(a[6]) + "</div>"
		s += "<div>" + str(a[3]) +"</div>"
		if a[7]==0 :
			s += "<div>" + u"对方还没有看" +"</div>"
		else:
			s += "<div>" + u"对方已经看过啦  阅读时间为 ： " + str(a[8])+"</div>"


	s+="""</body></html>
		"""
	return s


def letters_write_view():
	return u"""<html><body>
					<form action="/letters_write_second" method="post">
						你可以在这里设置让TA看的时间哦
						<input type="text" name="begin_time" placeholder="起始时间"><br />
						<input type="text" name="end_time" placeholder="截止时间">
						<input type="textarea" name="new_letter" placeholder="给TA写点什么吧~">
						<input type="submit" value="写完啦">
					</form>
				</body></html>
			"""



def chat_view(data):
	s = u"""<html><body>
				<form action="/chat_second" method="post">
					<input type="text" name="chat_content" placeholder="和TA聊聊吧"><br/>
					<input type="submit" value="发给TA">
				</form>
				"""
	last_time = datetime.datetime(1900,1,1)
	for a in data[::-1]:
		if (a[1]-last_time).total_seconds() >=60:
			s += "<div>" + str(a[1]) +"</div>"
		if a[3]==1:
			s += "<div>" + "ME" +a[2] +"</div>"
		else:
			s += "<div>" + "TA" +a[2] +"</div>"
		last_time = a[1]
	s +="""</body></html>
			"""
	return s





def calendar_view(year,month):
	s = u"""<html>
		<head>
		<style type="text/css">
		#calender{
			font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;
  			width:100%;
  			border-collapse:collapse;
  		}

  		#calender td,#calendar th{
  		    font-size:1em;
		    border:1px solid #98bf21;
		    padding:3px 7px 2px 7px;
		}

		#calender th{
			font-size:1.1em;
			text-align:left;
			padding-top:5px;
			padding-bottom:4px;
		}
		

		}
		</style>

	</head>
	<body>
	<table id="calender">
	<tr>
	<th>一</th>
	<th>二</th>
	<th>三</th>
	<th>四</th>
	<th>五</th>
	<th>六</th>
	<th>日</th>
	</tr>


	"""

	now = datetime.datetime.now(year,month,1)
	flag = true
	for i in range (5):
		s += <tr>
		for j in range (7):
			if j==first.isoweekday() and flag:
				s += "<td>"+now.day+"</td>"
			else:
				s +="<td>"+"</td>"
			if now.month != month:
				flag = false
			now += datetime.timedelta(1)
		s += </tr>







	s +="""</table>
	</body></html>
	"""




def index_view(now,unread_count):
	s = u"""
	<html><body>
		<a href="/signup_first">注册</a><br />
		<a href="/login_first">登陆</a><br />
		<a href="/love_book_first?year={0}&month={1}&day={2}">Love Book</a><br />""".format(now.year,now.month,now.day)
	if unread_count:
		s+= u"<div> TA给你写了{0}封信，你还没有看喏</div>".format(unread_count)
	s+="</body></html>"
	return s





