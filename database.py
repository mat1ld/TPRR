import sqlite3

def create_connection():
    """Создаем подключение к базе данных и возвращаем соединение и курсор."""
    conn = sqlite3.connect('data/database.db')  # Путь к файлу базы данных
    cursor = conn.cursor()
    return conn, cursor

def create_table():
    """Создаем таблицы users, messages и friends, если они еще не существуют."""
    conn, cursor = create_connection()  # Получаем соединение и курсор

    # Создаем таблицу users, если она еще не существует
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        login TEXT NOT NULL,
                        password TEXT NOT NULL,
                        status TEXT NOT NULL DEFAULT 'неактивен'
                    )''')

    # Создаем таблицу messages, если она еще не существует
    cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        sender INTEGER NOT NULL,
                        receiver INTEGER NOT NULL,
                        message TEXT NOT NULL,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (sender) REFERENCES users(id),
                        FOREIGN KEY (receiver) REFERENCES users(id)
                    )''')

    # Создаем таблицу friends, если она еще не существует
    cursor.execute('''CREATE TABLE IF NOT EXISTS friends (
                        user_id INTEGER NOT NULL,
                        friend_id INTEGER NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES users(id),
                        FOREIGN KEY (friend_id) REFERENCES users(id),
                        PRIMARY KEY (user_id, friend_id)
                    )''')

    conn.commit()
    conn.close()

# Вызов функции для создания таблиц при старте программы
create_table()

def add_user(login, password, status="неактивен"):
    """Добавляем нового пользователя в таблицу users."""
    conn, cursor = create_connection()
    cursor.execute("INSERT INTO users (login, password, status) VALUES (?, ?, ?)", (login, password, status))
    conn.commit()

    # Проверка, что пользователь был добавлен
    cursor.execute("SELECT * FROM users WHERE login=?", (login,))
    user = cursor.fetchone()
    if user:
        print(f"Пользователь {login} успешно добавлен.")
    else:
        print(f"Ошибка при добавлении пользователя {login}.")
    
    conn.close()


def get_user_by_login(login):
    """Получаем информацию о пользователе по логину."""
    conn, cursor = create_connection()
    cursor.execute("SELECT * FROM users WHERE login=?", (login,))
    user = cursor.fetchone()
    conn.close()
    return user

def add_message(sender_id, receiver_id, message):
    """Добавляем сообщение в таблицу messages."""
    conn, cursor = create_connection()
    cursor.execute("INSERT INTO messages (sender, receiver, message) VALUES (?, ?, ?)", (sender_id, receiver_id, message))
    conn.commit()
    conn.close()

def get_messages(sender_id, receiver_id):
    """Получаем список сообщений между двумя пользователями."""
    conn, cursor = create_connection()
    cursor.execute("SELECT message, timestamp FROM messages WHERE sender=? AND receiver=?", (sender_id, receiver_id))
    messages = cursor.fetchall()
    conn.close()
    return messages

def add_friend(user_id, friend_id):
    """Добавляем пользователя в список друзей другого пользователя, если они еще не друзья."""
    conn, cursor = create_connection()

    # Проверяем, есть ли уже такая связь в таблице friends
    cursor.execute("SELECT 1 FROM friends WHERE user_id = ? AND friend_id = ?", (user_id, friend_id))
    if cursor.fetchone():
        print(f"Пользователь {user_id} уже добавлен в друзья пользователя {friend_id}")
    else:
        # Добавляем связь, если её нет
        cursor.execute("INSERT INTO friends (user_id, friend_id) VALUES (?, ?)", (user_id, friend_id))
        conn.commit()
        print(f"Пользователь {user_id} добавлен в друзья пользователя {friend_id}")
    
    conn.close()

def get_friends(user_id):
    """Получаем список друзей пользователя."""
    conn, cursor = create_connection()  # Открываем соединение

    cursor.execute("SELECT friend_id FROM friends WHERE user_id=?", (user_id,))
    friends = cursor.fetchall()

    friend_usernames = []
    for friend_id in friends:
        # Получаем логин друга по его ID
        cursor.execute("SELECT login FROM users WHERE id=?", (friend_id[0],))
        friend = cursor.fetchone()
        if friend:
            friend_usernames.append(friend[0])  # Добавляем логин друга в список
    
    conn.close()  # Закрываем соединение после выполнения всех запросов
    return friend_usernames


