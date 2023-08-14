from database.models import User
from database import db

# Функция регистрации пользователя
def register_user_db(name, phone_number):
    # User check on able on base
    checker = User.query.filter_by(phone_number=phone_number).first()
    # If user exist
    if checker:
        return checker.id
    # add data on database
    new_user = User(name=name, phone_number=phone_number)
    db.session.add(new_user)
    db.session.commit()
    return new_user.id