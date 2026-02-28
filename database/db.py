import sqlite3
import os

def fetch_grants():
    db_path = os.path.join(os.path.dirname(__file__), "grants.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM grants")
    data = cursor.fetchall()
    conn.close()
    return data