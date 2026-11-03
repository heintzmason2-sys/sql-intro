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
    Where salary IS NOT NULL
    ORDER BY salary DESC
    LIMIT 3
""")

employees = cursor.fetchall()

for employee in employees:
    print(employee)

conn.close()