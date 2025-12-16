import requests
from datetime import datetime, timedelta

# Налаштування: сьогодні та 7 до цього
today = datetime.today()
one_week_ago = today - timedelta(days=7)

# Форматування дат для запиту
end_date = today.strftime("%Y%m%d")
start_date = one_week_ago.strftime("%Y%m%d")

print("Введіть код валюти (наприклад: usd, eur, pln).")
print("Введіть 'exit' для завершення.\n")

while True:
    currency = input("Введіть код валюти: ").lower()

    if currency == "exit":
        print("Програму завершено.")
        break

    url = (
        "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
        f"?valcode={currency.upper()}"
        f"&date={end_date}"
        "&json"
    )

    print(f"Надсилання запиту для {currency.upper()}...")

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if not data:
            print("Валюту не знайдено. Спробуйте ще раз.\n")
        else:
            # Результат
            item = data[0]
            print(f"\nКурс {item['txt']} ({item['cc']}) на {item['exchangedate']}:")
            print(f"Рейт: {item['rate']} UAH\n")
    else:
        print(f"Помилка! Код статусу: {response.status_code}")
