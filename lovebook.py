
def lovebook_view(data,together_date):
	s = """ <html> <body>
				days=Math.round((datetime.datetime(year,month,day,23,59,59)-together_date)
					/1000/3600/24			 
		"""
	for a in data:
		s += "<div>"+a[0]+"</div>"
		s += "<div>"+a[1]+"</div>"
		s += "<div>"+a[2]+"</div>"
	s+="""
		<form action="/demo/demo_form.asp" id="usrform">
			<input type="submit">
		</form>

		<textarea name="new content" form="usrform"> A Book Only Belongs to Your Twos </textarea>

	</body></html>"""
	return s

	