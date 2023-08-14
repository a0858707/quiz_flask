from flask import Flask
from database import db
app = Flask(__name__)

#настройка дб
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://quiz.db'
db.init_app(app)

