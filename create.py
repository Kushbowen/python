import sqlite3

conn = sqlite3.connect('afternoon.db')
print("opened database successfully")

conn.execute('''CREATE TABLE EMPLOYEE(
ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
SALARY REAL NOT NULL);''')


print("table created successfully")
conn.close()