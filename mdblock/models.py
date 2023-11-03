from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

#MODEL
#vytvoirm sitaku globalnejsiu instanciu
db = SQLAlchemy()

#vytvorim trieud ktora bude dedit z model
#keby sme definovali nejaku inu ktora nededi z model tak ta by sa nemapovala do DB
class Article(db.Model):
	#vytvorime stlpec 
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	content = db.Column(db.String)

#ked ideme mirgrovat
#ked ideme mirgrovat
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True)
	password = db.Column(db.String)
	#selft je metoda triedy
	def set_password(self,password):
		self.password = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password, password)