from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
from forms import QuestionForm, AnswerForm, LoginForm

#настройка для защиты полей
app.config['CSRF_ENABLED']=True
app.config['SECRET_KEY']= 'SDVSBRGRZDFBZ'

current_user_email = None
@app.route ("/", methods=['POST', "GET"])
def main_page():
    global current_user_email
    if current_user_email:
        question_form = QuestionForm()

        return render_template('index.html', question_form=question_form)

    elif not current_user_email:
        login_form = LoginForm()

        if request.method == "POST":
            if login_form.validate_on_submit():
                user_password = session.get(login_form.email.data)
                if user_password == login_form.password.data:
                    current_user_email = login_form.email.data
    return render_template('authorization.html', login_form=login_form)

#мост для публикации вопроса
@app.route ("/public-question", methods=["POST"])
def public_question():
    question_form = QuestionForm()

    #получить значение полей
    header = question_form.question_header.data
    main_text = question_form.question_text.data
    print(header, main_text)
    return 'some text'

@app.route('/register', methods=["POST"])
def register_user():
    user_data = LoginForm()
    #получаем данные введенные в форму
    email =user_data.email.data
    password = user_data.password.data

    #генерим сессию
    session[email] = password

    return render_template("login.html", login_form=user_data)

app.run(debug=True)
