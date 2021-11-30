# 로또 복권 생성 프로그램
# 1~45중에 추첨
import random

# lotto = [] 빈 리스트 준비
lotto = []
# 로또 복권 번호 1개 추첨

num1 = random.randint(1, 45)
num2 = random.randint(1, 45)
num3 = random.randint(1, 45)
num4 = random.randint(1, 45)
num5 = random.randint(1, 45)
num6 = random.randint(1, 45)

print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)

for i in range(0, 6):
    num = random.randint(1, 45)
    # print(num, end=' ')
    if num not in lotto:
        lotto.append(num)

while len(lotto) < 6:
    num = random.randint(1, 45)
    if num not in lotto:
        lotto.append(num)




print(lotto)






