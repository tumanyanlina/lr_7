import sqlite3

con = sqlite3.connect(r'C:\Users\tuman\OneDrive\Desktop\МиТП_лабы\lr_7\orders.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_number INT,
            sum INT)
            '''
            )

users_data = [
    ('Anna', 'annasm@mail.ru'),
    ('Ekaterina', 'kate1201@gmail.com')
]

orders_data = [
    (66736, 1854),
    (65471, 1564)
]
cur.executemany("INSERT INTO users(name, email) VALUES (?, ?)", users_data)
cur.executemany("INSERT INTO orders(order_number, sum) VALUES (?, ?)", orders_data)
con.commit()

print("Пользователи:")
cur.execute("SELECT * FROM users")
users = cur.fetchall()

for user in users:
    print(user)
print("Заказы:")
cur.execute("SELECT * FROM orders")
orders = cur.fetchall()

for order in orders:
    print(order)


con.close()