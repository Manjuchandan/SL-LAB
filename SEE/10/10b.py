from flask import Flask,redirect,url_for,request,render_template
import time
import re

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])

def student():

	if request.method=="GET":
		return render_template("student.html" , msg="Register Here!")



	if request.method=="POST":
		
		if request.form["usn"]==" " or request.form["dob"]==" " or int(request.form["m1"])==" " or int(request.form["m1"])==" " or int(request.form["m1"])==" " :

			return render_template("student.html" , msg="All fields are required!")
	
		elif int(request.form["m1"])<0 or int(request.form["m1"])<0 or int(request.form["m1"])<0 :
			
			return render_template("student.html" , msg="Negative marks not allowed!")
	

		else:

			try:
				time.strptime(request.form["dob"] , "%d/%m/%Y")
			except ValueError:
				return render_template("student.html" , msg="Date is invalid!")
	


		usn_pattern="^[1][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$"

		if re.match(usn_pattern , request.form["usn"]):
			avg=(int(request.form["m1"]) + int(request.form["m2"]) + int(request.form["m3"]))/3
			return render_template("student.html" , msg="Average = "+str(avg))


		else:
			return render_template("student.html" , msg="USN is invalid!")
	

	
if __name__=='__main__':
	app.run(debug=True)
