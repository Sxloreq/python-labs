# Наш початковий список продуктів
sklad = {
    "молоко": 15,
    "кефір": 4,
    "сир": 10,
    "йогурт": 2,
    "масло": 3
}

def zmina_skladu(nazva, kst):
    if nazva in sklad:
        sklad[nazva] = sklad[nazva] + kst
        # Перевірка щоб не пішло в мінус
        if sklad[nazva] < 0:
            sklad[nazva] = 0
    else:
        sklad[nazva] = kst

# Робимо операції
zmina_skladu("молоко", -5)
zmina_skladu("йогурт", 10)
zmina_skladu("сметана", 6)

print("Зараз на складі:")
for tovar in sklad:
    print(tovar, ":", sklad[tovar])

# Шукаємо товари яких мало (менше 5)
malo_tovariv = []
for tovar in sklad:
    kilkist = sklad[tovar]
    if kilkist < 5:
        malo_tovariv.append(tovar)

print("Треба докупити:")
print(malo_tovariv)
