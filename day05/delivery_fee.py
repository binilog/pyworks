def get_price(unit_price, quantity):
    delivery_fee = 2500
    price = unit_price * quantity

    if price < 20000:
      price += delivery_fee
      return price
    else: return price

price1 = get_price(15000, 2)
price2 = get_price(5000, 3)

print("상품1 가격은 " + str(price1) + "원 입니다.")
print("상품2 가격은 " + format(price2, ',d') + "원 입니다.")

