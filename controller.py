import random
from config import bot
from models import session, User

def initUser(user_id, username):
    users = session.query(User).filter(User.id == user_id).scalar()
    if users is None:
        newUser = User(id=user_id, username=username)
        User.add(newUser)

def deletePartner(userId, sendNotif = False):
    user = User.get(userId)
    user.partnerId = None
    if sendNotif:
        notification(userId, f"Собеседник закончил диалог")
    session.commit()

def getPartnerId(userId):
    return User.get(userId).partnerId

def getRandomPartner(user_id):
    try:
        result = session.query(User).filter(User.id != user_id).filter(User.partnerId == None).all()

        potent_part = [user.id for user in result]
        if len(potent_part) == 0:
            notification(user_id, "Пока нет свободных собеседников, попробуйте найти собеседника позже")
            return -1
        else:
            return potent_part[random.randint(0, len(potent_part) - 1)]
    except ConnectionError:
        print("mda")

def nextPartner(user_id):
    try:
        user = User.get(user_id)
        print("user: ", user)
        if user.partnerId is None:
            futurePart = getRandomPartner(user.id)
            if futurePart != -1:
                user.partnerId = futurePart
                notification(user_id, "У вас новый собеседник")
                partner = User.get(futurePart)
                partner.partnerId = user_id
                notification(futurePart, "У вас новый собеседник")
                session.commit()
        else:
            partnerId = user.id
            deletePartner(user_id)
            deletePartner(partnerId, True)
            nextPartner(user_id)

    except ConnectionError:
        print("какая-то ошибка")

def getStatus(userId):
    user = User.get(userId)
    return f"мой Id: {user.id} \n" \
           f"статус: {'без собеседника' if user.partnerId is None else 'есть собеседник'} \n"



def notification(user_id, msg):
    bot.send_message(user_id, msg)