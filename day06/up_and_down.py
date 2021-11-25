#숫자 추측 게임
import random

com = random.randint(1, 100) #컴퓨터가 1~100 난수 생성
min_v = 1
max_v = 100

for i in range(10):
    guess = int(input("맞혀보거라([%d회] %d~%d) -> " % (i+1, min_v, max_v)))
    if guess == com:
        print(("*****")*1234)
        break
    elif guess > com:
        print("틀렸다\n그보다 작다 애송아")
        max_v = guess
    else:
        print("아니다\n그보다 크다 애송아")
        min_v = guess
print("걍 알려준다 정답은 %d 이다" % com)
print("니 점수는 %d점따리" % ((10-i) *10))