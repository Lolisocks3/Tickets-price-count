total_price = 0
tickets_count = int(input("Сколько билетов вы хотите купить? "))

for i in range(tickets_count):
    age = int(input(f"Введите возраст посетителя {i+1}: "))
    if age < 18:
        price = 0
    elif 18 <= age < 25:
        price = 990
    else:
        price = 1390
    total_price += price

if tickets_count > 3:
    total_price *= 0.9

total_price = round(total_price) 

print(f"Сумма к оплате: {total_price} руб.")
