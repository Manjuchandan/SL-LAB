from flask import Flask,redirect,url_for,request,session,render_template
import time
import re

app = Flask(__name__)

app.secret_key="secret"

@app.route("/", methods=["POST","GET"])

def index():

	try:
		balance=session["balance"]
		count=session["count"]

	except KeyError:
		balance=session["balance"]=9000
		count=session["count"]=0

	if request.method=="GET":
		return render_template("index.html",balance=balance,msg=" ")

	if request.method=="POST":

		if request.form["amount"]==" ":
			msg="Amount is required"
			return render_template("index.html", balance=balance, msg=msg)

		if int(request.form["amount"]) < 0:
			msg="can not enter negative amount"
			return render_template("index.html", balance=balance, msg=msg)

		if session["count"]==5:
			msg="5 transactions complete"
			return render_template("index.html", balance=balance, msg=msg)

		if request.form["action"]=="withdraw":
			if int(request.form["amount"]) > 5000:
				msg="can not withraw more than 5000"
				return render_template("index.html", balance=balance, msg=msg)
			else:
				balance=balance-int(request.form["amount"])
				session["balance"]=balance
				session["count"]=session["count"] + 1
				msg="money withdrawn"
				return render_template("index.html", balance=balance, msg=msg)

		elif request.form["action"]=="deposit":
				balance=balance+int(request.form["amount"])
				session["balance"]=balance
				session["count"]=session["count"] + 1
				msg="money deposited"
				return render_template("index.html", balance=balance, msg=msg)

if __name__=='__main__':
	app.run(debug=True)

