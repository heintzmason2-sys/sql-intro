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
cursor.execute("PRAGMA table_info(employees)")
columns = cursor.fetchall()
for column in columns:
    print(column)

cursor.execute("""
    INSERT INTO employees (name, title, salary)
    SELECT 'Marcus Johnson', 'Software Engineer', 85000.00
    WHERE NOT EXISTS (
        SELECT 1 FROM employees
        WHERE name = 'Marcus Johnson'
    )
""")

cursor.executemany("""
    INSERT INTO employees (name, title, salary)
    VALUES (?, ?, ?)
    """, [
        ("Sarah Williams", "Data Analyst", 92000),
        ("David Chen", "Backend Developer", 105000),
        ("Emily Rodriguez", "Cybersecurity Analyst", 98000),
        ("James Wilson", "Software Engineer", 115000),
        ("Olivia Martinez", "Database Admin", 88000)
    ])

conn.commit()

cursor.execute("SELECT * FROM employees")
employees = cursor.fetchall()

for employee in employees:
    print(employee)

conn.close()