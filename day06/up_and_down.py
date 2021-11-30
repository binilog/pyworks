#숫자 추측 게임
import random

com = random.randint(1, 100) #컴퓨터가 1~100 난수 생성
min_v = 1
max_v = 100

for i in range(10):
    try:
        guess = int(input("맞혀봐([%d회] %d~%d) -> " % (i+1, min_v, max_v)))
        if guess > 100 or guess < 1:
            print("입력 범위를 초과했어요. 다시 입력해 주세요.")
        elif guess == com:
            print(("*****")*1234)
            break
        elif guess > com:
            print("틀렸다\n그보다 작다")
            max_v = guess
        else:
            print("아니다\n그보다 크다")
            min_v = guess
    except:
        print("숫자가 아닙니다. 다시 입력해 주세요")
# print(i)
print("정답은 %d 이다" % com)
print("점수는 %d점" % ((10-i) *10))