# VIPcustomer 클래스 정의
from day09.class_lib.customer import Customer

class VIPCustomer(Customer):
    def __init__(self, cid, name, agent):
        super().__init__(cid, name) #부모 멤버 상속
        self.agent = agent       #전문상담원 멤버 >>>>agent
        self.cgrade = "VIP"      #등급은 vip
        self.sale_ratio = 0.1       #할인율 10%
        self.bonus_ratio = 0.05   #보너스 적립5%

    def calc_price(self, price):
        price -= int(price * self.sale_ratio)  # int는 정수로 변경
        # 할인된 가격은 가격 - (가격 x 구매 할인율)
        # 10000 - 10000x 0.1
        # 10000 - 1000 = 9000 는 할인된 가격이다.
        self.bonus_point += int(price * self.bonus_ratio)
        return price

    def __str__(self):
        return super().__str__() + "  \n전문 상담원 ID는 {}입니다.".format(self.agent)