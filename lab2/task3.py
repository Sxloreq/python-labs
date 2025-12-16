def filter_ips(input_file_path, output_file_path, allowed_ips):
    ip_counts = {}
    try:
      
        infile = open(input_file_path, "r")
        for line in infile:
            ip = line.split()[0] # IP іде першим
            if ip in allowed_ips:
                if ip in ip_counts:
                    ip_counts[ip] = ip_counts[ip] + 1
                else:
                    ip_counts[ip] = 1
        infile.close()

        # Запис в файл
        outfile = open(output_file_path, "w")
        for ip in ip_counts:
            line = ip + " - " + str(ip_counts[ip]) + "\n"
            outfile.write(line)
        outfile.close()
        print("Результат записано в", output_file_path)

    except FileNotFoundError:
        print("Вхідний файл не знайдено!")
    except IOError:
        print("Помилка при роботі з файлами!")

# Перевірка
allowed = ["127.0.0.1", "192.168.1.1"]
filter_ips("apache_logs.txt", "filtered_ips.txt", allowed)
