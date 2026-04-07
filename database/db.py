import sqlite3

DB_NAME = "datastalker.db"

def get_connection():
    """
    Create and return a database connection
    """
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Initialize database and create tables
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recruiter TEXT,
        frequency INTEGER,
        denied INTEGER,
        odd_time INTEGER,
        unknown INTEGER,
        risk_score INTEGER,
        decision TEXT
    )
    """)

    conn.commit()
    conn.close()