from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session

from .database import articles

flask_app = Flask(__name__)
flask_app.secret_key = b'o\xa11\xe6\x84\xb7\x80\xa5\rA\xcf\xaf\xb62\xccA\xe3\xe1\x83\x98\xf4\xf2f['

@flask_app.route("/")
def welcome_page():
	return render_template("welcome_page.html")

@flask_app.route("/about/")
def about():
	return render_template("about.jinja")

@flask_app.route("/admin_page/")
def admin_page():
	if "logged" not in session:
		return redirect(url_for("view_login"))
	return render_template("admin.jinja")

@flask_app.route("/articles/")
def view_articles():
	return render_template("articles.jinja", articles=articles.items())

@flask_app.route("/articles/<int:art_id>")
def view_article(art_id):
	article = articles.get(art_id)
	if article:
		return render_template("article.jinja", article=article)
	return render_template("article_nenajdeny.jinja", art_id=art_id)

@flask_app.route("/login/", methods=["GET"])
def view_login():
	return render_template("login.jinja")

@flask_app.route("/login/", methods=["POST"])
def login_user():
	#if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		if username == "admin" and password == "admin":
			#return "OK"
			session["logged"] = True
			return redirect(url_for("admin_page"))
		else:
			#return "NOT OK"
			return redirect(url_for("view_login"))

@flask_app.route("/logout/", methods=["POST"])
def logout_user():
	session.pop("logged")
	return redirect(url_for("welcome_page"))

#@flask_app.route("/admin/")
#def view_admin():
#	return"hello z inej url:"

#@flask_app.route("/admin/<string:name>/")
#def view_admin_name(name):
#	return"hello z URL: {}".format(name)

