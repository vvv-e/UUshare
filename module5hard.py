# Дополнительное практическое задание по модулю: "Классы и объекты."

class UrTube:
    """
    Уртуб.
    Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
    """

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        evrika = False
        hsh = 0
        cu = None
        for usr in self.users:
            if nickname == usr.nickname:
                cu = usr
                hsh = usr.password
                evrika = True
                break
        if evrika:
            if hash(password) == hsh:
                self.current_user = usr
            else:
                print(f"Пользователь с именем {nickname} неправильно задал пароль.")
        else:
            print(f"Пользователь с именем {nickname} не существует.")

    def register(self, nickname, password, age):
        evrika = False
        for usr in self.users:
            if nickname == usr.nickname:
                evrika = True
                break
        if evrika:
            print(f"Пользователь {nickname} уже существует.")
        else:
            usr = User(nickname, password, age)
            if not usr is None:
                self.users.append(usr)
                self.current_user = usr
            else:
                print(f"Текущий пользователь не изменен по причине: Пользователь {nickname} не создан.")

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        for v_par in video:
            evrika = False
            for v in self.videos:
               pass # if v_par ==

    def get_videos(self, video):
        pass

    def watch_video(self, title):
        pass


class User:
    """
    Пользователь.
    Атрибуты: nickname(имя пользователя, строка), password(хэш-код, число), age(возраст, число)
    """

    def __new__(cls, *args, **kwargs):
        if not isinstance(args[0], str):
            print("Имя пользователя должно быть строковым. Объект Пользователь не создан.")
        elif not isinstance(args[1], str):
            print("Пароль должен быть строковым. Объект Пользователь не создан.")
        elif not isinstance(args[2], int):
            print("Возраст должен быть целым числом. Объект Пользователь не создан.")
        else:
            return super().__new__(cls)

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    """
    Видео.
    Атрибуты:title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)),
             adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """

    def __new__(cls, *args, **kwargs):
        if not isinstance(args[0], str):
            print("Название фильма должно быть строковым. Объект Видео не создан.")
        elif not isinstance(args[1], int):
            print("Продолжительность фильма должна быть целым числом. Объект Видео не создан.")
        elif kwargs.get('adult_mode') != None and not isinstance(kwargs['adult_mode'], bool):
            print("Ограничение по возрасту должно быть логическим значением. Объект Видео не создан.")
        else:
            return super().__new__(cls)

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
