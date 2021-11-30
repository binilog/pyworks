# GoldCustomer 클래스 정의 - Customer를 상속받음
from day09.class_lib.customer import Customer


class GoldCustomer(Customer):
    def __init__(self, cid, name):
        super().__init__(cid, name)  # 부모 멤버 상속
        self.cgrade = "GOLD"  # 등급 : GOLD
        self.sale_ratio = 0.1  # 할인 sale 10%
        self.bonus_ratio = 0.02  # 보너스 적립율

    def calc_price(self, price):
        price -= int(price * self.sale_ratio) #int는 정수로 변경
        #할인된 가격은 가격 - (가격 x 구매 할인율)
        #10000 - 10000x 0.1
        # 10000 - 1000 = 9000 는 할인된 가격이다.
        self.bonus_point += int(price * self.bonus_ratio)
        return price

