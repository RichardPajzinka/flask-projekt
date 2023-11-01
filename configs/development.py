#bude obsahovat veci pre moje dane vyvojove prostredie
DEBUG = True
DATABASE = "/vagrant/blog.db"
SQLALCHEMY_DATABASE_URI = "sqlite:////vagrant/blog.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////vagrant/blog.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False