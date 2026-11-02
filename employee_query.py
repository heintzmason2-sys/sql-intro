## 11/02/26
## Sql practice for employee query
## Practice using sqlite3 to query employee database
## Day 2
import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT name, title
    FROM employees
""")

employees = cursor.fetchall()

for employee in employees:
    print(employee)

conn.close()