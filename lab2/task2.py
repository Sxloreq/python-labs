import hashlib

def generate_file_hashes(file_paths):
    hashes = {}
    for path in file_paths:
        try:
            f = open(path, "rb")
            content = f.read()
            h = hashlib.sha256(content).hexdigest()
            hashes[path] = h
            f.close()
        except FileNotFoundError:
            print("Файл не знайдено:", path)
        except IOError:
            print("Помилка читання:", path)
            
    return hashes

# Перевірка
files = ["apache_logs.txt", "task1.py"]
print(generate_file_hashes(files))
