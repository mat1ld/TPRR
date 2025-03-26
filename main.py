from database import create_table, add_user, get_user_by_login, add_message, get_messages, add_friend, get_friends

def main():
    # Создаем таблицы (если их нет)
    create_table()  # Важно вызвать этот метод для создания всех таблиц

    # Пример регистрации пользователей
    add_user("user1", "password1")
    add_user("user2", "password2")

    # Получение пользователей из базы данных по логину
    user1 = get_user_by_login("user1")
    user2 = get_user_by_login("user2")

    # Пример отправки сообщения
    if user1 and user2:
        add_message(user1[0], user2[0], "Привет, как дела?")

    # Пример получения сообщений
    messages = get_messages(user1[0], user2[0])
    print("Сообщения между user1 и user2:")
    for message in messages:
        print(f"Сообщение: {message[0]}, Время: {message[1]}")

    # Пример добавления друга
    add_friend(user1[0], user2[0])

    # Получаем список друзей для user1
    friends = get_friends(user1[0])
    print("Друзья user1:")
    for friend_id in friends:
        friend = get_user_by_login(friend_id)
        print(friend)

if __name__ == "__main__":
    main()
