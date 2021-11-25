#random() - 무작위수(난수) 추출
import math
import random

print(random.random()) #0.0 <= x < 1.0 x는 0.0보다 크거나 같지만 1.0보단 작다.

dice = random.random() * 6 + 1
print(math.floor(dice))
# randint(처음,끝) : 처음과 끝사이의 난수 그냥 제한을 건다 이말이지 1 이상 6이하
dice2 = random.randint(1, 6)
print(dice2)
#이건 lis 저기에서 무작위로 뺄때 쓰는거 lis안에 있는 저거저거 항목
lis = ["강아지", "고양이", "햄스터", "소"]
print(random.choice(lis))
# 리스트의 항목을 무작위로 섞기 순서 상관없이 다 바뀜 ㅇㅇ
random.shuffle(lis)
print(lis)

