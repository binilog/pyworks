# 자리배치도 프로그램
# 고객수를 열(좌석)로 나눠 행(줄)을 구해서 for문으로 배치
customer_num = int(input("입장객 수 입력 : "))
col_num = int(input("좌석 열 수 입력 : "))

# 나머지 없는 경우 있는 경우로 row 계산
if customer_num % col_num == 0:
    row = customer_num % col_num
else:
    row = customer_num % col_num + 1  #몫 + 1

for i in range(0, row):
    for j in range(1, col_num+1):
        seat = i*col_num+j
        if seat > customer_num:
            break
        print("좌석" + str(seat), end=' ')
    print()