from flask import Flask, render_template
from questions import question_bp
app = Flask(__name__)
#рега компонентов
app.register_blueprint(question_bp)

@app.route('/')
def hello_world():
    names= ['JEF', 'JOHN']
    return render_template('index.html', blabla=names)
#динамическая генераци ссылок
@app.route('/product/<string:name>')
def get_my_name(name):
    return f'Hello {name}✋'

app.run()