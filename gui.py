import tkinter as tk
from tkinter import messagebox
from database import add_user, get_user, add_message, add_friend

# Создание главного окна
def create_main_window():
    root = tk.Tk()
    root.title("Система обмена сообщениями")

    # Функция для входа
    def login():
        username = entry_username.get()
        password = entry_password.get()
        # Логика аутентификации
        user = get_user(username)
        if user and user[2] == password:
            messagebox.showinfo("Успех", "Вход выполнен!")
            root.destroy()  # Закрыть окно входа
            show_main_window(username)  # Открыть главное окно
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль")

    # Окно входа
    login_window = tk.Frame(root)
    login_window.pack()

    tk.Label(login_window, text="Логин").pack()
    entry_username = tk.Entry(login_window)
    entry_username.pack()

    tk.Label(login_window, text="Пароль").pack()
    entry_password = tk.Entry(login_window, show="*")
    entry_password.pack()

    login_button = tk.Button(login_window, text="Войти", command=login)
    login_button.pack()

    # Кнопка для регистрации
    register_button = tk.Button(login_window, text="Зарегистрироваться", command=lambda: show_register_window())
    register_button.pack()

    root.mainloop()

# Функция регистрации нового пользователя
def show_register_window():
    register_window = tk.Tk()
    register_window.title("Регистрация")

    tk.Label(register_window, text="Введите логин").pack()
    reg_username = tk.Entry(register_window)
    reg_username.pack()

    tk.Label(register_window, text="Введите пароль").pack()
    reg_password = tk.Entry(register_window, show="*")
    reg_password.pack()

    def register():
        username = reg_username.get()
        password = reg_password.get()
        add_user(username, password)  # Добавление пользователя в базу данных
        messagebox.showinfo("Успех", "Регистрация успешна!")
        register_window.destroy()  # Закрыть окно регистрации

    register_button = tk.Button(register_window, text="Зарегистрироваться", command=register)
    register_button.pack()

    register_window.mainloop()

# Главное окно
def show_main_window(username):
    main_window = tk.Tk()
    main_window.title("Основное окно")

    # Кнопка для отправки сообщения
    def send_message():
        # Логика отправки сообщений
        message = entry_message.get()
        messagebox.showinfo("Сообщение", f"Сообщение отправлено: {message}")
        add_message(1, 2, message)  # Пример использования базы данных

    def send_message():
        message = entry_message.get()
        if message:
            add_message(1, 2, message)  # Пример отправки сообщения
            messagebox.showinfo("Сообщение", f"Сообщение отправлено: {message}")
        print(f"Сообщение от пользователя 1 пользователю 2: {message}")  # Логирование отправки


    tk.Label(main_window, text=f"Привет, {username}!").pack()

    entry_message = tk.Entry(main_window)
    entry_message.pack()

    send_button = tk.Button(main_window, text="Отправить сообщение", command=send_message)
    send_button.pack()

    # Кнопка для добавления друга

    def add_friend_func():
        friend_username = entry_friend.get()
        friend = get_user(friend_username)
        if friend:
            add_friend(1, friend[0])  # Добавление друга в базу данных
            messagebox.showinfo("Друзья", f"{friend_username} добавлен в список друзей!")
            print(f"{friend_username} добавлен в друзья.")  # Логирование для проверки
        else:
            messagebox.showerror("Ошибка", "Пользователь не найден")


    entry_friend = tk.Entry(main_window)
    entry_friend.pack()
    add_friend_button = tk.Button(main_window, text="Добавить друга", command=add_friend_func)
    add_friend_button.pack()

    main_window.mainloop()

if __name__ == "__main__":
    create_main_window()
