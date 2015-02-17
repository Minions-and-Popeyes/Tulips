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

	