import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "grants.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS grants")

cursor.execute("""
CREATE TABLE grants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    sector TEXT,
    min_revenue REAL,
    max_revenue REAL,
    stage TEXT,
    dpiit_required INTEGER,
    state TEXT,
    description TEXT,
    documents TEXT
)
""")

sample = [
    ("Startup India Seed Fund", "AI", 0, 5000000, "Prototype", 1, "Any",
     "Seed funding support", "Pitch Deck, DPIIT Certificate"),

    ("Karnataka AI Grant", "AI", 0, 20000000, "MVP", 1, "Karnataka",
     "AI innovation support", "GST, Revenue Proof")
]

cursor.executemany("""
INSERT INTO grants 
(name, sector, min_revenue, max_revenue, stage, dpiit_required, state, description, documents)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", sample)

conn.commit()
conn.close()

print("Database reset and initialized successfully!")