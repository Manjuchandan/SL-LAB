from flask import Flask,redirect,render_template,url_for,request
import time
import re

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])

def Index():

	if request.method=="GET":
		return render_template("Index.html",msg="Welcome for Shopping!")



	if request.method=="POST":

		if int(request.form["i1"])<0 or int(request.form["i2"])<0 or int(request.form["i3"])<0:

			return render_template("Index.html",msg="No of items can not be Negative!")

		else:
			cost=100*int(request.form["i1"])+200*int(request.form["i2"])+500*int(request.form["i3"])
			return render_template("Index.html", msg="Total Cost = Rs"+str(cost))


if __name__=='__main__':
	app.run(debug=True)
