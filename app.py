from flask import Flask

flask_app = Flask(__name__)

@flask_app.route("/")
def index():
	return "hello world"

@flask_app.route("/admin/")
def view_admin():
	return"hello z inej url:"

@flask_app.route("/admin/<string:name>/")
def view_admin_name(name):
	return"hello z URL: {}".format(name)