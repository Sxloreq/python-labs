from database.db_connection import get_connection

def create_tables():
    conn = get_connection()
    with conn:
        # Три таблиці одним блоком
        conn.executescript("""
        CREATE TABLE IF NOT EXISTS EventSources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            location TEXT,
            type TEXT
        );

        CREATE TABLE IF NOT EXISTS EventTypes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type_name TEXT UNIQUE NOT NULL,
            severity TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS SecurityEvents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            source_id INTEGER REFERENCES EventSources(id),
            event_type_id INTEGER REFERENCES EventTypes(id),
            message TEXT,
            ip_address TEXT,
            username TEXT
        );
        """)
    conn.close()

def insert_initial_event_types():
    conn = get_connection()
    initial_data = {
        "Login Success": "Informational",
        "Login Failed": "Warning",
        "Port Scan Detected": "Warning",
        "Malware Alert": "Critical"
    }
    with conn:
        for name, sev in initial_data.items():
            conn.execute("INSERT OR IGNORE INTO EventTypes (type_name, severity) VALUES (?, ?)", (name, sev))
    conn.close()
