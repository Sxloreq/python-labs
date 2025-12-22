import requests
import json
from datetime import datetime, timedelta

def get_currency_rates():
    currency_code = "USD"
    days_to_check = 7
    data_list = []
    
    today = datetime.now()

    print(f"Починаю збір даних для {currency_code} за останні {days_to_check} днів...")

    for i in range(days_to_check):
        current_date = today - timedelta(days=i)
        date_str = current_date.strftime("%Y%m%d")
        
        url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&date={date_str}&json"
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data:

                    item = data[0]
                    data_list.append(item)
                    print(f"Отримано курс за {item['exchangedate']}: {item['rate']}")
            else:
                print(f"Помилка запиту для дати {date_str}")
        except Exception as e:
            print(f"Сталася помилка: {e}")

    data_list.sort(key=lambda x: datetime.strptime(x['exchangedate'], "%d.%m.%Y"))


    with open("task1.json", "w", encoding="utf-8") as f:
        json.dump(data_list, f, indent=4, ensure_ascii=False)
    
    print("\nДані успішно збережено у файл 'task1.json'")

if __name__ == "__main__":
    get_currency_rates()
