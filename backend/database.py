import sqlite3

DATABASE = "devconnect.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                firebase_uid TEXT UNIQUE,
                name TEXT,
                email TEXT,
                role TEXT CHECK(role IN ('client', 'freelancer'))
            );
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                tech_stack TEXT,
                budget INTEGER,
                timeline TEXT,
                client_id INTEGER REFERENCES users(id)
            );
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS proposals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id INTEGER REFERENCES jobs(id),
                freelancer_id INTEGER REFERENCES users(id),
                message TEXT,
                rate INTEGER,
                timeline TEXT,
                status TEXT DEFAULT 'pending'
            );
        ''')
        conn.commit()
