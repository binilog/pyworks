name = input("이름을 입력하세요: ")
height = float(input("키를 입력하세요 :"))
height = height / 100
weight = float(input("몸무게를 입력하세요: "))

bmi = weight / (height * height)

print("%s님의 bmi는 %.2f입니다" % (name, bmi))

if bmi < 20:
    print("저체중입니다.")
elif bmi < 25:
    print("정상입니다.")
elif bmi < 30:
    print("과체중입니다.")
