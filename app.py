from flask import Flask, render_template, request
import random
import dataset

db = dataset.connect("postgres://hrtsghdazhopek:1dbaaca385a175c25fd0d48ede998636485a7feb2d7cbc026808dfb04f056c9b@ec2-23-21-96-159.compute-1.amazonaws.com:5432/d8a1a4j9tt3q74")

app = Flask(__name__)
#flask name

# @app.route('/quote')
# def quote():
# 	Quotes=["<h2>let your life be guided by gratnes</h2>","<h2>be the best version of your self</h2>", "<h2>all great leaders are Readers</h2>","<h2>be patient everything is coming together</h2>","<h2>silence is better than bulshit</h2> "]
# 	return (random.choice(Quotes))
@app.route('/')
@app.route('/home')
def homepage():
	return render_template("home.html")
@app.route('/about')
def about():
	return render_template("hobbies.html")
@app.route('/snapchat')
def snapchat():
	return render_template("snapchat.html")
@app.route('/quote')
def learn():
	return render_template("quote.html")
@app.route('/contact', methods =["GET", "POST"])
def contact():
	return render_template("contact.html")
@app.route('/feedback' ,methods=["POST"])
def feedback():
	form = request.form
	name= form["name"]
	email = form["email"]
	message= form["message"]

	contactsTable = db["contacts"]
	entry = {"name":name , "email":email , "message":message }
	contactsTable.insert(entry)
	print list(contactsTable.all())
	return render_template("action_page.html", name= name, message = message)
@app.route ('/showall')
def showall():
	contacts = db ["contacts"]
	allcontacts = list(contacts.all())
	return render_template ("showall.html", contacts= allcontacts)

	
# @app.route('/listExample')
# def listExample():
# 	mylist = ["zack efron", "barack obama", "sadeel", "the rock", "minymoh" ]
# 	display = True
# 	return render_template("listExample.html", display= display, list = mylist)






if __name__ == "__main__":
	app.run()
