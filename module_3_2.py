# Домашняя работа по уроку "Способы вызова функции".

# проверка на правильность эл.адреса почты
def is_adr_normal(s):
    adr = s.lower()
    if adr.find("@") == -1:
        return False
    elif adr.find(".com") == -1 and adr.find(".ru") == -1 and adr.find(".net") == -1:
        return False
    else:
        return True

# рассылка писем
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if not is_adr_normal(recipient) or not is_adr_normal(sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return
    elif recipient.lower() == sender.lower():
        print("Нельзя отправить письмо самому себе!")
        return
    elif sender.lower() == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        return
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        return

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
