## 11/02/26
## Sql practice for employee query
## Practice using sqlite3 to query employee database
## Day 2
import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT COUNT(*), title
    FROM employees
    GROUP BY title
    ORDER BY COUNT(*) DESC
""")

employees = cursor.fetchall()

for employee in employees:
    print(employee)

conn.close()