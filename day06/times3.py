# 1부터 100까지의 수 중에서 배수 출력

def times(x):
    global count
    for i in range(1, 101):
        if i % x == 0:
            count += 1
            print(i, end=' ')

            # print(count)
count = 0
times()
print("\n 3의 배수의 개수 : " + str(count) + "개")