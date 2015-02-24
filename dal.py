import cherrypy
from PIL import Image
from StringIO import StringIO
from Models.Entities.photo import photo

def lovebook_items(id1,id2,begin_time,stop_time):
	cur = cherrypy.request.cur
	cur.execute("SELECT * from lovebook WHERE (user=%s or user=%s) and time>=%s and time<=%s  ORDER BY time desc",(id1,id2,begin_time,stop_time))
	return cur.fetchall()

def inbox(user_id,timenow):
	cur = cherrypy.request.cur
	cur.execute("SELECT begin_time,end_time,content,is_read from letters WHERE (`to`=%s) and %s >= begin_time and %s <= end_time ORDER BY id desc",(user_id,timenow,timenow))
	return cur.fetchall()

def outbox(user_id):
	cur = cherrypy.request.cur
	cur.execute("SELECT * from letters WHERE (`from`=%s) ORDER BY id desc",(user_id,))
	return cur.fetchall()

def unread_letters_count(user_id):
	cur = cherrypy.request.cur
	cur.execute("SELECT count(*) from letters where `to`=%s and is_read=0",(user_id,))
	return cur.fetchall()[0][0]


def new_chat(cur,user_id,peer_id,time,content):
	cur = cherrypy.request.cur
	cur.execute("INSERT INTO chat (time,content,`from`,`to`) values(%s,%s,%s,%s)",(time,content,user_id,peer_id))


def previous_chat(peer_id,user_id,skip,top):
	cur = cherrypy.request.cur
	cur.execute("SELECT id,time,content,`from`=%s from chat WHERE `from`=%s or `from`=%s ORDER BY id desc limit %s,%s",(user_id,peer_id,user_id,skip,top))
	return cur.fetchall()


def affairs_in_range(user_id,peer,begin_time,end_time):
	cur = cherrypy.request.cur
	cur.execute("SELECT * from calendar WHERE (user=%s or user=%s)and begin_time>=%s and begin_time<%s",(user_id,peer,begin_time,end_time))
	return cur.fetchall()

def uploadImage(u,photo_file):
<<<<<<< HEAD
	data = photo.file.read()
	p = photo(None,data,u.id)
=======
	im = Image.open(photo_file.file)
	buf = StringIO()
	im.save(buf,'PNG')
	p = photo(None,buf.getvalue(),u.id)
>>>>>>> origin/master
	p.save()
	return p.id


def previous_gifts(user_id):
	cur = cherrypy.request.cur
	cur.execute("SELECT user.gender,gifts.* from gifts left join user on user.id=gifts.to WHERE frm=%s or `to`=%s ORDER BY `date` desc",(user_id,user_id))
	return cur.fetchall()

	








