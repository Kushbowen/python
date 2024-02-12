import sqlite3
conn = sqlite3.connect('afternoon.db')
print("opened database successfully")
conn.execute("INSERT INTO EMPLOYEE VALUES  (1, 'FAITH KARIMI', 34, 340000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES  (2, 'JANE KARIMI', 24, 440000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES  (3, 'KUSH BOWEN', 35, 120000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES  (4, 'MARK KURUI', 40, 500000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES  (5, 'WINNIE JANE', 28, 320000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES  (6, 'NATHAN MULWA', 25, 780000.00)")


conn.commit()
print("employee inserted successfully")
conn.close()