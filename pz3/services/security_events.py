from database.db_connection import get_connection
from datetime import datetime

def add_security_event(src_id, type_id, msg, ip=None, user=None):
    conn = get_connection()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = "INSERT INTO SecurityEvents (timestamp, source_id, event_type_id, message, ip_address, username) VALUES (?,?,?,?,?,?)"
    conn.execute(sql, (now, src_id, type_id, msg, ip, user))
    conn.commit()
    conn.close()

def detect_bruteforce():
    conn = get_connection()
    query = """
    SELECT ip_address, COUNT(id) as total
    FROM SecurityEvents
    WHERE event_type_id = (SELECT id FROM EventTypes WHERE type_name = 'Login Failed')
      AND timestamp >= datetime('now', '-1 hour')
    GROUP BY ip_address
    HAVING total > 5
    """
    rows = conn.execute(query).fetchall()
    conn.close()
    return rows

def search_events(text):
    conn = get_connection()
    rows = conn.execute("SELECT * FROM SecurityEvents WHERE message LIKE ?", (f"%{text}%",)).fetchall()
    conn.close()
    return rows
