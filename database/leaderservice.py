from database import db
from database.models import Leaders, UserAnswer

# record results this test
def user_end_test_db(user_id, correct_answers, level):
    exact_user_score = Leaders.query.fiter_by(user_id=user_id, level=level).first()
    # проверить есть ли чтото внутри базы.
    if exact_user_score:
        # к старым очкам добавить текущие
        exact_user_score.score += correct_answers
        # если не было пользователя
        db.session.commit()
    else:
        new_leader_data=Leaders(user_id, level=level, score=correct_answers)

        db.session.add(new_leader_data)
        db.session.commit()
    return True

def get_top_5_leaders_db(level):
    exact_level_leaders = Leaders.query.filter_by(level=level).order_by(Leaders.score.desc()).all()
    """
    1-20 
    2-40
    3-12
    4-30
    5-60
    """
    return exact_level_leaders[:6]
#запись каждого пользователя
def add_user_answer_db(user_id, q_id, user_answer, correctness):
    new_answer = UserAnswer(user_id=user_id,
                            question_id=q_id,
                            user_answer=user_answer,
                            correctness=correctness)
    db.session.add(new_answer)
    db.session.commit()
    return True

