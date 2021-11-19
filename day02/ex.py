# # for i in range(0, 5):
# #     for j in range(0, 5):
# #         print("$", end=' ')
# #     print()
# # for i in range(0, 10):
# #     for j in range(0, 1+i):
# #         print("$", end=' ')
# #     print()
# # 5행 5열 안에 1부터 순차적으로 증가.
# for i in range(0, 10):
#     for j in range(0, 1+i):
#         print("$", end=' ')
#     print()
customer = int(input("입장객 수 입력 : "))
col = int(input("좌석 열 수 입력:"))
if customer % col == 0:
    row = int(customer / col)
else:
    row = customer // col + 1
    
for i in range(0, row):
    for j in range(1, col+1):
        seat = i * col + j
        if seat > customer:
            break
        print("좌석",str(seat), end=' ')
    print()