from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
app= Flask(__name__)

@app.route("/")
def Home():
	return render_template("home.html")

@app.route("/about_me")
def About_me():
	return render_template("about_me.html")

@app.route("/contact_me")
def Contact_me():
	return render_template("contact_me.html")

if __name__ == "__main__":
	app.debug = True
	app.run()
