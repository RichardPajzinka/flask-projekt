from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import g
from flask import flash

#from .database import articles

import sqlite3
import os

#DATABASE = "/vagrant/blog.db"

flask_app = Flask(__name__)
#flask_app.secret_key = b'o\xa11\xe6\x84\xb7\x80\xa5\rA\xcf\xaf\xb62\xccA\xe3\xe1\x83\x98\xf4\xf2f['

flask_app.config.from_pyfile("/vagrant/configs/default.py")

if "MDBLOCK_CONFIG" in os.environ:
	flask_app.config.from_envvar("MDBLOCK_CONFIG")

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

@flask_app.route("/articles/", methods=["GET"])
def view_articles():
	db = get_db()
	cur = db.execute("select * from articles order by if desc")
	#tymto si do premennej articles natiahnem vsetky zaznami
	articles = cur.fetchall()
	return render_template("articles.jinja", articles=articles)

@flask_app.route("/articles/", methods=["POST"])
def add_articles():
	db = get_db()
	db.execute("insert into articles (title,content) values (?,?)",
		[request.form.get("title"), request.form.get("content")])
	db.commit()
	return redirect(url_for("view_articles"))

@flask_app.route("/articles/<int:art_id>")
def view_article(art_id):
	db = get_db()
	cur = db.execute("select * from where if=(?)",[art_id])
	article = cur.fetchone()
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
		if username == flask_app.config["USERNAME"] and password == flask_app.config["PASSWORD"]:
			#return "OK"
			session["logged"] = True
			flash("Login successful", "alert-success")
			return redirect(url_for("admin_page"))
		else:
			flash("Invalid successful", "alert-danger")
			#return "NOT OK"
			return redirect(url_for("view_login"))

@flask_app.route("/logout/", methods=["POST"])
def logout_user():
	session.pop("logged")
	flash("Logout successful", "alert-success")
	return redirect(url_for("welcome_page"))

#@flask_app.route("/admin/")
#def view_admin():
#	return"hello z inej url:"

#@flask_app.route("/admin/<string:name>/")
#def view_admin_name(name):
#	return"hello z URL: {}".format(name)

def connect_db():
	rv = sqlite3.connect(flask_app.config["DATABASE"])
	rv.row_factory = sqlite3.Row
	return rv

#spojenie iba jedno a je jedno ake
def get_db():
	if not hasattr(g, "sqlite_db"):
		g.sqlite_db = connect_db()
	return g.sqlite_db

@flask_app.teardown_appcontext
def close_db(error):
	if hasattr(g, "sqlite_db"):
		g.sqlite_db.close()

def init_db(app):
	with app.app_context():
		db = get_db()
		with open("mdblock/schema.sql", "r") as fp:
			db.cursor().executescript(fp.read())
		db.commit()
