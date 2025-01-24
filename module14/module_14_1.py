# Домашнее задание по теме "Создание БД, добавление, выбор и удаление элементов"
import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect("not_telegram.db")
    cursor = conn.cursor()
    # создать таблицу
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
       id INTEGER PRIMARY KEY,
       username TEXT NOT NULL,
       email TEXT NOT NULL,
       age INTEGER,
       balance INTEGER NOT NULL
       )
    ''')

    # удалить записи, если есть
    cursor.execute("DELETE FROM Users")

    # заполнить записями
    for i in range(1, 11):
        cursor.execute("INSERT INTO Users(username,email,age,balance) VALUES(?,?,?,1000)",
                       (f"User{i}", f"example{i}@gmail.com", i * 10))

    # Обновить баланс у каждой второй записи, начиная с 1-ой (установить на 500)
    # for i in range(1, 11, 2):
    #    cursor.execute("UPDATE Users SET balance=? WHERE id=?",(500, i))
    cursor.execute("UPDATE Users SET balance=? WHERE id % 2 = 1", (500,))

    # Удалить каждую третью запись, начиная с 1-ой
    # for i in range(1, 11, 3):
    #    cursor.execute("DELETE FROM Users WHERE id=?", (i,))
    cursor.execute("DELETE FROM Users WHERE id % 3 = 1")

    # Выборку всех записей при помощи fetchall(), где возраст не равен 60
    cursor.execute("SELECT username,email,age,balance FROM Users WHERE NOT age = ?", (60,))
    rows = cursor.fetchall()
    for r in rows:
        print(f"Имя: {r[0]}|Почта: {r[1]}|Возраст: {r[2]}|Баланс: {r[3]}")

    conn.commit()
    conn.close()
