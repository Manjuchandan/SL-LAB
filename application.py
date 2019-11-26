from flask import Flask, redirect, url_for ,render_template,request
import time
import re

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])

def indexJS():
	if request.method == 'GET':
		msg = "**hello user enter your details***"
		return render_template("indexJS.html",msg = msg)
	
	if request.method == 'POST':
 
		if request.form["usn"] == "" or request.form["dob"] == "" :
			msg = "All form fields are required**"
			return render_template("indexJS.html", msg=msg)


		try:
			time.strptime(request.form["dob"],"%d/%m/%Y")
		except ValueError:
			msg = "**date is invalid**"
			return render_template("indexJS.html", msg=msg)

		usn_pattern = "^[1][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$"

		if not re.match(usn_pattern, request.form["usn"]):
			msg ="**usn format invalid**"
			return render_template("indexJs.html", msg=msg)

		l=[request.form["usn"],request.form["dob"]]
              
		return render_template("success.html", l=l)



if __name__ == '__main__':
	app.run()
