import sqlite3

conn = sqlite3.connect(r'C:\Users\tuman\OneDrive\Desktop\МиТП_лабы\lr_7\bank.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS accounts(id INTEGER PRIMARY KEY, balance INTEGER)")
cur.execute("DELETE FROM accounts")
cur.execute("INSERT INTO accounts VALUES (1, 500)")
cur.execute("INSERT INTO accounts VALUES (2, 300)")
conn.commit()

try:
    conn.execute("BEGIN")

    cur.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
    cur.execute("UPDATE accounts SET balance = balance + 100 WHERE id = 2")

    conn.commit()        
    print("Транзакция успешна")
except Exception as e:
    conn.rollback()      
    print("Ошибка. Откат:", e)

for row in cur.execute("SELECT * FROM accounts"):
    print(row)

cur.close()
conn.close()