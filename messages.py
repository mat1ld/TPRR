from database import create_connection

def send_message(sender, receiver, message):
    conn, cursor = create_connection()  # Получаем соединение и курсор
    cursor.execute('INSERT INTO messages (sender, receiver, message) VALUES (?, ?, ?)', 
                   (sender, receiver, message))
    conn.commit()
    conn.close()

def get_messages(sender, receiver):
    conn, cursor = create_connection()  # Получаем соединение и курсор
    cursor.execute('SELECT * FROM messages WHERE (sender = ? AND receiver = ?) OR (sender = ? AND receiver = ?)', 
                   (sender, receiver, receiver, sender))
    messages = cursor.fetchall()
    conn.close()
    return messages
