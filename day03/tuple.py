# tuple(튜플) 자료구조
# 요소를 추가 삭제 변경할 수 없다
# 리스트와 인덱싱이나 슬라이싱 방식이 같음
# 소괄호()를 사용
t1 = ("011008-3123412")
print(t1)

print()

t1 = (1,2 )
print(t1)
print(type(t1))
# t1 = (1)
# print(t1)
# print(type(t1))
t2 = (2, 3, 4)
t1 = t2 + t1        #입력한 항의 순서에 따라서 바뀌네
print(t1)
print(t1[0])
print(t1[-4])
print(t1[2:])

# t1[1] = 5