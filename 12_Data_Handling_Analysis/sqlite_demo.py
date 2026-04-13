# sqlite_demo.py

"""
Definition: SQLite is a C-language library that implements a small, fast, self-contained, 
high-reliability, full-featured, SQL database engine. Python has built-in support via 'sqlite3'.
"""

import sqlite3

def database_demo():
    # Connect to in-memory database
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    # Create table
    cursor.execute("CREATE TABLE students (id INTEGER, name TEXT)")
    
    # Insert data
    cursor.execute("INSERT INTO students VALUES (1, 'Kunal')")
    cursor.execute("INSERT INTO students VALUES (2, 'Rahul')")
    
    # Query data
    cursor.execute("SELECT * FROM students")
    print("Database Query Results:")
    for row in cursor.fetchall():
        print(f"  ID: {row[0]}, Name: {row[1]}")
    
    conn.close()

database_demo()
