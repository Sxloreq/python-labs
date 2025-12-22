from database.db_setup import create_tables, insert_initial_event_types
from services import event_sources, event_types, security_events

def main():
    create_tables()
    insert_initial_event_types()

    while True:
        print("\n--- MONITORING SYSTEM v2 ---")
        print("1. Реєстрація джерела | 2. Новий тип події | 3. Записати лог")
        print("4. Перевірка Brute-force | 5. Пошук у логах | 0. Вихід")
        
        cmd = input("\nОберіть дію: ")

        if cmd == "1":
            n = input("Назва: ")
            l = input("IP/Локація: ")
            t = input("Тип (Firewall/Server): ")
            event_sources.add_event_source(n, l, t)
            print(">> Джерело збережено.")

        elif cmd == "4":
            attacks = security_events.detect_bruteforce()
            if not attacks:
                print(">> Атак не виявлено.")
            for ip, count in attacks:
                print(f"!! УВАГА: IP {ip} має {count} спроб входу!")

        elif cmd == "0":
            print("Завершення роботи...")
            break

if __name__ == "__main__":
    main()
