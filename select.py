import sqlite3
conn = sqlite3.connect('afternoon.db')
print("opened database successfully")

cursor = conn.execute("SELECT * FROM EMPLOYEE")
for row in cursor:
    print("ID :", row[0])
    print("NAME :", row[1])
    print("AGE :", row[2])
    print("SALARY :", row[3])

print("records found")

conn.close()