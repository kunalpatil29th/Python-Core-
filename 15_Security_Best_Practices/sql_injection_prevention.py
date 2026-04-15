# sql_injection_prevention.py

"""
Definition: SQL Injection is a vulnerability where an attacker can interfere with the queries that an application makes to its database. 
Prevention: Always use parameterized queries or an ORM instead of string formatting.
"""

import sqlite3

def secure_query(user_input):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
    
    # WRONG WAY (Vulnerable to SQL Injection):
    # query = f"SELECT * FROM users WHERE username = '{user_input}'"
    
    # RIGHT WAY (Parameterized Query):
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (user_input,))
    print(f"Executed query safely with input: {user_input}")

# Usage
secure_query("admin' OR '1'='1")
