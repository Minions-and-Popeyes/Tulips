# -*- coding: utf-8 -*-
import datetime
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





def login_view(failed,redirect):
	s = u"""<html>
			  <body>"""
	if failed:
		s+=u"<p> 登陆失败，用户名或密码不正确 </p>"
	s+=u"""
			  <form action="/login_second" method="post">
			  	<input type=text name="person_email"  placeholder="邮箱"/>
			  	<input type=password name="person_password" placeholder="密码">"""
	s+=u'<input type="hidden" name="redirect" value={0} />'.format(redirect)
	s+=u"""<input type=submit value="登陆">
			  </form>
			  </body>
				</html>
	"""
	return s



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
			    var x = event.clientX;  
			    var y = event.clientY;  
			    var canvas = event.target;  
			    var loc = getPointOnCanvas(canvas, x, y);  
			    console.log("mouse down at point( x:" + loc.x + ", y:" + loc.y + ")");  
			    tempContext.beginPath();  
			    tempContext.moveTo(loc.x, loc.y);  
			    started = true;  
			}  
			  
			function doMouseMove(event) {  
			    var x = event.clientX;  
			    var y = event.clientY;  
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
					if(xmlhttp.readyState==4 && xmlhttp.status==200){
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





def calendar_view(data,data_couple,year,month):
	s = u"""<html>
		<head>
		<style type="text/css">
		#calendar{
			font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;
  			width:100%;
  			border-collapse:collapse;
  		}

  		#calendar td,#calendar th{
  		    font-size:1em;
  		    border-style: solid;
		    border-width:1px;
		    padding:50px 7px 2px 7px;
		}

		#calendar th{
			font-size:1.1em;
			text-align:left;
			padding-top:5px;
			padding-bottom:4px;
		}
		</style>
		



		<script>
			function foo1(year,month,day){
				x = new XMLHttpRequest()
				x.open('GET','/calendar_the_day_affair?year='+year+'&month='+month+'&day='+day,true)
				x.onreadystatechange = function(){
					if(x.readyState==4 && x.status==200){
						y = document.getElementById('pop')
						document.getElementById('content').innerHTML =x.responseText
						document.getElementById('st').setAttribute('value',''+year+'-'+month+'-'+day+' 08:00:00')
						document.getElementById('ed').setAttribute('value',''+year+'-'+month+'-'+day+' 10:00:00')
						y.hidden = false
					}
				}
				x.send()
			}
		</script>

		<div id="pop" hidden="true" style="position:absolute;width:30%; height:30%; top:20%; left:35%; background:cyan" onclick="document.getElementById('pop').hidden=false">
			<div id="content"></div>
			<form action="/calendar_second" method="post">
			起始时间<input id='st' type ="text" name = "begin_time"/><br/>
			结束时间<input id='ed' type ="text" name = "end_time"/><br/>
			事件<input type ="text" name = "affair"><br/>
			<input type ="submit" value ="完成">
			</form>
		</div>

	</head>
	<body>
	<table id="calendar" >
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


	dict = {}
	for a in data:
		dict[a[2].day] = (a[5],a[1])
	now = datetime.datetime(year,month,1)
	flag = True
	for i in range (5):
		s += "<tr>"
		print now.weekday()
		for j in range (7):
			print j
			if j==now.weekday() and flag:
				print 'asdf'
				if dict.has_key(now.day):
					if dict[now.day][1]==data_couple.boy:
						s += "<td onclick=\"foo1({0},{1},{2})\">{2}<br/><div style=\"background:blue\">{3}</div></td>".format(now.year,now.month,now.day,dict[now.day][0])
					else:
						s += "<td onclick=\"foo1({0},{1},{2})\">{2}<br/><div style=\"background:pink\">{3}</div></td>".format(now.year,now.month,now.day,dict[now.day][0])
				else:
					s+="<td onclick=\"foo1({0},{1},{2})\">{2}</td>".format(now.year,now.month,now.day)
				now += datetime.timedelta(1)
			else:
				s +="<td>"+"</td>"
			if now.month != month:
				flag = False
		s += "</tr>"
	s +="""</table>
	</body></html>
	"""
	return s

def gifts_chain(data):
	s = u"""
		  <html><body>
		  <form action="/gifts_second" method="post" enctype="multipart/form-data">
		  filename: <input type="file" name="myFile"/><br/>
		  <input type="textarea" name="description"/>

		  <input type="text" name="year" placeholder="2015"/>年
		  <input type="text" name="month" placeholder="2"/>月
		  <input type="text" name="day" placeholder="14"/>日<br/>
		  
		  TA送我的<input type="radio" name="who" value="TA"/><br/>
		  我送TA的<input type="radio" name="who" value="ME"/><br/>
		     
          <input type="submit"/>
            
		  </form>

	"""
	s += u"""
	      </body></html>
	"""
	return s

def photo_library(ids):
	s='<html><body>'
	for id in ids:
		s+='<a href="/photo?id={0}"><img src="/photo?id={0}&height=200&width=200" /></a>'.format(id)
	s+="""
	<form action="/upload_photo" method="post" enctype="multipart/form-data" >
		<input type="file" name="photo" />
		<input type="submit" />
	</form>
	</body></html>
	"""
	return s

def index_view(now,unread_count,login,days):
	s = u"""
	<html><body>
		<a href="/signup_first">注册</a><br />"""
	if login:
		s+=u'<a href="/logout">登出</a><br />'
		s+=u'<p>今天是我们在一起的第{0}天</p>'.format(int(math.ceil(days.total_seconds() /3600 / 24)))
	else:
		s+=u'<a href="/login_first">登陆</a><br />'
	s+="""<a href="/love_book_first?year={0}&month={1}&day={2}">Love Book</a><br />""".format(now.year,now.month,now.day)
	if unread_count:
		s+= u"<div> TA给你写了{0}封信，你还没有看喏</div>".format(unread_count)
	s+=u"""<a href="/letters_inbox">收件箱</a><br />
			<a href="/letters_outbox">发件箱</a><br />
			<a href="/chat_first">聊天</a><br />
			<a href="/letters_write_first">写信</a><br />
		</body></html>"""
	return s




