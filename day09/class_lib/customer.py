# Customer 클래스

class Customer:
    def __init__(self, cid, name):
        self.cid = cid
        self.name = name
        self.cgrade = "SILVER"
        self.bonus_point = 0
        self.bonus_ratio = 0.01

    def getname(self):
        return self.name
    def calc_price(self, price):
        self.bonus_point += int(price * self.bonus_ratio)
        # 보너스 포인트는 정수로 변경 - 가격 x 보너스 적립율
        return price

    def __str__(self):
        return "{}님의 등급은 {} 이고, 보너스 포인트는 {}점입니다."\
            .format(self.name, self.cgrade, self.bonus_point)









