def analyze_log_file(log_file_path):
    results = {}
    try:
        f = open(log_file_path, "r")
        for line in f:
            parts = line.split()
            if len(parts) > 8:
              
                code = parts[8]
                if code in results:
                    results[code] = results[code] + 1
                else:
                    results[code] = 1
        f.close()
    except FileNotFoundError:
        print("Помилка: Файл не знайдено!")
    except IOError:
        print("Помилка читання файлу!")
    
    return results

# Перевірка
print(analyze_log_file("apache_logs.txt"))
