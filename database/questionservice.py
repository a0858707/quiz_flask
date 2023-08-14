from database.models import Question
from database import db

# Функция добавления вопроса -7 параметров
def add_questions_db(main_text, v1, v2, v3, v4, correct_answer, level):
    new_question = Question(main_text=main_text,
                            v1=v1, v2=v2, v3=v3, v4=v4,
                            correct_answer=correct_answer, level=level)
    db.session.add(new_question)
    db.session.commit()
    return True

# Вывести 20 вопросов - 1 параметр level=level.all, query.all
def get_question_db(level):
    questions = Question.query.filter_by(level=1).all()
    return questions[:21]

# Проверка ответа пользователя
def check_user_answer_db(question_id, user_answer):
    questions = Question.query.filter_by(id=question_id).first()
    if questions.correct_answer == user_answer:
        return True
    else:
        return False