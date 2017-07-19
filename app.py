from flask import Flask, render_template
import random

app = Flask(__name__)
#flask name
@app.route('/')
def hello():
	return "<h1>hello, world</h1>"
@app.route('/goodbye')
def goodbye():
	return "<h1>goodbye, world</h1>"
@app.route('/quote')
def quote():
	Quotes=["<h2>let your life be guided by gratnes</h2>","<h2>be the best version of your self</h2>", "<h2>all great leaders are Readers</h2>","<h2>be patient everything is coming together</h2>","<h2>silence is better than bulshit</h2> "]
	return (random.choice(Quotes))
@app.route('/home')
def homepage():
	return render_template("home.html")
@app.route('/about')
def about():
	return render_template("hobbies.html")
@app.route('/snapchat')
def snapchat():
	return render_template("snapchat.html")
@app.route('/listExample')
def listExample():
	mylist = ["zack efron", "barack obama", "sadeel", "the rock", "minymoh" ]
	display = True
	return render_template("listExample.html", display= display, list = mylist)






if __name__ == "__main__":
	app.run()
