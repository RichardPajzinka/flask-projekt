from flask import Flask
from flask import render_template

from .database import articles

flask_app = Flask(__name__)

@flask_app.route("/")
def welcome_page():
	return render_template("welcome_page.html")

@flask_app.route("/about/")
def about():
	return render_template("about.jinja")

@flask_app.route("/admin_page/")
def admin_page():
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

#@flask_app.route("/admin/")
#def view_admin():
#	return"hello z inej url:"

#@flask_app.route("/admin/<string:name>/")
#def view_admin_name(name):
#	return"hello z URL: {}".format(name)

