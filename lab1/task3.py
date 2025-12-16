# Список продажів електроніки
prodazhi = [
    {"tovar": "myshka", "kilkist": 50, "cina": 300},
    {"tovar": "klaviatura", "kilkist": 20, "cina": 800},
    {"tovar": "monitor", "kilkist": 5, "cina": 5000},
    {"tovar": "myshka", "kilkist": 10, "cina": 300},
    {"tovar": "kilimok", "kilkist": 100, "cina": 150}
]

def rahuvati_dohid(spisok):
    rezultat = {}
    for zapys in spisok:
        nazva = zapys["tovar"]
        # Рахуємо гроші за цей продаж
        groshi = zapys["kilkist"] * zapys["cina"]
        
        if nazva in rezultat:
            rezultat[nazva] = rezultat[nazva] + groshi
        else:
            rezultat[nazva] = groshi
    return rezultat

# Отримуємо результати
dohid_po_tovarah = rahuvati_dohid(prodazhi)
print("Дохід по кожному товару:")
print(dohid_po_tovarah)

# Шукаємо товари де дохід більше 1000
pributkovi = []
for kluch in dohid_po_tovarah:
    summa = dohid_po_tovarah[kluch]
    if summa > 1000:
        pributkovi.append(kluch)

print("Товари з доходом понад 1000:")
print(pributkovi)
