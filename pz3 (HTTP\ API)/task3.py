import json
import matplotlib.pyplot as plt

def plot_currency():
    try:

        with open("task1.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        dates = [item["exchangedate"] for item in data]
        rates = [item["rate"] for item in data]
        currency_name = data[0]["cc"]

        plt.figure(figsize=(10, 6))
        plt.plot(dates, rates, marker='o', linestyle='-', color='b', label=f'Курс {currency_name}')
        
        plt.title(f"Динаміка курсу {currency_name} за останній тиждень")
        plt.xlabel("Дата")
        plt.ylabel("Курс (UAH)")
        
        plt.grid(True)
        plt.legend()
        
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        
        plt.savefig("currency_graph.png")
        print("Графік збережено як 'currency_graph.png'")
        
        plt.show()

    except FileNotFoundError:
        print("Файл 'task1.json' не знайдено. Спочатку запустіть task2.py!")
    except Exception as e:
        print(f"Помилка при побудові графіка: {e}")

if __name__ == "__main__":
    plot_currency()
