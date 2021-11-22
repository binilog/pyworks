# dan = 3
# print("", dan, "의 배수")
# for i in range(1, 21):
#     print('3의', i, '배수는', dan * i)

# num = 3
# print(",num,")
count = 0
sum = 0
for i in range(1,21):
    if i % 3 == 0:
        count += 1
        sum += i
        print(i, end=' ')
avg = sum / count
print()
print("3의 배수의 갯수 :", count)
print("3의 배수의 합계 :", sum)
print("3의 배수의 평균 :", avg)