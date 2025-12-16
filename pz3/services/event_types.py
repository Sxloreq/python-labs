from database.db_connection import get_connection
import sqlite3

def add_event_type(name, level):
    """Реєстрація нової категорії події з визначеним рівнем важливості"""
    db = get_connection()
    try:
        with db:
            sql_query = "INSERT INTO EventTypes (type_name, severity) VALUES (?, ?)"
            db.execute(sql_query, (name, level))
        print(f">> Категорію '{name}' додано до бази.")
    except sqlite3.IntegrityError:
        print(f">> Помилка: Тип події '{name}' вже є у списку!")
    finally:
        db.close()

def get_event_types():
    """Отримання повного переліку типів подій, відсортованих за ID"""
    db = get_connection()
    all_types = []
    try:
        query = "SELECT id, type_name, severity FROM EventTypes ORDER BY id ASC"
        all_types = db.execute(query).fetchall()
    except Exception as error:
        print(f">> Не вдалося завантажити типи подій: {error}")
    finally:
        db.close()
    
    return all_types
