from database.db_connection import get_connection

def add_event_source(source_name, source_loc, source_type):
    """Реєстрація нового джерела подій у системі"""
    db = get_connection()
    try:
        with db:
            query = "INSERT INTO EventSources (name, location, type) VALUES (?, ?, ?)"
            db.execute(query, (source_name, source_loc, source_type))
        print(f">> Джерело '{source_name}' успішно збережено.")
    except Exception as e:
        print(f">> Помилка при додаванні джерела: {e}")
    finally:
        db.close()

def get_event_sources():
    """Отримання списку всіх зареєстрованих джерел"""
    db = get_connection()
    data = []
    try:
        cursor = db.execute("SELECT id, name, location FROM EventSources ORDER BY name ASC")
        data = cursor.fetchall()
    except Exception as e:
        print(f">> Не вдалося отримати дані: {e}")
    finally:
        db.close()
    
    return data
