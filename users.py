import sqlite3
from database import create_table  # Импортируем функцию из database.py

def register_user(login, password, status='неактивен'):
    # Создаем таблицу, если она еще не существует
    create_table()

    # Подключаемся к базе данных
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()

    # Выполняем запрос на добавление пользователя
    cursor.execute('INSERT INTO users (login, password, status) VALUES (?, ?, ?)', (login, password, status))

    # Сохраняем изменения и закрываем соединение
    conn.commit()
    conn.close()

# Новая функция get_user_status
def get_user_status(login):
    # Подключаемся к базе данных
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()

    # Выполняем запрос для получения статуса пользователя
    cursor.execute('SELECT status FROM users WHERE login = ?', (login,))
    result = cursor.fetchone()

    # Если результат найден, возвращаем статус, иначе 'неизвестно'
    conn.close()
    return result[0] if result else 'неизвестно'
