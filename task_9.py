import sqlite3
import csv

con = sqlite3.connect(r'C:\Users\tuman\OneDrive\Desktop\МиТП_лабы\lr_7\orders.db')
cur = con.cursor()

tables = [
    ('users', ['ID', 'Имя', 'Email']),
    ('orders', ['ID', 'Номер заказа', 'Сумма'])
]

for table, headers in tables:
    cur.execute(f"SELECT * FROM {table}")
    with open(fr'C:\Users\tuman\OneDrive\Desktop\МиТП_лабы\lr_7\{table}.csv', 'w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerows([headers] + cur.fetchall())

con.close()