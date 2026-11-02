## intro to sql, sqlite3
# Employee database
import sqlite3

conn = sqlite3.connect("company.db")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        title TEXT,
        salary REAl
    )
""")

cursor.execute("""
    INSERT INTO employees (name, title, salary)
    SELECT 'Marcus Johnson', 'Software Engineer', 85000.00
    WHERE NOT EXISTS (
        SELECT 1 FROM employees
        WHERE name = 'Marcus Johnson'
    )
""")

conn.commit()

cursor.execute("SELECT * FROM employees")
employee = cursor.fetchone()

print(employee)

conn.close()