area = 60
price = 5000
total_price = 0
total = 0
for year in range(1, 6):
    if year % 2 == 1 and year != 1:
        price += 1000
    total_price = price*area
    total += total_price
    print(f"Year {year}: {int(total_price)}\tPrice per 0.25 acres/0.1 Hectare: {price}")
print(f"Total Price: {total}")