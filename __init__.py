from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SECRET_KEY"] = "do not try"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

#create database 
db = SQLAlchemy(app)
migrate = Migrate(app)


from Grade_12 import views
