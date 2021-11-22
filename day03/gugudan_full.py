#구구단 출력

dan = int(input('단을 입력하세요 : '))

print("[", dan, "]단")
for i in range(1, 10):
    print(dan, 'x', i, '=', dan*i)


for i in range(2, 10):
    for j in range(1, 10):
        print(i, 'x', j, '=', (i*j)