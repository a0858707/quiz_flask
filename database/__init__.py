from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# импорт всех функций из файлов для бд
from database.leaderservice import *
from database.questionservice import *
from database.registerservice import *