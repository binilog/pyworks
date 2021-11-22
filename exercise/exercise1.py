# a = "life is too short, you need python"
#
# if "wife" in a:
#     print("wife")
# elif "python" in a and "you" not in a:
#     print("python")
# elif "shirt" not in a:
#     print("shirt")
# elif "need" in a:
#     print("need")
# else:
#     print("none")

#1000까지의 숫자중 3의 배수 모든 값을 더한 값 출력
# num = 0
# i = 1
# while i <= 1000:
#     if i % 3 == 0:
#         num += i
#     i+= 1
#
# print(num)

# i = 0
# while True:
#     i += 1
#     if i > 5: break
#     print('*' * i)

# for i in range(1,101):
#     print(i)

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
count = len(A)
total = 0
average = 0.0
for i in A:
    total += i
average = total / count
print("점수 :", A)
print("총합 :", sum(A))
print("평균 :", average)
