from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

#vytvoirm sitaku globalnejsiu instanciu
db = SQLAlchemy()

#vytvorim trieud ktora bude dedit z model
#keby sme definovali nejaku inu ktora nededi z model tak ta by sa nemapovala do DB
class Article(db.Model):
	#vytvorime stlpec 
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	content = db.Column(db.String)

