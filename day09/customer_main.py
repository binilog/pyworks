from day09.class_lib.customer import Customer
from day09.class_lib.goldcustomer import GoldCustomer
from day09.class_lib.vipcustomer import VIPCustomer

c = Customer(101, "놀부")  # 객체 생성
g = GoldCustomer(201, "흥부")  # 얘도 객체 생성
v = VIPCustomer(301, "심청", 1004)

# 제품 구매 ()< 10000원
cost_c = c.calc_price(10000)
cost_g = g.calc_price(10000)
cost_v = v.calc_price(10000)

# 제품 지불 비용을 출력해보쟈
print(c.getname() + "님의 지불비용은 " + str(cost_c) + "원 입니다.")
print(g.getname() + "님의 지불비용은 " + str(cost_g) + "원 입니다.")
print(v.getname() + "님의 지불비용은 " + str(cost_v) + "원 입니다.")

print()

print(c)
print(g)
print(v)

# print("뭐 이해가 안간다 언제나\n" * 100)
