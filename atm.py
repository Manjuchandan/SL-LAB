from flask import Flask , redirect , render_template , url_for , request , session
import time
import re


app = Flask(__name__)

app.secret_key = "secret"

@app.route("/", methods=["POST" , "GET"])

def indexs():

	try:
		count = session["count"]
		balance = session["balance"]

	except KeyError:
		count = session["count"] = 0
		balance = session["balance"] = 8000

	if request.method == "GET":
		return render_template("indexs.html" , balance=balance , msg=" " )

	if request.method == "POST":

		if request.form["amount"] == " " :
			msg="amount is required"
			return render_template("indexs.html" , balance=balance , msg=msg)

		if int(request.form["amount"]) < 0 :
			msg="can not enter negative amount"
			return render_template("indexs.html" , balance=balance , msg=msg)

		if session["count"] == 5:
			msg="5 tracsactions is complete"
			return render_template("indexs.html" , balance=balance , msg=msg)

		if  request.form["action"] == "withdraw":

			if int(request.form["amount"]) > session["balance"] :
				msg="can not withdraw amount more than balance"
				return render_template("indexs.html" , balance=balance , msg=msg)

			elif int(request.form["amount"]) > 5000 :
				msg="can not withdraw amount more than 5000"
				return render_template("indexs.html" , balance=balance , msg=msg)


			else:
				balance = balance - int(request.form["amount"])
				session["balance"] = balance
				session["count"] = session["count"] + 1
				msg = "money withdrawn"
				return render_template("indexs.html" , balance=balance , msg=msg)

		elif  request.form["action"] == "deposit" :

			if int(request.form["amount"]) > 10000 :
				msg="can not deposit amount more than 10000"
				return render_template("indexs.html" , balance=balance , msg=msg)
			else:
				balance = balance + int(request.form["amount"])
				session["balance"] = balance
				session["count"] = session["count"] + 1
				msg = "money deposited"
				return render_template("indexs.html" , balance=balance , msg=msg)



if __name__ =='__main__' :
	app.run()



