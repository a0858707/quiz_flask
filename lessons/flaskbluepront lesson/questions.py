from flask import Blueprint, render_template, request
question_bp = Blueprint('questions', __name__)

@question_bp.route('/all-questions')
def get_all_questions():
    all_questions = ['что такое фласк', 'как создать блюпринт']
    return render_template("all_questions.html", questions=all_questions)

#ссылка для публикации ответа
@question_bp.route('/public-answer', methods=["POST"])
def public_answer():
    # получить данныпе введенные на фронте
    answer_from_front = request.form.get('answer')
    print(answer_from_front)

    #перенаправлени обратно на ол квесшнс

    return redirect('/all-questions')
