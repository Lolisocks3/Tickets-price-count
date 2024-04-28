age = int(input("Сколько вам лет: "))
tickets = int(input("Сколько билетов вы хотите купить?: "))

if age < 18:
    price = 0


if age >= 18 and age <= 25:
    price = 990
if age > 25:
   price = 1390
if tickets > 3:
    price = price * 0.9

print("Итого", int(price), "рублей")
