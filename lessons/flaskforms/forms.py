from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

# форма публикации вопросов
class QuestionForm(FlaskForm):
    question_header = StringField('Заголовок', validators=[DataRequired('обязательно')])
    question_text = TextAreaField('Опиши проблему', validators=[DataRequired('обязательно')])
    button = SubmitField("Опубликовать")

#форма для ответа
class AnswerForm(FlaskForm):
    answer_text = TextAreaField('ответ на вопрос', validators=[DataRequired('обязательно')])
    button = SubmitField('Ответить')

#login logout
class LoginForm(FlaskForm):
    email = StringField('почта', validators=[DataRequired()])
    password = StringField('пароль', validators=[DataRequired()])
    button = SubmitField("войти/зарегаться")
